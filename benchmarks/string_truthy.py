#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Benchmark string truthy evaluation (stock terms).

Run from the repository root with py2be installed or on PYTHONPATH:

    python benchmarks/string_truthy.py

Filter benchmark groups:

    python benchmarks/string_truthy.py string_is_truthy
    python benchmarks/string_truthy.py mixed_batch
"""

from __future__ import print_function

import sys
import timeit

from py2be import (
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)


INPUTS = (
    ('true', 'lower'),
    ('TRUE', 'upper'),
    ('True', 'title'),
    ('false', 'lower'),
    ('FALSE', 'upper'),
    ('False', 'title'),
    ('yes', 'lower'),
    ('YES', 'upper'),
    ('Yes', 'title'),
    ('no', 'lower'),
    ('NO', 'upper'),
    ('No', 'title'),
    ('on', 'lower'),
    ('ON', 'upper'),
    ('On', 'title'),
    ('off', 'lower'),
    ('OFF', 'upper'),
    ('Off', 'title'),
    ('1', ''),
    ('0', ''),
    ('unrecognised', 'unrecognised'),
)


PADDED_INPUTS = (
    (' true', 'leading/lower/true'),
    ('true ', 'trailing/lower/true'),
    (' true ', 'both/lower/true'),
    (' FALSE', 'leading/upper/FALSE'),
    ('false ', 'trailing/lower/false'),
    (' YES ', 'both/upper/YES'),
    (' 1', 'leading/1'),
    ('0 ', 'trailing/0'),
    (' unrecognised ', 'both/unrecognised'),
)


MIXED_INPUTS = (
    'yes',
    'no',
    'TRUE',
    'off',
    'maybe',
    '1',
    '0',
    '',
)

MIXED_PADDED_INPUTS = (
    ' yes ',
    ' no ',
    ' TRUE ',
    ' off ',
    ' maybe ',
    ' 1 ',
    ' 0 ',
    '   ',
)


NUMBER = 200000
REPEAT = 5


def _bench_name(label, input_value):

    if label:
        return '%s/%s' % (label, input_value)
    return input_value


def _run_bench(name, fn, arg):

    elapsed = min(timeit.repeat(lambda: fn(arg), repeat=REPEAT, number=NUMBER))
    per_op_ns = (elapsed / float(NUMBER)) * 1e9

    print('%-48s %8.1f ns/op' % (name, per_op_ns))


def _run_mixed(name, fn, inputs):

    def batch():

        for s in inputs:
            fn(s)

    elapsed = min(timeit.repeat(batch, repeat=REPEAT, number=NUMBER))
    per_op_ns = (elapsed / float(NUMBER)) * 1e9

    print('%-48s %8.1f ns/op' % (name, per_op_ns))


def bench_group(group_name, inputs, classify):

    print('[%s]' % group_name)

    for input_value, label in inputs:
        name = '%s/%s' % (group_name, _bench_name(label, input_value))
        _run_bench(name, classify, input_value)

    print('')


def bench_mixed(group_name, inputs, classify):

    print('[%s]' % group_name)
    _run_mixed('%s/mixed_batch' % group_name, classify, inputs)
    print('')


def main(argv):

    groups = {
        'string_is_truthy': (
            lambda: bench_group('string_is_truthy', INPUTS, string_is_truthy),
            lambda: bench_group('string_is_truthy_padded', PADDED_INPUTS, string_is_truthy),
            lambda: bench_mixed('string_is_truthy', MIXED_INPUTS, string_is_truthy),
            lambda: bench_mixed('string_is_truthy_padded', MIXED_PADDED_INPUTS, string_is_truthy),
        ),
        'string_is_truey': (
            lambda: bench_group('string_is_truey', INPUTS, string_is_truey),
            lambda: bench_group('string_is_truey_padded', PADDED_INPUTS, string_is_truey),
        ),
        'string_is_falsey': (
            lambda: bench_group('string_is_falsey', INPUTS, string_is_falsey),
            lambda: bench_group('string_is_falsey_padded', PADDED_INPUTS, string_is_falsey),
        ),
        'mixed_batch': (
            lambda: bench_mixed('string_is_truthy', MIXED_INPUTS, string_is_truthy),
            lambda: bench_mixed('string_is_truthy_padded', MIXED_PADDED_INPUTS, string_is_truthy),
        ),
    }

    selected = argv[1:]

    if not selected:
        selected = [
            'string_is_truthy',
            'string_is_truey',
            'string_is_falsey',
            'mixed_batch',
        ]

    print('py2be string truthy benchmarks (number=%d, repeat=%d)' % (NUMBER, REPEAT))
    print('')

    for key in selected:
        if key not in groups:
            print('Unknown group: %s' % key, file=sys.stderr)
            return 1

        for run in groups[key]:
            run()

    return 0


if '__main__' == __name__:

    sys.exit(main(sys.argv))
