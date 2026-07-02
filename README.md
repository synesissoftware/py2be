# py2be <!-- omit in toc -->

![Language](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version](https://badge.fury.io/py/py2be.svg)](https://badge.fury.io/py/py2be)
[![GitHub release](https://img.shields.io/github/v/release/synesissoftware/py2be.svg)](https://github.com/synesissoftware/py2be/releases/latest)
![Python](https://img.shields.io/badge/Python-2.7%20%7C%203.8+-lightgrey)
[![CI](https://github.com/synesissoftware/py2be/actions/workflows/python-package.yml/badge.svg)](https://github.com/synesissoftware/py2be/actions/workflows/python-package.yml)
[![Last Commit](https://img.shields.io/github/last-commit/synesissoftware/py2be)](https://github.com/synesissoftware/py2be/commits/master)

Simple Python library determining whether strings indicate *truey* or *falsey* values.


## Table of Contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Installation \& usage](#installation--usage)
  - [Python version compatibility](#python-version-compatibility)
  - [Text string inputs (`unicode` / `bytes`)](#text-string-inputs-unicode--bytes)
- [Terminology](#terminology)
- [Components](#components)
  - [Functions](#functions)
- [Project Information](#project-information)
  - [Where to get help](#where-to-get-help)
  - [Contribution guidelines](#contribution-guidelines)
  - [Dependencies](#dependencies)
    - [Dev Dependencies](#dev-dependencies)
  - [Related projects](#related-projects)
  - [License](#license)


## Introduction

**to-be** is a library providing facilities for determining whether the truthyness of strings. It is implemented in several languages: **py2be** is the **Python** implementation.

**py2be** explicitly supports **Python 2.7** — not other Python 2.x releases — and **Python 3.8+**. This is enforced at install time via `python_requires` in **setup.py** and exercised in GitHub Actions on **Python 2.7** and **Python 3.8–3.14**.


## Installation & usage

Install via **pip** or **pip3**, as in:

```
$ pip3 install py2be
```

Use via **import**:

```Python
import py2be
```

or import the functions you need:

```Python
from py2be import (
    str2bool,
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)
```


### Python version compatibility

**py2be** is intended to run on **Python 2.7** and **Python 3.8+** only. Versions in the Python 3.0–3.7 range are excluded by `python_requires`.

| Python version | Support |
| -------------- | ------- |
| **2.7** | Supported (the only Python 2 release supported) |
| **3.0 – 3.7** | Not supported |
| **3.8+** | Supported |

| Requirement | Applies to |
| ----------- | ---------- |
| Python **2.7** or **3.8+** | All public APIs (`str2bool`, `string_is_falsey`, `string_is_truey`, `string_is_truthy`) |

The public API surface is listed in `py2be.__all__`.


### Text string inputs (`unicode` / `bytes`)

All public functions take a single string argument `s`. The library classifies **text** only; binary buffers are not accepted.

| Input | Python 2.7 | Python 3.8+ |
| ----- | ------------ | ----------- |
| `unicode` / text `str` | Supported | Supported (`str`) |
| `str` (byte string) | Supported for ASCII stock terms (e.g. `"true"`, `"no"`) | N/A — `str` is text |
| `bytes`, `bytearray`, and other non-text types | Not supported — behaviour is undefined; decode to text first | Not supported — behaviour is undefined; decode to text first |
| `None` | `str2bool(None)` returns `None`; the boolean predicates return `False` | Same |

On **Python 3**, passing `bytes` (for example `b"true"`) will not match stock terms and is not a supported use case. Decode explicitly before calling, for example `s.decode("utf-8")` or `s.decode("ascii")`.

On **Python 2.7**, prefer `unicode` literals (e.g. `u"true"`) for non-ASCII configuration values. ASCII `str` literals work for the stock vocabulary because they match the internal comparison tables directly.

Trimming uses `str.strip()` / `unicode.strip()`; only leading and trailing whitespace is removed before lower-case matching.


## Terminology

The term "*truthy*" is an unhelpfully overloaded term in the programming world, insofar as it is used to refer to the notion of "truthyness" - whether something can be _deemed to be_ interpretable as truth - and also the true side of that interpretation. In this library, the former interpretation is used, leaving us with the following terms:

* "*truthy*" - whether something can be _deemed to be_ interpretable as having truth (and, thus, will be *falsey* or *truey*);
* "*falsey*" - whether an object can be _deemed to be_ interpretable as being false;
* "*truey*" - whether an object can be _deemed to be_ interpretable as being true;

For example, consider the following **Python** program:

```Python
from py2be import (
    string_is_falsey,
    string_is_truey,
    string_is_truthy,
)

s1 = "no"
s2 = "True"
s3 = "orange"

# "no" is validly truthy, and is falsey
assert string_is_falsey(s1)
assert not string_is_truey(s1)
assert string_is_truthy(s1)

# "True" is validly truthy, and is truey
assert not string_is_falsey(s2)
assert string_is_truey(s2)
assert string_is_truthy(s2)

# "orange" is not validly truthy, and is neither falsey nor truey
assert not string_is_falsey(s3)
assert not string_is_truey(s3)
assert not string_is_truthy(s3)
```


## Components

### Functions

The following public functions are defined in the current version:

| Function | Purpose |
| -------- | ------- |
| `str2bool(s)` | Classifies `s` as unrecognised (`None`), falsey (`False`), or truey (`True`). |
| `string_is_falsey(s)` | Indicates that `s`, when trimmed, is classified as truthy and is deemed falsey. |
| `string_is_truey(s)` | Indicates that `s`, when trimmed, is classified as truthy and is deemed truey. |
| `string_is_truthy(s)` | Indicates that `s`, when trimmed, is classified as truthy (and is deemed either falsey or truey). |

**NOTE:** `string_is_falsey(x) == not string_is_truey(x)` is **not** guaranteed (for example, when `x` is not classified as truthy, both predicates return `False`).

Stock falsey terms (after optional trimming and case folding) include `0`, `false`, `no`, and `off`. Stock truey terms include `1`, `true`, `yes`, and `on`. Several common capitalisations and mixtures of case are recognised without lower-casing first.


## Project Information

### Where to get help

[GitHub Page](https://github.com/synesissoftware/py2be "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/py2be.


### Dependencies

**py2be** has no (non-development) dependencies.


#### Dev Dependencies

**py2be** has no (additional) development dependencies.


### Related projects

* [**2be**](https://github.com/synesissoftware/2be) (**C**);
* [**to_be.Ruby**](https://github.com/synesissoftware/to_be.Ruby);
* [**to-be.Rust**](https://github.com/synesissoftware/to-be.Rust);


### License

**py2be** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->
