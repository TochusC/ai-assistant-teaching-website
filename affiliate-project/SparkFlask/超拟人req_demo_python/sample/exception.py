class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class FileNotFoundException(Exception):
    def __init__(self, msg):
        self.message = msg