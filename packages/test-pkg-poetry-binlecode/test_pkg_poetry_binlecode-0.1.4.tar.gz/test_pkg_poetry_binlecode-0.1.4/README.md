# test package build with poetry

Comparing to setuptools, poetry is all-in-one shop and with less manual
configuration in python package development cycle.
For example, `pyproject.toml` is created by poetry with format of PEP 518
package specs with `poetry new` command.

```sh
pyenv shell 3.9.11
python -m venv ./venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install poetry
```

## package initialization

Use poetry to initialzes a package under project root:

```sh
poetry new test_pkg_poetry_binlecode
```

Use poetry to add dependencies, they are added to pyproject.toml by poetry
automatically.

```sh
# add pytest as dev dependency
poetry add pytest --dev
# show dependency tree
poetry show --tree
# generate lock file
poetry lock

# The install command reads the pyproject.toml file from the current project,
# resolves the dependencies, and installs them.
# If poetry.lock exists, the lock file is used instead of resolving dependencies.
poetry install

poetry export --output requirements.txt
```

## testing with pytest

Run pytest at project root level, it will scan tests folder and test scripts.

```sh
poetry run pytest
```

## source code formatting with black

```sh
poetry run black .
```

## build distribution and publish

Check package and build distribution. Poetry builds both source and wheel
distributions.

```sh
poetry check
poetry build
```

To publish to pypi, config api token first.

```sh
poetry config pypi-token.pypi <my-token>
```

Poetry can use token to publish:

```sh
poetry publish

Publishing test-pkg-poetry-binlecode (0.1.0) to PyPI
 - Uploading test-pkg-poetry-binlecode-0.1.0.tar.gz 100%
 - Uploading test_pkg_poetry_binlecode-0.1.0-py3-none-any.whl 100%
```

## github cicd workflows

Black (PEP8) lint check is triggered on all push and pull requests.

Pull-request driven tests cover python 3.8, 3.9 on multiple platforms.

Release candidate is built with python 3.9 on ubuntu-latest platform.

