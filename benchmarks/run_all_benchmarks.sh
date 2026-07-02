#! /bin/bash

set -e

cd "$(dirname "$0")/.."

export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}$(pwd)"

python benchmarks/string_truthy.py "$@"
