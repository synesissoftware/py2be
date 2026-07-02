
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


def _str_is_falsey(s):

    if not isinstance(s, _text_type):

        return False

    if s in FALSEY_PRECISE_STRINGS:

        return True

    if s in TRUEY_PRECISE_STRINGS:

        return False

    s = s.strip().lower()

    if s in FALSEY_LOWERCASE_STRINGS:

        return True

    return False


def _str_is_truey(s):

    if not isinstance(s, _text_type):

        return False

    if s in TRUEY_PRECISE_STRINGS:

        return True

    if s in FALSEY_PRECISE_STRINGS:

        return False

    s = s.strip().lower()

    if s in TRUEY_LOWERCASE_STRINGS:

        return True

    return False


def str2bool(s):

    return _str2bool(s)


def string_is_falsey(s):

    return _str_is_falsey(s)


def string_is_truey(s):

    return _str_is_truey(s)


def string_is_truthy(s):

    return _str2bool(s) is not None
