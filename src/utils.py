from datetime import datetime
import math
from typing import Union

HUMAN_READABLE_SYMBOLS = ["K", "M", "G"]


def approx_number(number: Union[float, int]) -> float:
    """
    Approximate a number to the nearest tenth.
    Args:
        number (float or int): The number to be approximated.
    Returns:
        float: The number rounded up to the nearest tenth.
    """
    approx_number = math.ceil(number * 10) / 10

    return approx_number


def human_readable_file_size(file_size: int) -> str:
    """
    Convert a file size in bytes to a human-readable string with appropriate units.
    Args:
        file_size (int): The size of the file in bytes.
    Returns:
        str: A human-readable string representing the file size with appropriate units.
    """
    if file_size // 1024 == 0:
        return str(file_size)
    else:
        abbreviation_index = 0
        while (
            file_size >= 1024 and abbreviation_index < len(HUMAN_READABLE_SYMBOLS) - 1
        ):
            file_size /= 1024
            abbreviation_index += 1
        abbreviation_symbol = HUMAN_READABLE_SYMBOLS[abbreviation_index]
    return str(approx_number(file_size)) + abbreviation_symbol


def human_readable_datetime(datetime_timestamp: int) -> str:
    """
    Convert a datetime timestamp to a human-readable string.
    Args:
        datetime_timestamp (int): The timestamp of the datetime.
    Returns:
        str: A human-readable string representing the datetime.
    """
    return datetime.fromtimestamp(datetime_timestamp).strftime("%b %d %H:%M")
