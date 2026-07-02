# py2be - TODO <!-- omit in toc -->


## Table of Contents <!-- omit in toc -->

- [Project improvements](#project-improvements)
- [Functional improvements](#functional-improvements)
- [Performance improvements](#performance-improvements)


## Project improvements

* [x] **build_dist.sh** and **build_dist_uv.sh** (build + `twine check`);
* [x] **MANIFEST.in**;
* [x] `python_requires` (Python 2.7 and Python 3.8+);
* [x] Python 2.7 test infrastructure (`tests/__init__.py`, `tests/run_unittest.py`, `tests/test_package.py`);
* [x] expanded unit tests and GitHub Actions (Python 2.7, pytest, Python 3.14);
* [x] README polish (installation, compatibility table, API reference);
* [x] README: explicit Python 2.7 claim; `unicode` / `bytes` policy;
* [x] **EXAMPLES.md** and **examples/truthy_strings.py**;
* [x] **tests/test_bytes_rejection.py** (documented `unicode` / `bytes` policy);


## Functional improvements

* [ ] `Terms`, `string_is_truthy_with()`, and `stock_term_strings()` (cf. **to-be.Rust**);


## Performance improvements

* [x] **benchmarks/string_truthy.py** and **benchmarks/run_all_benchmarks.sh**;
* [x] one-sided `string_is_falsey()` / `string_is_truey()` paths with opposite-precise fast-fail (cf. **to-be.Rust**);
* [-] ~~~conditional-trim fast path (cf. **to-be.Rust**; measured regression on CPython for stock terms)~~~;
* [-] ~~~`bisect` precise-table lookup (cf. **to-be.Rust**; measured regression at current stock table sizes)~~~;


<!-- ########################### end of file ########################### -->

