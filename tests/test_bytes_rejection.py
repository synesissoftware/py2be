#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from py2be import (
    str2bool,
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)


class Bytes_rejection_tester(unittest.TestCase):

    def _assert_unclassified(self, s):

        self.assertIsNone(str2bool(s), 'str2bool(%r)' % (s,))
        self.assertFalse(string_is_falsey(s), 'string_is_falsey(%r)' % (s,))
        self.assertFalse(string_is_truey(s), 'string_is_truey(%r)' % (s,))
        self.assertFalse(string_is_truthy(s), 'string_is_truthy(%r)' % (s,))


    @unittest.skipIf(sys.version_info[0] < 3, 'bytes is text str on Python 2.7')
    def test__bytes_are_not_classified(self):

        self._assert_unclassified(b'')
        self._assert_unclassified(b'true')
        self._assert_unclassified(b'True')
        self._assert_unclassified(b'false')
        self._assert_unclassified(b'no')
        self._assert_unclassified(b'yes')
        self._assert_unclassified(b' YES ')


    @unittest.skipIf(sys.version_info[0] < 3, 'bytes is text str on Python 2.7')
    def test__bytearray_is_not_classified(self):

        self._assert_unclassified(bytearray(b''))
        self._assert_unclassified(bytearray(b'true'))
        self._assert_unclassified(bytearray(b'false'))
        self._assert_unclassified(bytearray(b' YES '))


    def test__text_inputs_remain_supported(self):

        self.assertIs(True, str2bool('true'))
        self.assertTrue(string_is_truey('true'))
        self.assertTrue(string_is_truthy('true'))

        self.assertIs(False, str2bool('no'))
        self.assertTrue(string_is_falsey('no'))
        self.assertTrue(string_is_truthy('no'))


    @unittest.skipIf(sys.version_info[0] >= 3, 'Python 2.7 byte str and unicode')
    def test__ascii_str_and_unicode_work_on_py2(self):

        self.assertIs(True, str2bool('true'))
        self.assertIs(True, str2bool(u'true'))
        self.assertIs(False, str2bool('no'))
        self.assertIs(False, str2bool(u'no'))


if '__main__' == __name__:

    unittest.main()
