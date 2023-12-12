# LatticeLeaper

A multi-dimensional maze solver.

## Description

LatticeLeaper is a maze solver, written in pure Python, with the goal of solving mazes of any size, shape, or dimensions. The end goal is to solve mazes from 2D to nD as quickly as possible.

The core may eventually be rewritten in Rust.

## Getting Started

### Dependencies

The main project has very few library dependencies, but the actual unit testing
part relies on several packages listed in
[`pyproject.toml`][pyproject.toml]. In general, you'll need:

- Python 3.10.0 or newer
- Poetry (for running unit tests)

The project is tested on the latest versions of Windows,
Mac OS, and Ubuntu, and it has also been tested on both CPython
and PyPy. Using other implementations or operating systems
may work, but is not guaranteed.

### Installation

To install the project with development dependencies,

1. Install Python 3.10.0 or newer
2. Install Poetry (`pip install poetry`)
3. Within the project directory, run `poetry install --with dev,linters,tests`
4. Either tap into the created virtual environment with `poetry shell`,
   or run all subsequent commands via `poetry run` (eg. `poetry run pytest`)

### Running unit tests

Run `poetry run pytest`. Pytest has already been configured via `pyproject.toml`,
coverage reports included.

For linting, the project uses Ruff. You can run it via `poetry run ruff .`.

## Version history

The project's changelog can be found [here][changelog].

## License

This project is licensed under the MIT license - see the [`LICENSE`][license]-file for details.

## Screenshots

![screenshot]

[pyproject.toml]: ./pyproject.toml
[changelog]: ./CHANGELOG.md
[license]: ./LICENSE
[screenshot]: ./docs/assets/example_session.png
