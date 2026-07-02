#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example: classify strings with py2be free functions.

Run from the repository root (with py2be on PYTHONPATH or installed):

    python examples/truthy_strings.py
"""

from __future__ import print_function

from py2be import (
    str2bool,
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)


def classify(label, s):

    print("%s:" % label)
    print("  input             = %r" % (s,))
    print("  str2bool()        = %r" % (str2bool(s),))
    print("  string_is_falsey  = %r" % (string_is_falsey(s),))
    print("  string_is_truey   = %r" % (string_is_truey(s),))
    print("  string_is_truthy  = %r" % (string_is_truthy(s),))
    print("")


def main():

    classify("falsey (stock)", "no")
    classify("truey (stock)", "True")
    classify("unrecognised", "orange")
    classify("whitespace-padded truey", " YES ")
    classify("none", None)


if '__main__' == __name__:

    main()
