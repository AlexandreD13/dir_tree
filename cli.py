"""
Author:         Alexandre Desfosses
Creation date:  2023-03-30
Documentation:
References:
"""

from dir_tree.main import print_directory_tree

import argparse
import os


def cli(argv=None):
    """

    :return:
    """
    parser = argparse.ArgumentParser(prog="Dir_tree",
                                     description="")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="More information displayed")

    # parser.add_argument("-b", "--argumentB", required=False, type=str, nargs=1,
    #                     help="The name of the argument B")

    # parser.add_argument("-c", "--argumentC", required=False, type=str, nargs=1,
    #                     default=["something"], help="The name of the argument C")

    args = parser.parse_args(argv)

    # Add your logic here to call methods and do stuff based on the inputs.
    # To use the arguments,
    #       args.argumentA[0], args.argumentB[0], etc...

    print()
    print_directory_tree()
