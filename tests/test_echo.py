#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
# ^^^ this is the echo file
import subprocess


class TestEcho(unittest.TestCase):
    """this tests all the args variants of echo.py"""

    # call func, get params, test to see if passse, then pass/fail
    def test_help(self):
        """Running the program without arguments should show usage."""
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect its output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper(self):
        """checking uppered inputs because we don't want debbie downers"""
        # can check for short or long if want by using asserts, but separating helps with probs
        args = ["-u", "I'm so tIIIred"]
        # ^^^ pass into a function and get transformed; parser will get -u and
        # translate string to uppercase and send back
        # test whether parser detects the -u flag and makes ns attr of ns.upper
        parser = echo.create_parser()
        # creatparser and make obj; feed args into; parser.parseargs and see
        # if an arg is a -u, namespace.upper is true
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "I'M SO TIIIRED")
        # use python -m unittest discover to test the add-ins here

    def test_upper_long(self):
        """checking uppered inputs because we don't want debbie downers"""
        args = ["--upper", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "I'M SO TIIIRED")

    def test_lower(self):
        """checking lowered inputs because how low can you go?"""
        args = ["-l", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "i'm so tiiired")

    def test_lower_long(self):
        """checking lowered inputs because how low can you go?"""
        args = ["--lower", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEqual(result, "i'm so tiiired")

    def test_title(self):
        """checking titled inputs because titles aren't just for knights"""
        args = ["-t", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "I'M So Tiiired")

    def test_title_long(self):
        """checking titled inputs because titles aren't just for knights"""
        args = ["--title", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "I'M So Tiiired")

    def test_all(self):
        """checking all input because inclusivity is key"""
        args = ["-tul", "I'm so tIIIred"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        # print("namespace is {}".format(namespace))
        self.assertTrue(namespace.upper)
        self.assertTrue(namespace.lower)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEqual(result, "I'M So Tiiired")
        # ^^^ the order here is based on how stuff is ordered in main

    def test_none(self):
        """checking no inputs because nothing is better than something"""
        args = ["I'm so tIIIred"]
        result = echo.main(args)
        self.assertEqual(result, "I'm so tIIIred")


if __name__ == "__main__":
    unittest.main()
