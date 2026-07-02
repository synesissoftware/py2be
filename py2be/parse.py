
import sys

from .constants import (
    FALSEY_LOWERCASE_STRINGS,
    FALSEY_PRECISE_STRINGS,
    TRUEY_LOWERCASE_STRINGS,
    TRUEY_PRECISE_STRINGS,
)

if sys.version_info[0] < 3:
    _text_type = basestring
else:
    _text_type = str


def _str2bool(s):

    if not isinstance(s, _text_type):

        return None

    if s in FALSEY_PRECISE_STRINGS:

        return False

    if s in TRUEY_PRECISE_STRINGS:

        return True

    s = s.strip().lower()

    if s in TRUEY_LOWERCASE_STRINGS:

        return True

    if s in FALSEY_LOWERCASE_STRINGS:

        return False

    return None


def str2bool(s):

    return _str2bool(s)


def string_is_falsey(s):

    return _str2bool(s) == False


def string_is_truey(s):

    return _str2bool(s) == True


def string_is_truthy(s):

    return _str2bool(s) is not None
