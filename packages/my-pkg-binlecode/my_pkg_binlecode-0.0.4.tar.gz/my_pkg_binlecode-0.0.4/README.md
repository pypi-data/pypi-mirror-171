# build a python package

This example repo:

- uses build, setuptools and pyproject.toml to build package
- uses setup.py to build package
- uses twine to upload package
- uses pip or setup.py to install package

```sh
pyenv shell 3.9.7
python -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip build wheel setuptools twine
```

## use build

Ref: https://packaging.python.org/en/latest/tutorials/packaging-projects/

build with pyproject.toml

```sh
rm -rf build dist *.egg-info
python -m build
```

upload to package index PyPI (First, register PyPI account if not yet.):

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

Alternatively, can use api token to replace interactive user credentials input.
First, get API token from pypi.org, then assign it to env var `TWINE_USERNAME`.

```sh
TWINE_USERNAME=<TOKEN> python -m twine upload --skip-existing dist/*
```

## use setuptools and setup.py

Ref: setuptools guide:
https://setuptools.pypa.io/en/latest/userguide/index.html

`python setup sdist` generates source distribution:

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

## bdist and bdist_wheel

`bdist` means build distribution, which is not necessarily binary.

`python setup.py bdist` generates:

- dist/<package-name>-<version>.<platform>.tar.gz, which is the default
  type of built distribution for the current platform
- build/bdist.<platform>
- build/lib folder that includes modules

`python setup.py bdist_wheel` generates:

- dist/<package-name>-<version>-<python>-<platform>.whl

A wheel file is essentially a zip archive with metadata of supported python
versions and platforms.

Usually both source and wheel build distributions should be generated and
uploaded to package index for download and install.

```sh
rm -rf build dist *.egg-info
python setup.py sdist bdist_wheel
```

upload package to PyPI (First, register PyPI account if not yet.):

```sh
twine upload dist/*
```

## install

`pip install <package-name>` is a general way of installing package.
pip always prefers wheel distribution over source distribution.
If wheel distribution is available for the target platform, source distribution
will be used to build package at client side.

pip install on wheel skips setup.py execution, which is described below.

Inside package folder, use
`python setup.py install` to install the distribution package.

A inline editable install is for development mode:
`python setup.py install --editable .` will install with the source content
that is editable, which is great for debuging and testing changes.

## pyproject.toml

A later [PEP517](https://www.python.org/dev/peps/pep-0517/) standard defines
`pyproject.toml` as the new standard for packaging and distributing python
modules.

If there's no `pyproject.toml` available, setuptools will fall back to
`setup.py` file.
