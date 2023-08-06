# Overview

A wrapper around flake8's cli that caches results between runs at file level.

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/com/jnoortheen/flake8-cached.svg?label=unix)](https://travis-ci.com/jnoortheen/flake8-cached)
[![Windows Build Status](https://img.shields.io/appveyor/ci/jnoortheen/flake8-cached.svg?label=windows)](https://ci.appveyor.com/project/jnoortheen/flake8-cached)
[![Coverage Status](https://img.shields.io/coveralls/jnoortheen/flake8-cached.svg)](https://coveralls.io/r/jnoortheen/flake8-cached)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jnoortheen/flake8-cached.svg)](https://scrutinizer-ci.com/g/jnoortheen/flake8-cached)
[![PyPI Version](https://img.shields.io/pypi/v/flake8-cached.svg)](https://pypi.org/project/flake8-cached)
[![PyPI License](https://img.shields.io/pypi/l/flake8-cached.svg)](https://pypi.org/project/flake8-cached)

# Setup

## Requirements

* Python 3.6+

## Installation

Install it directly into an activated virtual environment:

```text
$ pip install flake8-cached
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add flake8-cached
```

# Usage

After installation, the package can imported:

```shell
# it accepts all arguments as flake8
$ flake8-cached .
```

# Note

It creates cache files under `.cache/flake8` under the project directory. 
It is not cleaned up even if there is some config or python binary changes. 
Please remove the folder and re-run if you get stale results.
It is a simple cache implementation intended to be used during development.
