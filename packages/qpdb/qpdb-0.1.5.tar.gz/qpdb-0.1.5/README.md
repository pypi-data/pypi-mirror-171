# qu ⠶ pd

[![CI Status](https://github.com/qu-arx/qp/actions/workflows/master.yml/badge.svg)](https://github.com/qu-arx/qp/actions/workflows/master.yml)
[![Coverage](https://codecov.io/gh/qu-arx/qp/branch/master/graph/badge.svg)](https://codecov.io/github/qu-arx/qp)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Pandas API reference

## Motivation

To collect a database of the pandas API to enable gamified study,
or simple reference usage.

## Outline

- Either download docs as ZIP of HTML, or mine the package repo (parse RST with docutils to give
  doctrees). The latter would be preferable (but perhaps not useful since autosummary is used).
- Make sqlite3 database with fields: name (e.g. "DataFrame"), qualname prefix (e.g. "pandas"), type
  (e.g. "class"), and so on. This would amount to a 'walk' of the library's entity tree.
- Expose these entities in a structured way (as an entity tree).

## Possible applications

- 🐼 PQ Test: pandas API recall score, like an IQ test
- 🐼 PPM: typing test, for completing tasks in pandas

## Requires

- Python 3.10+

## Installation

```sh
pip install qpdb
```

> _qp_ is available from [PyPI](https://pypi.org/project/qpdb), and
> the code is on [GitHub](https://github.com/qu-arx/qp)

## Usage

The package can be used on the command line by calling `qp`

```sh
usage: qp [-h] [-v VERSION] [--domain DOMAIN] [-r ROLE] [-n NAMES]
          [--debug | --no-debug] [-c | --crawl | --no-crawl]
          [-q | --quiet | --no-quiet]
          [package]

positional arguments:
  package               (default: pandas)

options:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        (default: )
  --domain DOMAIN       (default: py)
  -r ROLE, --role ROLE  (default: )
  -n NAMES, --names NAMES
                        (default: )
  --debug, --no-debug   (default: False)
  -c, --crawl, --no-crawl
                        (default: False)
  -q, --quiet, --no-quiet
                        (default: False)
```

To print the inventory of names and their corresponding URLs, run `qp`.

To breakpoint and take a look at what info is available, run either 
`qp --debug` or `qp --debug --no-crawl`

To crawl each page of the docs, use `--crawl` (experimental)

To silence the STDERR header lines, add `-q` or `--quiet`

To get a list of all the entities in PyTorch (stable version) and their URLs, run:

```sh
qp torch -v stable -q | wc -l 
```
⇣
```
3366
```

To pull out just the `torch.Tensor` class methods, run:

```sh
qp torch -v stable --role method --names torch.Tensor -q | wc -l
```
⇣
```
514
```

This has many uses, for example to create a list of markdown format links, pipe it as:

```sh
echo "$(qp torch -v stable -r method -n torch.Tensor -q)" | \
  sed -e 's/ /]: /g' -e 's/^torch\.Tensor\./[/g'
```
⇣
```md
[abs]: https://pytorch.org/docs/stable/generated/torch.Tensor.abs.html#torch.Tensor.abs
[abs_]: https://pytorch.org/docs/stable/generated/torch.Tensor.abs_.html#torch.Tensor.abs_
[absolute]: https://pytorch.org/docs/stable/generated/torch.Tensor.absolute.html#torch.Tensor.absolute
[absolute_]: https://pytorch.org/docs/stable/generated/torch.Tensor.absolute_.html#torch.Tensor.absolute_
[acos]: https://pytorch.org/docs/stable/generated/torch.Tensor.acos.html#torch.Tensor.acos
[acos_]: https://pytorch.org/docs/stable/generated/torch.Tensor.acos_.html#torch.Tensor.acos_
...
```
