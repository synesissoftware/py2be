#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from py2be import (
    str2bool,
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)


class Truthy_tester(unittest.TestCase):

    def _assert_stock_truthy(self, s, truthy, truey, falsey):

        self.assertEqual(truthy, string_is_truthy(s), 'string_is_truthy(%r)' % (s,))
        self.assertEqual(truey, string_is_truey(s), 'string_is_truey(%r)' % (s,))
        self.assertEqual(falsey, string_is_falsey(s), 'string_is_falsey(%r)' % (s,))


    def test__string_is_falsey(self):

        self.assertFalse(string_is_falsey(""))
        self.assertFalse(string_is_falsey("Copyright ©"))

        self.assertTrue(string_is_falsey("0"))
        self.assertTrue(string_is_falsey("false"))
        self.assertTrue(string_is_falsey(" FALSE"))
        self.assertTrue(string_is_falsey("False"))
        self.assertTrue(string_is_falsey("FaLSe"))
        self.assertTrue(string_is_falsey("no"))
        self.assertTrue(string_is_falsey("No "))
        self.assertTrue(string_is_falsey("NO"))
        self.assertTrue(string_is_falsey(" Off "))
        self.assertTrue(string_is_falsey("off"))
        self.assertTrue(string_is_falsey("OFF"))

        self.assertFalse(string_is_falsey("1"))
        self.assertFalse(string_is_falsey("true"))
        self.assertFalse(string_is_falsey("TRUE"))
        self.assertFalse(string_is_falsey("True"))
        self.assertFalse(string_is_falsey("tRuE"))
        self.assertFalse(string_is_falsey("yes"))
        self.assertFalse(string_is_falsey(" YES"))
        self.assertFalse(string_is_falsey("Yes   "))
        self.assertFalse(string_is_falsey("yEs"))


    def test__string_is_truey(self):

        self.assertFalse(string_is_truey(""))
        self.assertFalse(string_is_truey("Copyright ©"))

        self.assertFalse(string_is_truey("0"))
        self.assertFalse(string_is_truey("false"))
        self.assertFalse(string_is_truey(" FALSE"))
        self.assertFalse(string_is_truey("False"))
        self.assertFalse(string_is_truey("FaLSe"))
        self.assertFalse(string_is_truey("no"))
        self.assertFalse(string_is_truey("No "))
        self.assertFalse(string_is_truey("NO"))
        self.assertFalse(string_is_truey(" Off "))
        self.assertFalse(string_is_truey("off"))
        self.assertFalse(string_is_truey("OFF"))

        self.assertTrue(string_is_truey("1"))
        self.assertTrue(string_is_truey("true"))
        self.assertTrue(string_is_truey("TRUE"))
        self.assertTrue(string_is_truey("True"))
        self.assertTrue(string_is_truey("tRuE"))
        self.assertTrue(string_is_truey("yes"))
        self.assertTrue(string_is_truey(" YES"))
        self.assertTrue(string_is_truey("Yes   "))
        self.assertTrue(string_is_truey("yEs"))


    def test__string_is_truthy(self):

        self.assertFalse(string_is_truthy(""))
        self.assertFalse(string_is_truthy("Copyright ©"))

        self.assertTrue(string_is_truthy("0"))
        self.assertTrue(string_is_truthy("false"))
        self.assertTrue(string_is_truthy(" FALSE"))
        self.assertTrue(string_is_truthy("False"))
        self.assertTrue(string_is_truthy("FaLSe"))
        self.assertTrue(string_is_truthy("no"))
        self.assertTrue(string_is_truthy("No "))
        self.assertTrue(string_is_truthy("NO"))
        self.assertTrue(string_is_truthy(" Off "))
        self.assertTrue(string_is_truthy("off"))
        self.assertTrue(string_is_truthy("OFF"))

        self.assertTrue(string_is_truthy("1"))
        self.assertTrue(string_is_truthy("true"))
        self.assertTrue(string_is_truthy("TRUE"))
        self.assertTrue(string_is_truthy("True"))
        self.assertTrue(string_is_truthy("tRuE"))
        self.assertTrue(string_is_truthy("yes"))
        self.assertTrue(string_is_truthy(" YES"))
        self.assertTrue(string_is_truthy("Yes   "))
        self.assertTrue(string_is_truthy("yEs"))


    def test__str2bool(self):

        self.assertIsNone(str2bool(None))
        self.assertIsNone(str2bool(""))
        self.assertIsNone(str2bool("orange"))
        self.assertIsNone(str2bool("Nyet"))

        self.assertIs(False, str2bool("0"))
        self.assertIs(False, str2bool("false"))
        self.assertIs(False, str2bool("no"))
        self.assertIs(False, str2bool("off"))

        self.assertIs(True, str2bool("1"))
        self.assertIs(True, str2bool("true"))
        self.assertIs(True, str2bool("yes"))
        self.assertIs(True, str2bool("on"))


    def test__whitespace_padded(self):

        self._assert_stock_truthy(" true", True, True, False)
        self._assert_stock_truthy(" TRUE", True, True, False)
        self._assert_stock_truthy(" True", True, True, False)
        self._assert_stock_truthy(" false", True, False, True)
        self._assert_stock_truthy(" FALSE", True, False, True)
        self._assert_stock_truthy(" False", True, False, True)
        self._assert_stock_truthy(" yes", True, True, False)
        self._assert_stock_truthy(" YES", True, True, False)
        self._assert_stock_truthy(" Yes", True, True, False)
        self._assert_stock_truthy(" no", True, False, True)
        self._assert_stock_truthy(" NO", True, False, True)
        self._assert_stock_truthy(" No", True, False, True)
        self._assert_stock_truthy(" on", True, True, False)
        self._assert_stock_truthy(" ON", True, True, False)
        self._assert_stock_truthy(" On", True, True, False)
        self._assert_stock_truthy(" off", True, False, True)
        self._assert_stock_truthy(" OFF", True, False, True)
        self._assert_stock_truthy(" Off", True, False, True)
        self._assert_stock_truthy(" 1", True, True, False)
        self._assert_stock_truthy(" 0", True, False, True)

        self._assert_stock_truthy("true ", True, True, False)
        self._assert_stock_truthy("TRUE ", True, True, False)
        self._assert_stock_truthy("True ", True, True, False)
        self._assert_stock_truthy("false ", True, False, True)
        self._assert_stock_truthy("FALSE ", True, False, True)
        self._assert_stock_truthy("False ", True, False, True)
        self._assert_stock_truthy("yes ", True, True, False)
        self._assert_stock_truthy("YES ", True, True, False)
        self._assert_stock_truthy("Yes ", True, True, False)
        self._assert_stock_truthy("no ", True, False, True)
        self._assert_stock_truthy("NO ", True, False, True)
        self._assert_stock_truthy("No ", True, False, True)
        self._assert_stock_truthy("on ", True, True, False)
        self._assert_stock_truthy("ON ", True, True, False)
        self._assert_stock_truthy("On ", True, True, False)
        self._assert_stock_truthy("off ", True, False, True)
        self._assert_stock_truthy("OFF ", True, False, True)
        self._assert_stock_truthy("Off ", True, False, True)
        self._assert_stock_truthy("1 ", True, True, False)
        self._assert_stock_truthy("0 ", True, False, True)

        self._assert_stock_truthy(" true ", True, True, False)
        self._assert_stock_truthy(" TRUE ", True, True, False)
        self._assert_stock_truthy(" True ", True, True, False)
        self._assert_stock_truthy(" false ", True, False, True)
        self._assert_stock_truthy(" FALSE ", True, False, True)
        self._assert_stock_truthy(" False ", True, False, True)
        self._assert_stock_truthy(" yes ", True, True, False)
        self._assert_stock_truthy(" YES ", True, True, False)
        self._assert_stock_truthy(" Yes ", True, True, False)
        self._assert_stock_truthy(" no ", True, False, True)
        self._assert_stock_truthy(" NO ", True, False, True)
        self._assert_stock_truthy(" No ", True, False, True)
        self._assert_stock_truthy(" on ", True, True, False)
        self._assert_stock_truthy(" ON ", True, True, False)
        self._assert_stock_truthy(" On ", True, True, False)
        self._assert_stock_truthy(" off ", True, False, True)
        self._assert_stock_truthy(" OFF ", True, False, True)
        self._assert_stock_truthy(" Off ", True, False, True)
        self._assert_stock_truthy(" 1 ", True, True, False)
        self._assert_stock_truthy(" 0 ", True, False, True)

        self._assert_stock_truthy("\ttrue\t", True, True, False)
        self._assert_stock_truthy("\tFALSE\t", True, False, True)
        self._assert_stock_truthy("\t yes \t", True, True, False)

        self._assert_stock_truthy(" tRuE ", True, True, False)
        self._assert_stock_truthy(" FaLSe ", True, False, True)
        self._assert_stock_truthy(" yEs ", True, True, False)

        self._assert_stock_truthy(" unrecognised ", False, False, False)
        self._assert_stock_truthy("   ", False, False, False)
        self._assert_stock_truthy("\t", False, False, False)


if '__main__' == __name__:

    unittest.main()
