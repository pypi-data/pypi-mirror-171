# build a python package

This example repo:

- uses build, setuptools and pyproject.toml to build package
- uses setup.py to build package
- uses twine to upload package to PyPI package index
- uses pip or setup.py to install package

PyPI package url: https://pypi.org/project/my-pkg-binlecode/

```sh
pyenv shell 3.9.7
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip build wheel setuptools twine
```

Ref: python package doc:
https://packaging.python.org/en/latest/tutorials/packaging-projects/

Ref: setuptools doc:
https://setuptools.pypa.io/en/latest/userguide/index.html

## use native build

Build with `pyproject.toml`, with setuptools as backend.

This build and upload flow is implemented in git action [pull-request
flow](.github/workflows/pull-request.yml):

```sh
rm -rf build dist *.egg-info
python -m build
```

## upload to PyPI

First, register PyPI account if not yet.

Upload to package index PyPI using twine:

```sh
# optional: --skip-existing
python -m twine upload --skip-existing dist/*

Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: binlecode
Enter your password:
Uploading my_pkg_binlecode-0.0.3-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.0/9.0 kB • 00:00 • 3.2 MB/s
Uploading my_pkg_binlecode-0.0.3.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 kB • 00:00 • 5.7 MB/s

View at:
https://pypi.org/project/my-pkg-binlecode/0.0.3/
```

Alternatively, PyPI supports api token to replace interactive user credentials.
First, get API token from pypi.org, then assign it to env var `TWINE_USERNAME`.

```sh
TWINE_USERNAME=token TWINE_PASSWORD=pypi-XXX... python -m twine upload --skip-existing dist/*
```

Replace env var setting with $HOME/.pypirc:

```
[pypi]
  username = __token__
  password = pypi-XXX...
```

## use setuptools and setup.py

Use setup.py script to build. Distribution types should be specified.

This is implemented as git action
[publish workflow](.github/workflows/publish.yml).

#### build sdist

Build source distribution:

```sh
python setup.py sdist
```

This generates source distribution:

- dist folder that contains `<package-name>-<version>.tar.gz`
- <package-name>.egg-info folder

A source distribution contains source code.
That includes not only Python code but also the source code of any extension
modules (usually in C or C++) bundled with the package.
With source distributions, extension modules are compiled on the user’s side
rather than the developer’s.

Source distributions also contain a bundle of metadata sitting in a directory
called `<package-name>.egg-info`. Egg distribution format is being replaced
by wheel distribution format.

#### build bdist_wheel

`python setup.py bdist_wheel` generates:

- dist/<package-name>-<version>-<python>-<platform>.whl

A wheel file is essentially a zip archive with metadata of supported python
versions and platforms.

Usually both source and wheel distributions should be generated and
uploaded to package index (PyPI) for download and install.

```sh
rm -rf build dist *.egg-info
python setup.py sdist bdist_wheel
```

Upload package to PyPI (First, register PyPI account if not yet.):

```sh
python -m twine upload --skip-existing dist/*
```

## install package

`pip install <package-name>` is a general way of installing package.
pip always prefers wheel distribution over source distribution.
If wheel distribution is available for the target platform, source distribution
will be used to build package at client side.

To install from local, for example, the package project folder,
`pip install .` installs the package from current folder.

Local install is handy for development mode, where -e/--editable flag is
enabled to instruct python to track change in target package project folder:
`pip install --editable .`.

pip install on wheel skips setup.py execution, if wheel is not available,
pip has to:

- download the source distribution and extract it
- run `python setup.py install` on the extracted folder to build and install

Inside package folder, use --editable flag for development mode:
`python setup.py install --editable .`.

## about pyproject.toml

A later [PEP517](https://www.python.org/dev/peps/pep-0517/) standard defines
`pyproject.toml` as the new standard for packaging and distributing python
modules.

If there's no `pyproject.toml` available, setuptools will fall back to
`setup.py` file.

## pytest

There are two test folders, one is inside package folder, the other 
is stand-alone at project root.

To invoke pytest on in package tests, run pytest with package name, pytest 
will resolve test modules and testing functions.

Running pytest with `pytest ..` instead of `python -m pytest ..` yields nearly 
equivalent behaviour, except that the latter will add the current directory to 
`sys.path`, which is standard python behavior.

```sh
python -m pytest my_pkg
# or
pytest my_pkg
```

To invoke pytest on the root level tests folder, make sure `__init__.py`
file is in the folder to make it a package:

```sh
python -m pytest tests
# or
pytest tests
```