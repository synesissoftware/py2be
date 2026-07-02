# **py2be** Changes


## 0.1.0 - 2nd July 2026

* modularised implementation (`constants`, `parse`, `truthy`);
* added **benchmarks/string_truthy.py** and **benchmarks/run_all_benchmarks.sh**;
* `str2bool()` and `string_is_truthy()` now classify stock terms via `_TRUTHY_STRINGS` and a module-built `_TRUTHY_TABLE` keyed by `(length, first_char)` (cf. **to-be.Rust** first-letter dispatch); always strips before lookup; strong on padded stock terms and unrecognised inputs (benchmarked);
* retained one-sided `string_is_falsey()` and `string_is_truey()` paths (`_str_is_falsey`, `_str_is_truey`) with opposite-precise fast-fail and conditional `strip().lower()` (cf. **to-be.Rust**); `constants.py` precise/lowercase tuples remain for these paths until a later elision pass;
* added docstrings to `str2bool()`, `string_is_falsey()`, `string_is_truey()`, and `string_is_truthy()`;
* measured and ruled out for stock vocabulary at current table sizes: merged precise-table linear scan, `bisect` lookup, state-machine parsers, and conditional-trim fast paths (see **README** benchmarks section);

## 0.0.4 - 2nd July 2026

* added top-level `__all__` documenting the public API;
* removed `tests` and `examples` from installable packages;
* added `python_requires` for Python 2.7 and Python 3.8+;
* added **MANIFEST.in**;
* aligned **build_dist.sh** with **build_dist_uv.sh** (system Python);
* added **build_dist_uv.sh** (build + `twine check`);
* added **tests/test_package.py**;
* added **tests/run_unittest.py** and Python 2.7 compatibility shims in **tests/__init__.py**;
* expanded unit tests (`str2bool`, whitespace-padded stock terms);
* extended GitHub Actions workflow (Python 2.7 job, Python 3.14, pytest);
* fix project URL;
* README polish (installation, Python version compatibility, Components/API reference, CI badges, examples, URL(s));
* fixed pytest import failure (removed repo-root `__init__.py`; `pip install -e .` in CI; **pytest.ini**);
* README: explicit Python 2.7 compatibility claim; documented `unicode` / `bytes` input policy;
* added **examples/truthy_strings.py** and **EXAMPLES.md**;
* added `Programming Language :: Python :: 3.14` classifier;
* added **tests/test_bytes_rejection.py** (bytes / `bytearray` not classified on Python 3; Py2.7 text inputs);


## 0.0.3 - 1st September 2025

* GitHub Actions;
* badges;
* .gitattributes;


## 0.0.2 - 11th August 2025

* name fixes;


## 0.0.1 - 11th August 2025

* initial version;



<!-- ########################### end of file ########################### -->

