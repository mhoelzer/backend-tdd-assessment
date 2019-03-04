#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
# ^^^ this is the echo file
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    # ^^^ we get helpful asserts from ut
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

    # def test_upper(self):
    #     process = subprocess.Popen(
    #         ["python", "./echo.py", "-u"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     # self.assertEquals(stdout, stdout)
    #     self.assertTrue(stdout.upper())
    #     # creatparser and make obj; feed args into; parser.parseargs and see
    #     # if an arg is a -u, namespace.upper is true
    
    # test the -u option 
    def test_upper_short(self):
        args = ["-u" or "--upp"]
        # ^^^ pass into a funciton and get transformed; parser will get -u and
        # translate string to uppercase and send back
        # test whether parser detects the -u flag and makes ns attr of ns.upper
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        print("namespace is {}".format(namespace))
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEqual(result, "MICHAEL WAS HERE")

    # def test_upper_long(self):
    #     args = ["--upper", "Michael ewas here"]
    #     parser = echo.create_parser()
    #     namespace = parser.parse_args(args)
    #     print("namespace is {}".format(namespace))
    #     self.assertTrue(namespace.upper)
    #     result = echo.main(args)
    #     self.assertEqual(result, "MICHAEL WAS HERE")
        # use python -m unittest discover to test the add-ins here

    def test_lower(self):
        pass

    def test_title(self):
        pass


if __name__ == "__main__":
    unittest.main()
