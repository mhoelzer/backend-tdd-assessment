#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the "echo" cmd line utility"""

__author__ = "mhoelzer"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="change text based on command line input/option")
    # parser.add_argument("-h", "--help", help="show this help message and exit")
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    print("main args are {}".format(args))
    parser = create_parser()
    # if not arguments
    if not args:
        # ^^^ aka if len(sys.argv) <= 1
        parser.print_usage()
        sys.exit(1)
    namespace = parser.parse_args(args)
    output_text = namespace.text
    # do the bussiness logic of echo.py; transform
    if namespace.upper:
        output_text = output_text.upper()
    if namespace.lower:
        output_text = output_text.lower()
    if namespace.title:
        output_text = output_text.title()
    return output_text


if __name__ == "__main__":
    # example of cmdl: python echo.py --upper "Michael was Here"
    print("original sys.argv is {}".format(sys.argv))
    print(main(sys.argv[1:]))
    # ^^^ get everything after the file name
    # ^^^ reference a slice of a list, so to get another list of just the
    # user-supplied arguments (but without the script name)
    # ^^^ first arg after python is the echo.py but dont give main func the
    # echo.py and main wants the last 2 args