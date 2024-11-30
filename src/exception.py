class InvalidArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidPathError(Exception):
    def __init__(self, message):
        super().__init__(message)