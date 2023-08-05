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
usage: qp [-h] [-v VERSION] [-d | --debug | --no-debug]
          [-f | --fetch | --no-fetch]
          [package_name]

positional arguments:
  package_name          (default: pandas)

options:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        (default: )
  -d, --debug, --no-debug
                        (default: False)
  -f, --fetch, --no-fetch
                        (default: True)
```

To print the inventory of names and their corresponding URLs,
run `qp --no-fetch`. (The `--fetch` flag is assumed by default)

To breakpoint and take a look at what info is available, run either 
`qp --debug` or `qp --debug --no-fetch`

To silence the STDERR output, add `-q` or `--quiet`

To get a list of all the entities in PyTorch (stable version) and their URLs, run:

```sh
qp torch -v stable -q --no-fetch
```

and for example to pull out the `torch.Tensor` class methods, run:

```sh
echo "$(qp torch -v stable -q --no-fetch | grep -E '^torch.Tensor\.')" | cut -d\. -f 3-
```

This gives:

```
H https://pytorch.org/docs/1.12/tensors.html#torch.Tensor.H
T https://pytorch.org/docs/1.12/tensors.html#torch.Tensor.T
abs https://pytorch.org/docs/1.12/generated/torch.Tensor.abs.html#torch.Tensor.abs
abs_ https://pytorch.org/docs/1.12/generated/torch.Tensor.abs_.html#torch.Tensor.abs_
absolute https://pytorch.org/docs/1.12/generated/torch.Tensor.absolute.html#torch.Tensor.absolute
absolute_ https://pytorch.org/docs/1.12/generated/torch.Tensor.absolute_.html#torch.Tensor.absolute_
...
```

For example, to create a list of markdown format links, pipe that on to:

```sh
... | sed 's/ /]: /g' | sed 's/^/[/g'
```
⇣
```
[H]: https://pytorch.org/docs/stable/tensors.html#torch.Tensor.H
[T]: https://pytorch.org/docs/stable/tensors.html#torch.Tensor.T
[abs]: https://pytorch.org/docs/stable/generated/torch.Tensor.abs.html#torch.Tensor.abs
[abs_]: https://pytorch.org/docs/stable/generated/torch.Tensor.abs_.html#torch.Tensor.abs_
[absolute]: https://pytorch.org/docs/stable/generated/torch.Tensor.absolute.html#torch.Tensor.absolute
[absolute_]: https://pytorch.org/docs/stable/generated/torch.Tensor.absolute_.html#torch.Tensor.absolute_
[acos]: https://pytorch.org/docs/stable/generated/torch.Tensor.acos.html#torch.Tensor.acos
[acos_]: https://pytorch.org/docs/stable/generated/torch.Tensor.acos_.html#torch.Tensor.acos_
[acosh]: https://pytorch.org/docs/stable/generated/torch.Tensor.acosh.html#torch.Tensor.acosh
[acosh_]: https://pytorch.org/docs/stable/generated/torch.Tensor.acosh_.html#torch.Tensor.acosh_
...
```

but perhaps you only want methods of the class, not attributes:
