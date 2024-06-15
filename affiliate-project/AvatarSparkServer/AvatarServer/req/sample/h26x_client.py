import itertools
import os
import sys

from sample import nalutypes

import bitstring


class H26xParser:
    """
    H.264 extractor for Annex B streams.
    """
    START_CODE_PREFIX = "0x00000001"
    START_CODE_PREFIX_SHORT = "0x000001"
    VALID_CALLBACKS = [
        "sps",
        "pps",
        "slice",
        "aud",
        "nalu"
    ]

    def __init__(self, f, verbose=False, use_bitstream=None):
        """
        Create a new extractor for a .264/h264 file in Annex B format.

        f: input file
        use_bitstream: blob to use as bitstream (for testing)
        verbose: whether to print out NAL structure and fields
        """
        if use_bitstream:
            self.file = None
            self.stream = bitstring.BitStream(use_bitstream)
        else:
            fn, ext = os.path.splitext(os.path.basename(f))
            valid_input_ext = ['.264', '.h264']
            if not ext in valid_input_ext:
                raise RuntimeError("Valid input types: " + str(valid_input_ext))
            bitstream_file = f
            self.file = bitstream_file
            self.stream = bitstring.BitStream(filename=bitstream_file)
        self.verbose = verbose
        self.callbacks = {}
        self.nalu_len = 0

    def set_callback(self, name, fun):
        """
        Set a callback function for raw data extracted. The function will be called with the raw
        bytes of the complete NALU. Valid callbacks are:

        - aud: for every AUD found
        - nalu: for every complete NAL unit found
        - sps: for every SPS NAL unit found
        - pps: for every PPS NAL unit found
        - slice: for every VCL NAL unit found with a slice in it (args: data, buffer_size, first_mb_in_slice)

        Raw data for all callbacks never includes the start code, but all the NAL headers, except
        for the "nalu" callback.
        """
        if name not in self.VALID_CALLBACKS:
            raise RuntimeError(name + " is not a valid callback. Choose one of " + str(self.VALID_CALLBACKS) + ".")
        if not callable(fun):
            raise RuntimeError(str(fun) + " is not a callable function")

        self.callbacks[name] = fun

    def __call(self, name, *args):
        """
        Calls a given callback, and silently skips if it is not implemented.

        name: name of the callback, e.g. "nalu", "aud", whatever
        args: will be expanded to the list of arguments, so you can call this with:
              self.__call("foo", arg1, arg2, ...)
        """
        if name not in self.VALID_CALLBACKS:
            return
        if name not in self.callbacks.keys():
            return
        else:
            self.callbacks[name](*args)

    def _get_nalu_positions(self):
        """
        Saves all the NALU positions as bit positions in self.nal_unit_positions
        """
        self.nal_unit_positions = list(self.stream.findall(self.START_CODE_PREFIX, bytealigned=True))
        self.short_nal_unit_positions = list(self.stream.findall(self.START_CODE_PREFIX_SHORT, bytealigned=True))

        if not self.nal_unit_positions and not self.short_nal_unit_positions:
            # fixme 集成时注意删除
            print("No NALUs found in stream")
            sys.exit(1)

        if not self.nal_unit_positions:
            self.nal_unit_positions = self.short_nal_unit_positions
        else:
            # if there were extraneous 3-byte NAL unit start codes, use them too
            extra_nal_unit_pos = set([max(s - 8, 0) for s in self.short_nal_unit_positions]) - set(
                self.nal_unit_positions)
            if len(extra_nal_unit_pos) and self.nal_unit_positions:
                if self.verbose:
                    print("Warning: 3-byte extra NAL unit start code found")
                self.nal_unit_positions.extend([s + 8 for s in extra_nal_unit_pos])
                self.nal_unit_positions = sorted(self.nal_unit_positions)

        self.end_of_stream = len(self.stream)
        self.nal_unit_positions.append(self.end_of_stream)
        self.nalu_len = len(self.nal_unit_positions) - 1
        return self.nal_unit_positions

    def _decode_nalu(self, nalu_bytes):
        """
        Returns nal_unit_type and RBSP payload from a NALU stream
        """
        if "0x" + nalu_bytes[0: 4 * 8].hex == self.START_CODE_PREFIX:
            start_code = nalu_bytes.read('bytes:4')
        else:
            start_code = nalu_bytes.read('bytes:3')
        forbidden_zero_bit = nalu_bytes.read(1)
        nal_ref_idc = nalu_bytes.read('uint:2')
        nal_unit_type = nalu_bytes.read('uint:5')
        nal_unit_payload = nalu_bytes[nalu_bytes.pos:]

        rbsp_payload = bitstring.BitStream()
        for i in range(int(len(nal_unit_payload) / 8)):
            if len(nal_unit_payload) - nal_unit_payload.pos >= 24 and \
                    nal_unit_payload.peek('bits:24') == '0x000003':
                rbsp_payload.append(nal_unit_payload.read('bits:8'))
                rbsp_payload.append(nal_unit_payload.read('bits:8'))
                nal_unit_payload.read('bits:8')
            else:
                if nal_unit_payload.pos == len(nal_unit_payload):
                    continue
                rbsp_payload.append(nal_unit_payload.read('bits:8'))

        return nal_unit_type, rbsp_payload

    def parse(self):
        """
        Parse the bitstream and extract each NALU.
        Call the respective callbacks for each NALU type found.
        """
        self._get_nalu_positions()
        nalu_sps = None
        nalu_pps = None
        i = 0
        for current_nalu_pos, next_nalu_pos in zip(self.nal_unit_positions, itertools.islice(self.nal_unit_positions, 1, None)):
            i = i + 1
            current_nalu_bytepos = int(current_nalu_pos / 8)
            next_nalu_bytepos = int(next_nalu_pos / 8)
            nalu_bytes = self.stream[current_nalu_pos: next_nalu_pos]

            self.__call('nalu', nalu_bytes)

            if self.verbose:
                print("\r\n")
                print("=============================================================")
                print("")
                print("NALU bytepos:\t[" + str(current_nalu_bytepos) + ", " + str(next_nalu_bytepos - 1) + "]")
                print("NALU offset:\t" + str(current_nalu_bytepos) + " Bytes")
                print(
                    "NALU length:\t" + str(next_nalu_bytepos - current_nalu_bytepos) + " Bytes (including start code)")

            current_nalu_stream_segment = bitstring.BitStream(self.stream[current_nalu_pos: next_nalu_pos])

            nal_unit_type, rbsp_payload = self._decode_nalu(current_nalu_stream_segment)

            if self.verbose:
                print("NALU type:\t" + str(nal_unit_type) + " (" + nalutypes.get_description(nal_unit_type) + ")")
                print("NALU bytes:\t" + str(nalu_bytes))
                print("NALU RBSP:\t" + str(rbsp_payload))
                print("")

            if nal_unit_type == nalutypes.NAL_UNIT_TYPE_SPS:
                nalu_sps = nalutypes.SPS(rbsp_payload, self.verbose)
                self.__call('sps', rbsp_payload)
            elif nal_unit_type == nalutypes.NAL_UNIT_TYPE_PPS:
                nalu_pps = nalutypes.PPS(rbsp_payload, self.verbose)
                self.__call('pps', rbsp_payload)
            elif nal_unit_type == nalutypes.NAL_UNIT_TYPE_AUD:
                aud = nalutypes.AUD(rbsp_payload, self.verbose)
                self.__call('aud', rbsp_payload)
            elif nal_unit_type == nalutypes.NAL_UNIT_TYPE_CODED_SLICE_NON_IDR:
                nalu_slice = nalutypes.CodedSliceNonIDR(rbsp_payload, nalu_sps, nalu_pps, self.verbose)
                self.__call('slice', rbsp_payload)
            elif nal_unit_type == nalutypes.NAL_UNIT_TYPE_CODED_SLICE_IDR:
                nalu_slice = nalutypes.CodedSliceIDR(rbsp_payload, nalu_sps, nalu_pps, self.verbose)
                self.__call('slice', rbsp_payload)

    def h264_data_list(self):
        """
        Parse the bitstream and extract each NALU.
        Call the respective callbacks for each NALU type found.
        """
        self._get_nalu_positions()
        h264_data_list = []
        num = 1
        tmp_nalu_data = b""
        frame_len = self.nalu_len
        for current_nalu_pos, next_nalu_pos in zip(self.nal_unit_positions, itertools.islice(self.nal_unit_positions, 1, None)):
            nalu_bytes = self.stream[current_nalu_pos: next_nalu_pos]
            current_nalu_stream_segment = bitstring.BitStream(self.stream[current_nalu_pos: next_nalu_pos])
            nal_unit_type, rbsp_payload = self._decode_nalu(current_nalu_stream_segment)
            if num == 1:
                ws_type = 0
            else:
                ws_type = 1
            if num == frame_len:
                ws_type = 2
            # 帧数据整合
            if nal_unit_type in [nalutypes.NAL_UNIT_TYPE_SPS, nalutypes.NAL_UNIT_TYPE_SEI, nalutypes.NAL_UNIT_TYPE_PPS,
                                 nalutypes.NAL_UNIT_TYPE_AUD]:
                # h264 协议帧
                tmp_nalu_data = tmp_nalu_data + nalu_bytes.bytes
                frame_len = frame_len - 1
                continue
            if nal_unit_type == nalutypes.NAL_UNIT_TYPE_CODED_SLICE_IDR:
                tmp_nalu_data = tmp_nalu_data + nalu_bytes.bytes
                h264_data = [tmp_nalu_data, ws_type, len(tmp_nalu_data)]
                tmp_nalu_data = b""
            else:
                h264_data = [nalu_bytes.bytes, ws_type, int(nalu_bytes.len / 8)]
            h264_data_list.append(h264_data)
            num = num + 1
        return h264_data_list

    def get_nalu_data(self):
        self._get_nalu_positions()
        nalu_relative_pos = zip(self.nal_unit_positions, itertools.islice(self.nal_unit_positions, 1, None))
        for current_nalu_pos, next_nalu_pos in nalu_relative_pos:
            yield self.nalu_data_format(current_nalu_pos, next_nalu_pos)

    def nalu_data_format(self, cpos, npos):
        nalu_bytes = self.stream[cpos: npos]
        current_nalu_stream_segment = bitstring.BitStream(self.stream[cpos: npos])
        nal_unit_type, rbsp_payload = self._decode_nalu(current_nalu_stream_segment)
        h264_data = {
            "type": nal_unit_type,
            "data": nalu_bytes.bytes,
            "other": nalu_bytes.len
        }
        return h264_data