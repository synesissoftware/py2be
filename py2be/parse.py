
import sys
from collections import namedtuple

from .constants import (
    FALSEY_LOWERCASE_STRINGS,
    FALSEY_PRECISE_STRINGS,
    TRUEY_LOWERCASE_STRINGS,
    TRUEY_PRECISE_STRINGS,
)

if sys.version_info[0] < 3:
    _text_type = basestring  # noqa: F821
else:
    _text_type = str


# Stock vocabulary: eight canonical spellings (Title-case words,
# single-char digits).
# Source of truth for str2bool() / string_is_truthy(); constants.py
# tuples remain for the one-sided paths below until a later elision pass.
_TRUTHY_STRINGS = {
    "0": False,
    "1": True,
    "False": False,
    "True": True,
    "No": False,
    "Yes": True,
    "Off": False,
    "On": True,
}

_TRUTHY_RECORD = namedtuple('_TruthyRecord', ('length', 'strings', 'truth'))


def _make_strings_tuple(canonical):
    # Precomputed accept variants per canonical key: 1-tuple for digits;
    # 2-tuple for all-lower / all-upper keys; 3-tuple (title, UPPER,
    # lower) for Title-case keys such as "True". Mixed-case input is
    # handled in _record_matches() via comparison to the lower-case
    # element.

    if canonical.upper() == canonical:

        if canonical.upper() == canonical.lower():

            return (canonical, )

    if canonical.isupper():

        return (canonical, canonical.lower())

    if canonical.islower():

        return (canonical.upper(), canonical)

    return (canonical, canonical.upper(), canonical.lower())


def _build_truthy_table(truthy_strings):
    # Key (length, first_char) gives O(1) lookup and disambiguates stock
    # collisions on the same letter (e.g. "On" vs "Off"). Register both
    # casings of the first character so lookup needs no normalisation
    # step.

    table = {}

    for canonical, truth in truthy_strings.items():

        record = _TRUTHY_RECORD(
            len(canonical),
            _make_strings_tuple(canonical),
            truth,
        )
        length = len(canonical)
        first = canonical[0]

        for letter in (first, first.swapcase()):

            table[(length, letter)] = record

    return table


_TRUTHY_TABLE = _build_truthy_table(_TRUTHY_STRINGS)


def _record_matches(s, record):
    # Try exact variant hit first; for 2/3-tuples fall back to lower-case
    # equality so inputs like "tRuE" match without an extra table entry.

    strings = record.strings

    if s in strings:

        return True

    if len(strings) >= 2 and s.lower() == strings[-1]:

        return True

    return False


def _str2bool(s):
    # Full classification path used by str2bool() and string_is_truthy().
    # Always strips first so padded and unpadded inputs share one code
    # path (benchmarks: faster padded stock matches and misses vs the
    # legacy precise-tuple tables; unpadded exact hits are slower — see
    # README). Caller must ensure s is text; public entry points guard
    # isinstance.

    s = s.strip()

    if not s:

        return None

    length = len(s)
    record = _TRUTHY_TABLE.get((length, s[0]))
    if not record:

        return None

    if _record_matches(s, record):

        return record.truth

    return None


def _str_is_falsey(s):
    # One-sided path: opposite-precise bail-out then lowercase falsey
    # table. Faster than routing through _str2bool() when the question
    # is polarity only (benchmarks ~2x on matching stock falsey terms).
    # Caller must ensure s is text.

    if s in FALSEY_PRECISE_STRINGS:

        return True

    if s in TRUEY_PRECISE_STRINGS:

        return False

    s = s.strip().lower()

    if s in FALSEY_LOWERCASE_STRINGS:

        return True

    return False


def _str_is_truey(s):
    # One-sided path: mirror of _str_is_falsey() for truey polarity.

    if s in TRUEY_PRECISE_STRINGS:

        return True

    if s in FALSEY_PRECISE_STRINGS:

        return False

    s = s.strip().lower()

    if s in TRUEY_LOWERCASE_STRINGS:

        return True

    return False


def str2bool(s):
    """Classify ``s`` as truey, falsey, or unrecognised.

    Returns ``True`` or ``False`` when ``s`` matches a recognised stock
    term after stripping leading and trailing whitespace. Returns
    ``None`` for unrecognised strings and for non-text ``s`` (for
    example ``bytes`` on Python 3).
    """

    if not isinstance(s, _text_type):

        return None

    return _str2bool(s)


def string_is_falsey(s):
    """Indicate whether ``s`` is a recognised stock falsey term.

    Returns ``True`` when ``s`` is classified as truthy and deemed
    falsey. Returns ``False`` for truey terms, unrecognised strings,
    and non-text ``s``.
    """

    if not isinstance(s, _text_type):

        return False

    return _str_is_falsey(s)


def string_is_truey(s):
    """Indicate whether ``s`` is a recognised stock truey term.

    Returns ``True`` when ``s`` is classified as truthy and deemed
    truey. Returns ``False`` for falsey terms, unrecognised strings,
    and non-text ``s``.
    """

    if not isinstance(s, _text_type):

        return False

    return _str_is_truey(s)


def string_is_truthy(s):
    """Indicate whether ``s`` is a recognised stock truthy term.

    Returns ``True`` for any recognised stock term, whether deemed
    falsey or truey. Returns ``False`` for unrecognised strings and
    for non-text ``s``.
    """

    if not isinstance(s, _text_type):

        return False

    return _str2bool(s) is not None
