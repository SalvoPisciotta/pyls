import argparse
from pyls.exceptions import InvalidArgumentError
import sys


class PyLSParser:

    def __init__(self) -> None:

        self.help_string = """
            Python 'ls' command implementation for structured JSON files simulating a file system.

            The goal is to navigate through this JSON file and showing content of files and folders.

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
        self.get_parser()
        self.args = self.parser.parse_args()
        self.check_args()
        if self.args.help:
            self.help_string_output()

    def get_parser(self) -> argparse.ArgumentParser:
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
        self.parser = argparse.ArgumentParser(
            description=self.help_string,
            add_help=False,
            formatter_class=argparse.RawTextHelpFormatter,
        )

        self.parser.add_argument(
            "path",
            default=".",
            nargs="?",
            help="Path of the folder to navigate on with ls '.' is set by default",
        )
        self.parser.add_argument(
            "-A",
            action="store_true",
            default=False,
            help="Include all items, including those starting with a dot.",
        )

        self.parser.add_argument(
            "-l",
            action="store_true",
            default=False,
            help="Display additional information about items",
        )
        self.parser.add_argument(
            "-r",
            action="store_true",
            default=False,
            help="Display items in reverse order.",
        )
        self.parser.add_argument(
            "-t",
            action="store_true",
            default=False,
            help="Sort items by the time they were last modified.",
        )
        self.parser.add_argument(
            "-h",
            action="store_true",
            default=False,
            help="Display human-readable sizes for items.",
        )
        self.parser.add_argument(
            "--filter",
            default=None,
            help="Filter options to display only files with 'file' or directories with 'dir'.",
        )
        self.parser.add_argument(
            "--help",
            action="store_true",
            default=None,
            help="Display the help message.",
        )

    def _check_filter_validity(self) -> None:
        """
        Validates the filter argument in the provided args.
        Raises InvalidArgumentError exception if the filter attribute is not 'file', 'dir', or None.
        Args:
            args: An object that contains the filter attribute.

        """
        if self.args.filter not in ["file", "dir", None]:
            raise InvalidArgumentError(
                f"error: {self.args.filter} is not a valid filter criteria."
                + " Available filters are 'file' or 'dir'."
            )

    def check_args(self) -> None:
        """
        Check the validity of the provided arguments.
        This function attempts to validate the given arguments by calling `_check_args`.
        If `InvalidArgumentError` exception is raised, prints error message and exits the program.
        Args:
            parser (argparse.ArgumentParser): The argument parser object.
            args (args: argparse.Namespace): The arguments to be checked.
        """
        try:
            self._check_filter_validity()  # This will raise the error if present
        except InvalidArgumentError as e:
            # Print only the message without traceback
            print(f"{e}")
            sys.exit()

    def help_string_output(self) -> None:
        """
        Display the help message for the pyls command-line tool.
        Args:
            parser (argparse.ArgumentParser): The argument parser object.
        """
        self.parser.print_help()
        sys.exit(0)

    def set_args(self, args: argparse.Namespace) -> None:
        """
        Set the arguments for the parser.
        Args:
            args (argparse.Namespace): The arguments to be set.
        """
        self.args = args
