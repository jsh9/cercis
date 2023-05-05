# Cercis

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Red_bud_2009.jpg/320px-Red_bud_2009.jpg)](https://en.wikipedia.org/wiki/Cercis)

_**Cercis**_ /ˈsɜːrsɪs/ is a Python code formatter that is more configurable than
[Black](https://github.com/psf/black) (a popular Python code formatter).

[_Cercis_](https://en.wikipedia.org/wiki/Cercis) is also the name of a deciduous tree
that boasts vibrant pink to purple-hued flowers, which bloom in early spring.

This code repository is forked from and directly inspired by
[Black](https://github.com/psf/black). The original license of Black is included in this
repository (see [LICENSE_ORIGINAL](./LICENSE_ORIGINAL)).

## 1. Motivations

While we like the idea of auto-formatting and code readability, we take issue with some
style choices and the lack of configurability of the Black formatter. Therefore,
_Cercis_ aims at providing some configurability beyond Black's limited offering.

## 2. Installation and usage

### 2.1. Installation

_Cercis_ can be installed by running `pip install cercis`. It requires Python 3.7+ to
run. If you want to format Jupyter Notebooks, install with
`pip install "cercis[jupyter]"`.

### 2.2. Usage

#### 2.2.1. Command line usage

To get started right away with sensible defaults:

```sh
cercis {source_file_or_directory}
```

You can run _Cercis_ as a package if running it as a script doesn't work:

```sh
python -m cercis {source_file_or_directory}
```

The commands above reformat entire file(s) in place.

#### 2.2.2. As pre-commit hook

To format Python files (.py), put the following into your `.pre-commit-config.yaml`
file. Remember to replace `<VERSION>` with your version of this tool (such as `v0.1.0`):

```yaml
- repo: https://github.com/jsh9/cercis
  rev: <VERSION>
  hooks:
    - id: cercis
      args: [--line-length=88]
```

To format Jupyter notebooks (.ipynb), put the following into your
`.pre-commit-config.yaml` file:

```yaml
- repo: https://github.com/jsh9/cercis
  rev: <VERSION>
  hooks:
    - id: cercis-jupyter
      args: [--line-length=88]
```

See [pre-commit](https://github.com/pre-commit/pre-commit) for more instructions. In
particular, [here](https://pre-commit.com/#passing-arguments-to-hooks) is how to specify
arguments in pre-commit config.

## 3. The code style

The code style in _Cercis_ is largely consistent with the
[style of of _Black_](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html).

The main difference is that _Cercis_ provides several configurable options that Black
doesn't. That's also our main motivation of creating _Cercis_.

_Cercis_ offers the following configurable options:

- [Extra indentation at function definition](#31-extra-indentation-at-function-definition)
- [Single quote vs double quote](#32-single-quote-vs-double-quote)
- ["Simple" lines with long strings](#33-simple-lines-with-long-strings)

The next section ([How to configure _Cercis_](#4-how-to-configure-cercis)) contains
detailed instructions of how to configure these options.

### 3.1. Extra indentation at function definition

<table>
  <tr>
    <td>

```python
# Cercis's default style
def some_function(
        arg1_with_long_name: str,
        arg2_with_longer_name: int,
        arg3_with_longer_name: float,
        arg4_with_longer_name: bool,
) -> None:
    ...
```

  </td>

  <td>

```python
# Black's style (not configurable)
def some_function(
    arg1_with_long_name: str,
    arg2_with_longer_name: int,
    arg3_with_longer_name: float,
    arg4_with_longer_name: bool,
) -> None:
    ...
```

  </td>

  </tr>
</table>

We choose to indent an extra 4 spaces because it adds a clear visual separation between
the function name and the argument list. Not adding extra indentation is also called out
as wrong in the the official
[PEP8 style guide](https://peps.python.org/pep-0008/#indentation).

If you do not like this default, you can easily turn it off.

| Option                 |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| Name                   | `--function-definition-extra-indent`                            |
| Abbreviation           | `-fdei`                                                         |
| Default                | `True`                                                          |
| Command line usage     | `cercis -fdei=False myScript.py`                                |
| `pyproject.toml` usage | `function-definition-extra-indent = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--function-definition-extra-indent=False]`              |

### 3.2. Single quote vs double quote

Both _Cercis_ and Black default to using double quotes. But in _Cercis_ you can specify
using single quotes as the default style.

| Option                 |                                             |
| ---------------------- | ------------------------------------------- |
| Name                   | `--single-quote`                            |
| Abbreviation           | `-sq`                                       |
| Default                | `False`                                     |
| Command line usage     | `cercis -sq=True myScript.py`               |
| `pyproject.toml` usage | `single-quote = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--single-quote=False]`              |

### 3.3. "Simple" lines with long strings

By default, Black wraps lines that exceed length limit. But for very simple lines (such
as assigning a long string to a variable), line wrapping is not necessary.

Also, as seen below, Black's default style can be a bit hard to predict (`var2` vs
`var3`).

<table>
  <tr>
    <td>

```python
# Cercis's default style
var1 = "not wrapped even if too long"

var2 = "not wrapped even if too long"  # comment

var3 = "not wrapped, if the line gets too long"
```

  </td>

  <td>

```python
# Black's style (not configurable)
var1 = (
    "wrapped when too long"
)

var2 = (
    "wrapped when too long"
)  # comment

var3 = "not wrapped, if the line gets too long"
```

  </td>

  </tr>
</table>

| Option                 |                                                           |
| ---------------------- | --------------------------------------------------------- |
| Name                   | `--wrap-line-with-long-string`                            |
| Abbreviation           | `-wl`                                                     |
| Default                | `False`                                                   |
| Command line usage     | `cercis -wl=True myScript.py`                             |
| `pyproject.toml` usage | `wrap-line-with-long-string = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--wrap-line-with-long-string=False]`              |

## 4. How to configure _Cercis_

### 4.1. Dynamically in the command line

Here are some examples:

- `cercis --single-quote=True myScript.py` to format files to single quotes
- `cercis --function-definition-extra-indent=False myScript.py` to format files without
  extra indentation at function definition
- `cercis --line-length=79 myScript.py` to format files with a line length of 79
  characters

### 4.2. In your project's `pyproject.toml` file

You can specify the options under the `[tool.cercis]` section of the file:

```toml
[tool.cercis]
line-length = 88
function-definition-extra-indent = true
single-quote = false
```

### 4.3. In your project's `.pre-commit-config.yaml` file

You can specify the options under the `args` section of your `.pre-commit-config.yaml`
file.

For example:

```yaml
repos:
  - repo: https://github.com/jsh9/cercis
    rev: 0.1.0
    hooks:
      - id: cercis
        args: [--function-definition-extra-indent=False, --ling-length=79]
  - repo: https://github.com/jsh9/cercis
    rev: 0.1.0
    hooks:
      - id: cercis-jupyter
        args: [--function-definition-extra-indent=False, --line-length=79]
```

### 4.4. Specify options in `tox.ini`

Currently, _Cercis_ does not support a config section in `tox.ini`. Instead, you can
specify the options in `pyproject.toml`.
