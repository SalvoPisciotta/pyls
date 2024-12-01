class InvalidArgumentError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidPathError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
