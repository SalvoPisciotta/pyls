import argparse
from src.exception import InvalidArgumentError
import sys


def get_parser():
    """
    Function to create the argument parser for the pyls.
    The parser includes the following argument:
    - `-A`: A boolean flag that, if True, includes all files,
      including those starting with a dot.(eg. .gitignore)
    Returns:
        argparse.ArgumentParser: The argument parser.
    """

    parser = argparse.ArgumentParser(description="Parser for pyls")
    parser.add_argument("path",
                        default= '.',
                        help="Path of the folder to navigate on with ls")
    parser.add_argument(
        "-A",
        action="store_true",
        default=False,
        help="Get all the items elements, included the one starting with .",
    )

    parser.add_argument(
        "-l",
        action="store_true",
        default=False,
        help="Get additional items information",
    )
    parser.add_argument(
        "-r",
        action="store_true",
        default=False,
        help="Get items in reverse order",
    )
    parser.add_argument(
        "-t",
        action="store_true",
        default=False,
        help="Get items sorted by time modified property",
    )
    parser.add_argument(
        "--filter",
        default=None,
        help="Filter options: 'file' for files, 'dir' for directories."
    )
    return parser

def _check_args(args):
    if args.filter not in ["file", "dir", None]:
        raise InvalidArgumentError(
            f"error: {args.filter} is not a valid filter criteria."
            + "Available filters are 'file' or 'dir'.")
    
def check_args(args):
    try:
        _check_args(args)  # This will raise the error
    except InvalidArgumentError as e:
        # Print only the message without traceback
        print(f"{e}")
        sys.exit()