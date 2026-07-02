#! /usr/bin/env python

import unittest

from py2be.constants import (
    FALSEY_PRECISE_STRINGS,
    TRUEY_PRECISE_STRINGS,
)


class Constants_tester(unittest.TestCase):

    def test__stock_precise_tables_are_sorted(self):

        self.assertEqual(
            list(FALSEY_PRECISE_STRINGS),
            sorted(FALSEY_PRECISE_STRINGS),
        )
        self.assertEqual(
            list(TRUEY_PRECISE_STRINGS),
            sorted(TRUEY_PRECISE_STRINGS),
        )


if '__main__' == __name__:

    unittest.main()
