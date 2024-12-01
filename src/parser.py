import argparse
from src.exception import InvalidArgumentError
import sys

help_string ="""
Python 'ls' command implementation for structured JSON files simulating a file system.

The goal is to navigate through a JSON structure and display the content of files and directories.

The JSON file has to have the following structure:
{
    'name': 'dir1',
    'size': 4096,
    'time_modified': 1699957865,
    'permissions': '-rw-r--r--',
    'contents': [
        {
            'name': 'file1',
            'size': 8911,
            'time_modified': 1699941437,
            'permissions': 'drwxr-xr-x'
        }
    ]
}
"""

def get_parser():
    """
    Creates and returns an argument parser for the pyls command-line tool.
    The parser supports the following arguments:
    - path: The path of the folder to navigate with ls (default is current directory).
    - -A: Include all items, including those starting with a dot.
    - -l: Display additional information about items.
    - -r: Display items in reverse order.
    - -t: Sort items by the time they were last modified.
    - -h: Display human-readable sizes for items.
    - --filter: Filter options to display only files with 'file' or directories with 'dir'.
    Returns:
        argparse.ArgumentParser: Configured argument parser for pyls.
    """
    parser = argparse.ArgumentParser(description=help_string,
                                    add_help=False,
                                    formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument("path",
                        default= '.',
                        nargs='?',
                        help="Path of the folder to navigate on with ls '.' is set by default")
    parser.add_argument(
        "-A",
        action="store_true",
        default=False,
        help="Include all items, including those starting with a dot.",
    )

    parser.add_argument(
        "-l",
        action="store_true",
        default=False,
        help="Display additional information about items",
    )
    parser.add_argument(
        "-r",
        action="store_true",
        default=False,
        help="Display items in reverse order.",
    )
    parser.add_argument(
        "-t",
        action="store_true",
        default=False,
        help="Sort items by the time they were last modified.",
    )
    parser.add_argument(
        "-h",
        action="store_true",
        default=False,
        help="Display human-readable sizes for items.",
    )
    parser.add_argument(
        "--filter",
        default=None,
        help="Filter options to display only files with 'file' or directories with 'dir'."
    )
    parser.add_argument(
        "--help",
        action="store_true",
        default=None,
        help="Filter options to display only files with 'file' or directories with 'dir'."
    )
    return parser

def _check_args(args):
    """
    Validates the filter argument in the provided args.
    Raises InvalidArgumentError exception if the filter attribute is not 'file', 'dir', or None.
    Args:
        args: An object that contains the filter attribute.

    """
    
    if args.filter not in ["file", "dir", None]:
        raise InvalidArgumentError(
            f"error: {args.filter} is not a valid filter criteria."
            + "Available filters are 'file' or 'dir'.")
    
def check_args(args):
    """
    Check the validity of the provided arguments.
    This function attempts to validate the given arguments by calling `_check_args`.
    If `InvalidArgumentError` exception is raised, prints the error message and exits the program.
    Args:
        args: The arguments to be checked.
    """
    try:
        _check_args(args)  # This will raise the error
    except InvalidArgumentError as e:
        # Print only the message without traceback
        print(f"{e}")
        sys.exit()