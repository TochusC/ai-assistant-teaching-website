# nalutypes.py
#
# The MIT License (MIT)
#
# Copyright (c) 2017 Werner Robitza
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.>

from tabulate import tabulate

# NAL REF IDC codes
NAL_REF_IDC_PRIORITY_HIGHEST = 3
NAL_REF_IDC_PRIORITY_HIGH = 2
NAL_REF_IDC_PRIORITY_LOW = 1
NAL_REF_IDC_PRIORITY_DISPOSABLE = 0

# NAL unit type codes
NAL_UNIT_TYPE_UNSPECIFIED = 0  # Unspecified
NAL_UNIT_TYPE_CODED_SLICE_NON_IDR = 1  # Coded slice of a non-IDR picture
NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_A = 2  # Coded slice data partition A
NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_B = 3  # Coded slice data partition B
NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_C = 4  # Coded slice data partition C
NAL_UNIT_TYPE_CODED_SLICE_IDR = 5  # Coded slice of an IDR picture
NAL_UNIT_TYPE_SEI = 6  # Supplemental enhancement information (SEI)
NAL_UNIT_TYPE_SPS = 7  # Sequence parameter set
NAL_UNIT_TYPE_PPS = 8  # Picture parameter set
NAL_UNIT_TYPE_AUD = 9  # Access unit delimiter
NAL_UNIT_TYPE_END_OF_SEQUENCE = 10  # End of sequence
NAL_UNIT_TYPE_END_OF_STREAM = 11  # End of stream
NAL_UNIT_TYPE_FILLER = 12  # Filler data
NAL_UNIT_TYPE_SPS_EXT = 13  # Sequence parameter set extension
# 14..18    # Reserved
NAL_UNIT_TYPE_CODED_SLICE_AUX = 19  # Coded slice of an auxiliary coded picture without partitioning


# 20..23    # Reserved
# 24..31    # Unspecified

def get_description(nal_unit_type):
    """
    Returns a clear text description of a NALU type given as an integer
    """
    return {
        NAL_UNIT_TYPE_UNSPECIFIED: "Unspecified",
        NAL_UNIT_TYPE_CODED_SLICE_NON_IDR: "Coded slice of a non-IDR picture",
        NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_A: "Coded slice data partition A",
        NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_B: "Coded slice data partition B",
        NAL_UNIT_TYPE_CODED_SLICE_DATA_PARTITION_C: "Coded slice data partition C",
        NAL_UNIT_TYPE_CODED_SLICE_IDR: "Coded slice of an IDR picture",
        NAL_UNIT_TYPE_SEI: "Supplemental enhancement information (SEI)",
        NAL_UNIT_TYPE_SPS: "Sequence parameter set",
        NAL_UNIT_TYPE_PPS: "Picture parameter set",
        NAL_UNIT_TYPE_AUD: "Access unit delimiter",
        NAL_UNIT_TYPE_END_OF_SEQUENCE: "End of sequence",
        NAL_UNIT_TYPE_END_OF_STREAM: "End of stream",
        NAL_UNIT_TYPE_FILLER: "Filler data",
        NAL_UNIT_TYPE_SPS_EXT: "Sequence parameter set extension",
        NAL_UNIT_TYPE_CODED_SLICE_AUX: "Coded slice of an auxiliary coded picture without partitioning"
    }.get(nal_unit_type, "unknown")


def _get_slice_type(slice_type):
    """
    Returns the clear name of the slice type
    """
    return {
        0: "P",
        1: "B",
        2: "I",
        3: "SP",
        4: "SI",
        5: "P",
        6: "B",
        7: "I",
        8: "SP",
        9: "SI",
    }.get(slice_type, "unknown")


class NALU(object):
    """
    Class representing a NAL unit, to be initialized with its payload only.
    The type must be inferred from the NALU header, before initializing the NALU by its subclass.
    """

    def __init__(self, rbsp_bytes, verbose, order=None):
        self.s = rbsp_bytes
        self.verbose = verbose
        self.order = order

    def print_verbose(self):
        if self.verbose:
            print(self.__class__.__name__ + " (payload size: " + str(len(self.s) / 8) + " Bytes)")
            to_print = []
            if self.order is not None:
                for key in self.order:
                    if key in vars(self):
                        value = vars(self)[key]
                        to_print.append([key, value])
            for key, value in sorted(vars(self).items()):
                if key == "verbose" or key == "s" or key == "order":
                    continue
                if self.order and key in self.order:
                    continue
                to_print.append([key, value])
            print(tabulate(to_print, headers=["field", "value"], tablefmt="grid"))


class AUD(NALU):
    """
    Access Unit Delimiter
    """

    def __init__(self, rbsp_bytes, verbose):
        super(AUD, self).__init__(rbsp_bytes, verbose)

        self.primary_pic_type = self.s.read('uint:3')

        self.print_verbose()


class CodedSliceIDR(NALU):
    """
    Coded slice of an IDR picture.
    """

    def __init__(self, rbsp_bytes, nalu_sps, nalu_pps, verbose):
        order = [
            'first_mb_in_slice',
            'slice_type',
            'slice_type_clear',
            'pic_parameter_set_id',
            'colour_plane_id',
            'frame_num',
            'field_pic_flag',
            'bottom_field_flag',
            'idr_pic_id',
        ]
        super(CodedSliceIDR, self).__init__(rbsp_bytes, verbose, order)
        # parse slice_header
        self.first_mb_in_slice = self.s.read('ue')
        self.slice_type = self.s.read('ue')
        self.slice_type_clear = _get_slice_type(self.slice_type)
        self.pic_parameter_set_id = self.s.read('ue')
        if ('separate_colour_plane_flag' in dir(nalu_sps) and
                nalu_sps.separate_colour_plane_flag == 1):
            self.colour_plane_id = self.s.read('uint:2')
        self.frame_num = self.s.read('uint:%i' % (nalu_sps.log2_max_frame_num_minus4 + 4))
        if not nalu_sps.frame_mbs_only_flag:
            self.field_pic_flag = self.s.read('uint:1')
            if self.field_pic_flag:
                self.bottom_field_flag = self.s.read('uint:1')
        IdrPicFlag = 1
        if IdrPicFlag:
            self.idr_pic_id = self.s.read('ue')

        self.print_verbose()


class CodedSliceNonIDR(NALU):
    """
    Coded slice of a non-IDR picture.
    """

    def __init__(self, rbsp_bytes, nalu_sps, nalu_pps, verbose):
        super(CodedSliceNonIDR, self).__init__(rbsp_bytes, verbose)

        # parse slice_header
        self.first_mb_in_slice = self.s.read('ue')
        self.slice_type = self.s.read('ue')
        self.slice_type_clear = _get_slice_type(self.slice_type)
        self.pic_parameter_set_id = self.s.read('ue')

        self.print_verbose()


class SPS(NALU):
    """
    Sequence Parameter Set class
    """

    def __init__(self, rbsp_bytes, verbose):
        order = [
            'profile_idc',
            'constraint_set0_flag',
            'constraint_set1_flag',
            'constraint_set2_flag',
            'constraint_set3_flag',
            'constraint_set4_flag',
            'constraint_set5_flag',
            'reserved_zero_2bits',
            'level_idc',
            'seq_parameter_set_id',
            'chroma_format_idc',
            'separate_colour_plane_flag',
            'bit_depth_luma_minus8',
            'bit_depth_chroma_minus8',
            'qpprime_y_zero_transform_bypass_flag',
            'seq_scaling_matrix_present_flag',
            'log2_max_frame_num_minus4',
            'pic_order_cnt_type',
            'log2_max_pic_order_cnt_lsb_minus4',
            'delta_pic_order_always_zero_flag',
            'offset_for_non_ref_pic',
            'offset_for_top_to_bottom_filed',
            'num_ref_frames_in_pic_order_cnt_cycle',
            'offset_for_ref_frame',
            'num_ref_frames',
            'gaps_in_frame_num_value_allowed_flag',
            'pic_width_in_mbs_minus_1',
            'pic_height_in_map_units_minus_1',
            'frame_mbs_only_flag',
            'mb_adapative_frame_field_flag',
            'direct_8x8_inference_flag',
            'frame_cropping_flag',
            'frame_crop_left_offst',
            'frame_crop_right_offset',
            'frame_crop_top_offset',
            'frame_crop_bottom_offset',
            'vui_parameters_present_flag',
        ]
        super(SPS, self).__init__(rbsp_bytes, verbose, order)

        # initializers
        self.offset_for_ref_frame = []
        self.seq_scaling_list_present_flag = []

        self.profile_idc = self.s.read('uint:8')
        self.constraint_set0_flag = self.s.read('uint:1')
        self.constraint_set1_flag = self.s.read('uint:1')
        self.constraint_set2_flag = self.s.read('uint:1')
        self.constraint_set3_flag = self.s.read('uint:1')
        self.constraint_set4_flag = self.s.read('uint:1')
        self.constraint_set5_flag = self.s.read('uint:1')
        self.reserved_zero_2bits = self.s.read('uint:2')
        self.level_idc = self.s.read('uint:8')
        self.seq_parameter_set_id = self.s.read('ue')

        if self.profile_idc in [100, 110, 122, 244, 44, 83, 86, 118, 128, 138, 139, 134, 135]:
            self.chroma_format_idc = self.s.read('ue')
            if self.chroma_format_idc == 3:
                self.separate_colour_plane_flag = self.s.read('uint:1')

            self.bit_depth_luma_minus8 = self.s.read('ue')
            self.bit_depth_chroma_minus8 = self.s.read('ue')
            self.qpprime_y_zero_transform_bypass_flag = self.s.read('uint:1')
            self.seq_scaling_matrix_present_flag = self.s.read('uint:1')

            if self.seq_scaling_matrix_present_flag:
                # TODO: have to implement this, otherwise it will fail
                raise NotImplementedError("Scaling matrix decoding is not implemented.")

        self.log2_max_frame_num_minus4 = self.s.read('ue')
        self.pic_order_cnt_type = self.s.read('ue')

        if self.pic_order_cnt_type == 0:
            self.log2_max_pic_order_cnt_lsb_minus4 = self.s.read('ue')
        elif self.pic_order_cnt_type == 1:
            self.delta_pic_order_always_zero_flag = self.s.read('uint:1')
            self.offset_for_non_ref_pic = self.s.read('se')
            self.offset_for_top_to_bottom_filed = self.s.read('se')
            self.num_ref_frames_in_pic_order_cnt_cycle = self.s.read('ue')
            for i in range(self.num_ref_frames_in_pic_order_cnt_cycle):
                self.offset_for_ref_frame.append(self.s.read('se'))

        self.num_ref_frames = self.s.read('ue')
        self.gaps_in_frame_num_value_allowed_flag = self.s.read('uint:1')
        self.pic_width_in_mbs_minus_1 = self.s.read('ue')
        self.pic_height_in_map_units_minus_1 = self.s.read('ue')
        self.frame_mbs_only_flag = self.s.read('uint:1')
        if not self.frame_mbs_only_flag:
            self.mb_adapative_frame_field_flag = self.s.read('uint:1')
        self.direct_8x8_inference_flag = self.s.read('uint:1')
        self.frame_cropping_flag = self.s.read('uint:1')
        if self.frame_cropping_flag:
            self.frame_crop_left_offst = self.s.read('ue')
            self.frame_crop_right_offset = self.s.read('ue')
            self.frame_crop_top_offset = self.s.read('ue')
            self.frame_crop_bottom_offset = self.s.read('ue')
        self.vui_parameters_present_flag = self.s.read('uint:1')

        # TODO: parse VUI
        # self.rbsp_stop_one_bit         = self.s.read('uint:1')

        self.print_verbose()


class PPS(NALU):
    def __init__(self, rbsp_bytes, verbose):
        order = [
            'pic_parameter_set_id',
            'seq_parameter_set_id',
            'entropy_coding_mode_flag',
            'pic_order_present_flag',
            'num_slice_groups_minus1',
            'slice_group_map_type',
            'run_length_minus1',
            'top_left',
            'bottom_right',
            'slice_group_change_direction_flag',
            'slice_group_change_rate_minus1',
            'pic_size_in_map_units_minus1',
            'slice_group_id',
            'num_ref_idx_l0_active_minus1',
            'num_ref_idx_l1_active_minus1',
            'weighted_pred_flag',
            'weighted_bipred_idc',
            'pic_init_qp_minus26',
            'pic_init_qs_minus26',
            'chroma_qp_index_offset',
            'deblocking_filter_control_present_flag',
            'constrained_intra_pred_flag',
            'redundant_pic_cnt_present_flag',
        ]
        super(PPS, self).__init__(rbsp_bytes, verbose, order)

        self.pic_parameter_set_id = self.s.read('ue')
        self.seq_parameter_set_id = self.s.read('ue')
        self.entropy_coding_mode_flag = self.s.read('uint:1')
        self.pic_order_present_flag = self.s.read('uint:1')
        self.num_slice_groups_minus1 = self.s.read('ue')
        if self.num_slice_groups_minus1 > 0:
            self.slice_group_map_type = self.s.read('ue')
            if self.slice_group_map_type == 0:
                self.run_length_minus1 = []
                for i_group in range(self.num_slice_groups_minus1 + 1):
                    self.run_length_minus1.append(self.s.read('ue'))
            elif self.slice_group_map_type == 2:
                self.top_left = []
                self.bottom_right = []
                for i_group in range(self.num_slice_groups_minus1 + 1):
                    self.top_left.append(self.s.read('ue'))
                    self.bottom_right.append(self.s.read('ue'))
            elif self.slice_group_map_type in [3, 4, 5]:
                self.slice_group_change_direction_flag = self.s.read('uint:1')
                self.slice_group_change_rate_minus1 = self.s.read('ue')
            elif self.slice_group_map_type == 6:
                self.pic_size_in_map_units_minus1 = self.s.read('ue')
                self.slice_group_id = []
                for i in range(self.pic_size_in_map_units_minus1 + 1):
                    self.slice_group_id.append(self.s.read('uint:1'))

        self.num_ref_idx_l0_active_minus1 = self.s.read('ue')
        self.num_ref_idx_l1_active_minus1 = self.s.read('ue')
        self.weighted_pred_flag = self.s.read('uint:1')
        self.weighted_bipred_idc = self.s.read('uint:2')
        self.pic_init_qp_minus26 = self.s.read('se')
        self.pic_init_qs_minus26 = self.s.read('se')
        self.chroma_qp_index_offset = self.s.read('se')
        self.deblocking_filter_control_present_flag = self.s.read('uint:1')
        self.constrained_intra_pred_flag = self.s.read('uint:1')
        self.redundant_pic_cnt_present_flag = self.s.read('uint:1')

        self.print_verbose()
