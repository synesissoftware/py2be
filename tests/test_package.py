#! /usr/bin/env python

import unittest

import py2be


class Package_tester(unittest.TestCase):

    def test_all_names_are_defined(self):

        for name in py2be.__all__:
            self.assertTrue(hasattr(py2be, name), name)
