import argparse


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
    parser.add_argument(
        "-A",
        action="store_true",
        default=False,
        help="Get all the files, included the one starting with .",
    )

    return parser
