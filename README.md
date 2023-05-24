# _Cercis_

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Red_bud_2009.jpg/320px-Red_bud_2009.jpg)](https://en.wikipedia.org/wiki/Cercis)

_**Cercis**_ /ˈsɜːrsɪs/ is a Python code formatter that is more configurable than
[Black](https://github.com/psf/black) (a popular Python code formatter).

[_Cercis_](https://en.wikipedia.org/wiki/Cercis) is also the name of a deciduous tree
that boasts vibrant pink to purple-hued flowers, which bloom in early spring.

This code repository is forked from and directly inspired by
[Black](https://github.com/psf/black). The original license of Black is included in this
repository (see [LICENSE_ORIGINAL](./LICENSE_ORIGINAL)).

_Cercis_ inherited Black's very comprehensive test cases, which means we are confident
that our configurability addition does not introduce any undesirable side effects. We
also thoroughly tested every configurable options that we added.

In particular, via its configurable options, _Cercis_ can completely fall back to Black.
See [Section 4.5](#45-how-to-fall-back-to-blacks-behavior) below for more details.

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

## 3. _Cercis_'s code style

_Cercis_'s code style is largely consistent with the
[style of of Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html).

The main difference is that _Cercis_ provides several configurable options that Black
doesn't. Configurability is our main motivation behind creating _Cercis_.

_Cercis_ offers the following configurable options:

1. [Line length](#31-line-length)
2. [Single quote vs double quote](#32-single-quote-vs-double-quote)
3. [Tabs vs spaces](#33-tabs-vs-spaces)
4. [Base indentation spaces](#34-base-indentation-spaces)
5. [Extra indentation at line continuation](#35-extra-indentation-at-line-continuation)
   1. [At function definition](#351-at-function-definition---function-definition-extra-indent)
   2. [In other line continuations](#352-in-other-line-continuations---other-line-continuation-extra-indent)
   3. [At closing brackets](#353-at-closing-brackets---closing-bracket-extra-indent)
6. ["Simple" lines with long strings](#36-simple-lines-with-long-strings)
7. [Collapse nested brackets](#37-collapse-nested-brackets)
8. [Wrap lines ending with comments](#38-wrapping-long-lines-ending-with-comments)
9. [Keep blank lines in brackets](#39-keep-blank-lines-in-brackets)

The next section ([How to configure _Cercis_](#4-how-to-configure-cercis)) contains
detailed instructions of how to configure these options.

### 3.1. Line length

_Cercis_ uses 79 characters as the line length limit, instead of 88 (Black's default).

You can override this default if necessary.

| Option                 |                                           |
| ---------------------- | ----------------------------------------- |
| Name                   | `--line-length`                           |
| Abbreviation           | `-l`                                      |
| Default                | 79                                        |
| Black's default        | 88                                        |
| Command line usage     | `cercis -l=120 myScript.py`               |
| `pyproject.toml` usage | `line-length = 120` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--line-length=120]`               |

### 3.2. Single quote vs double quote

_Cercis_ uses single quotes (`'`) as the default for strings, instead of double quotes
(`"`) which is Black's default.

You can override this default if necessary.

| Option                 |                                              |
| ---------------------- | -------------------------------------------- |
| Name                   | `--single-quote`                             |
| Abbreviation           | `-sq`                                        |
| Default                | `True`                                       |
| Black's default        | `False`                                      |
| Command line usage     | `cercis -sq=True myScript.py`                |
| `pyproject.toml` usage | `single-quote = false` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--single-quote=False]`               |

### 3.3. Tabs vs spaces

_Cercis_ offers users the ability to use tabs rather than spaces.

There are two associated options:

- `--use-tabs` (bool): whether to use tabs or spaces to format the code

| Option                 |                                          |
| ---------------------- | ---------------------------------------- |
| Name                   | `--use-tabs`                             |
| Abbreviation           | `-tab`                                   |
| Default                | `False`                                  |
| Black's default        | `False`                                  |
| Command line usage     | `cercis -tab=True myScript.py`           |
| `pyproject.toml` usage | `use-tabs = false` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--use-tabs=False]`               |

- `--tab-width` (int): when calculating line length (to determine whether to wrap
  lines), how wide shall _Cercis_ treat each tab. Only effective when `--use-tabs` is
  set to `True`.

| Option                 |                                       |
| ---------------------- | ------------------------------------- |
| Name                   | `--tab-width`                         |
| Abbreviation           | `-tw`                                 |
| Default                | 4                                     |
| Black's default        | N/A                                   |
| Command line usage     | `cercis -tab=True -tw=2 myScript.py`  |
| `pyproject.toml` usage | `tab-width = 2` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--tab-width=2]`               |

### 3.4. Base indentation spaces

This option defines the number of spaces that each indentation level adds. This option
has no effect when `--use-tabs` is set to `True`.

For example, if you set it to 2, contents within a `for` block is indented 2 spaces:

```python
for i in (1, 2, 3, 4, 5):
  print(i)
```

| Option                 |                                                     |
| ---------------------- | --------------------------------------------------- |
| Name                   | `--base-indentation-spaces`                         |
| Abbreviation           | `-bis`                                              |
| Default                | 4                                                   |
| Black's default        | 4                                                   |
| Command line usage     | `cercis -bis=True -tw=2 myScript.py`                |
| `pyproject.toml` usage | `base-indentation-spaces = 2` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--base-indentation-spaces=2]`               |

### 3.5. Extra indentation at line continuations

There are three associated options:

- `--function-definition-extra-indent`
- `--other-line-continuation-extra-indent`
- `--closing-bracket-extra-indent`

They control whether we add an **additional** indentation level in some situations. Note
that these options can work well with tabs (`--use-tabs=True`).

#### 3.5.1. At function definition (`--function-definition-extra-indent`)

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

We choose to add an extra indentation level when wrapping a function signature line.
This is because `def␣` happens to be 4 characters, so when the base indentation is 4
spaces, it can be difficult to visually distinguish the function name and the argument
list if we don't add an extra indentation.

If you set `--base-indentation-spaces` to other values than 4, this visual separation
issue will disappear, and you may not need to turn this option on.

This style is encouraged [in PEP8](https://peps.python.org/pep-0008/#indentation).

| Option                 |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| Name                   | `--function-definition-extra-indent`                            |
| Abbreviation           | `-fdei`                                                         |
| Default                | `True`                                                          |
| Black's default        | `False`                                                         |
| Command line usage     | `cercis -fdei=False myScript.py`                                |
| `pyproject.toml` usage | `function-definition-extra-indent = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--function-definition-extra-indent=False]`              |

#### 3.5.2. In other line continuations (`--other-line-continuation-extra-indent`)

"Other line continuations" are cases other than in function definitions, such as:

```python
var = some_function(
    arg1_with_long_name,
    arg2_with_longer_name,
)

var2 = [
    'something',
    'something else',
    'something more',
]
```

So if you set this option (`--other-line-continuation-extra-indent`) to `True`, you can
add an extra level of indentation in these cases:

```python
var = some_function(
        arg1_with_long_name,
        arg2_with_longer_name,
)

var2 = [
        'something',
        'something else',
        'something more',
]
```

| Option                 |                                                                     |
| ---------------------- | ------------------------------------------------------------------- |
| Name                   | `--other-line-continuation-extra-indent`                            |
| Abbreviation           | `-olcei`                                                            |
| Default                | `False`                                                             |
| Black's default        | `False`                                                             |
| Command line usage     | `cercis -olcei=True myScript.py`                                    |
| `pyproject.toml` usage | `other-line-continuation-extra-indent = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [----other-line-continuation-extra-indent=False]`            |

#### 3.5.3. At closing brackets (`--closing-bracket-extra-indent`)

This option lets people customize where the closing bracket should be. Note that both
styles are OK according to [PEP8](https://peps.python.org/pep-0008/#indentation).

<table>
  <tr>
    <td>

```python
# --closing-bracket-extra-indent=False

def function(
        arg1: int,
        arg2: float,
        arg3_with_long_name: list,
) -> None:
    print('Hello world')


result = func2(
    12345,
    3.1415926,
    [1, 2, 3],
)


something = {
    'a': 1,
    'b': 2,
    'c': 3,
}
```

  </td>

  <td>

```python
# --closing-bracket-extra-indent=True

def function(
        arg1: int,
        arg2: float,
        arg3_with_long_name: list,
        ) -> None:
    print('Hello world')


result = func2(
    12345,
    3.1415926,
    [1, 2, 3],
    )


something = {
    'a': 1,
    'b': 2,
    'c': 3,
    }
```

  </td>

  </tr>
</table>

| Option                 |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| Name                   | `--closing-bracket-extra-indent`                            |
| Abbreviation           | `-cbei`                                                     |
| Default                | `False`                                                     |
| Black's default        | `False`                                                     |
| Command line usage     | `cercis -cbei=True myScript.py`                             |
| `pyproject.toml` usage | `closing-bracket-extra-indent = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--closing-bracket-extra-indent=False]`              |

### 3.6. "Simple" lines with long strings

By default, Black wraps lines that exceed length limit. But for very simple lines (such
as assigning a long string to a variable), line wrapping is not necessary.

<table>
  <tr>
    <td>

```python
# Cercis's default style
# (Suppose line length limit is 30 chars)

# Cercis doesn't wrap slightly long lines
var1 = 'This line has 31 chars'



# Cercis doesn't wrap longer lines
var2 = 'This line has 43 characters_______'


# Falls back to Black when comments present
var3 = (
    'shorter line'  # comment
)
```

  </td>

  <td>

```python
# Black's style (not configurable)
# (Suppose line length limit is 30 chars)

# Black wraps slightly long lines
var1 = (
    "This line has 31 chars"
)

# But Black doesn't wrap longer lines
var2 = "This line has 43 characters_______"


# Black wraps comments like this:
var3 = (
    "shorter line"  # comment
)
```

  </td>

  </tr>
</table>

| Option                 |                                                           |
| ---------------------- | --------------------------------------------------------- |
| Name                   | `--wrap-line-with-long-string`                            |
| Abbreviation           | `-wl`                                                     |
| Default                | `False`                                                   |
| Black's default        | `True`                                                    |
| Command line usage     | `cercis -wl=True myScript.py`                             |
| `pyproject.toml` usage | `wrap-line-with-long-string = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--wrap-line-with-long-string=False]`              |

### 3.7. Collapse nested brackets

_Cercis_ by default collapses nested brackets to make the code more compact.

<table>
  <tr>
    <td>

```python
# Cercis's default style

# If line length limit is 30
value = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
])



# If line length limit is 10
value = function({
    1,
    2,
    3,
    4,
    5,
})


```

  </td>

  <td>

```python
# Black's style (not configurable)

# If line length limit is 30
value = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0],
    ]
)

# If line length limit is 10
value = function(
    {
        1,
        2,
        3,
        4,
        5,
    }
)
```

  </td>

  </tr>
</table>

| Option                 |                                                         |
| ---------------------- | ------------------------------------------------------- |
| Name                   | `--collapse-nested-brackets`                            |
| Abbreviation           | `-cnb`                                                  |
| Default                | `True`                                                  |
| Black's style          | `False`                                                 |
| Command line usage     | `cercis -cnb=True myScript.py`                          |
| `pyproject.toml` usage | `collapse-nested-brackets = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--collapse-nested-brackets=False]`              |

The code implementation of this option comes from
[Pyink](https://github.com/google/pyink), another forked project from Black.

### 3.8. Wrapping long lines ending with comments

Sometimes we have lines that exceed the length limit only because of the in-line
comment. If we do not want to wrap those lines, we can use two options provided here:

- `--wrap-comments`
- `--wrap-pragma-comments`

"Pragma comments", in this context, mean the directives for Python linters usually to
tell them to ignore certain errors. Pragma comments that _Cercis_ currently recognizes
include:

- _noqa_: `# noqa: E501`
- _type: ignore_: `# type: ignore[no-untyped-def]`
- _pylint_: `# pylint: disable=protected-access`
- _pytype_: `# pytype: disable=attribute-error`

| Option                 |                                              |
| ---------------------- | -------------------------------------------- |
| Name                   | `--wrap-comments`                            |
| Abbreviation           | `-wc`                                        |
| Default                | `False`                                      |
| Black's style          | `True`                                       |
| Command line usage     | `cercis -wc=True myScript.py`                |
| `pyproject.toml` usage | `wrap-comments = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--wrap-comments=False]`              |

| Option                 |                                                     |
| ---------------------- | --------------------------------------------------- |
| Name                   | `--wrap-pragma-comments`                            |
| Abbreviation           | `-wpc`                                              |
| Default                | `False`                                             |
| Black's style          | `True`                                              |
| Command line usage     | `cercis -wpc=True myScript.py`                      |
| `pyproject.toml` usage | `wrap-pragma-comments = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--wrap-pragma-comments=False]`              |

And below is a 2x2 matrix to explain how these two options work together:

|              | `-wc=True`                          | `-wc=False`             |
| ------------ | ----------------------------------- | ----------------------- |
| `-wpc=True`  | All comments wrapped w.n.           | No comments are wrapped |
| `-wpc=False` | p.c. not wrapped; o.c. wrapped w.n. | No comments are wrapped |

Note:

- "w.n." means "when necessary"
- "p.c." means "pragma comments"
- "o.c." means "other comments"

### 3.9. Keep blank lines in brackets

This option allows us to keep the blank lines that we intentionally add into the
contents of brackets.

<table>
  <tr>
    <td>

Cercis's default style:

```python
my_list = [
    # Group 1
    1,
    2,

    # Group 2
    3,
    4,

    # Group 3
    5,
    6,
]
```

  </td>

  <td>

Black's default style (not configurable):

```python
my_list = [
    # Group 1
    1,
    2,
    # Group 2
    3,
    4,
    # Group 3
    5,
    6,
]


```

  </td>

  </tr>
</table>

| Option                 |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| Name                   | `--keep-blank-lines-in-brackets`                            |
| Abbreviation           | `-kblib`                                                    |
| Default                | `True`                                                      |
| Black's style          | `False`                                                     |
| Command line usage     | `cercis -kblib=True myScript.py`                            |
| `pyproject.toml` usage | `keep-blank-lines-in-brackets = true` under `[tool.cercis]` |
| `pre-commit` usage     | `args: [--keep-blank-lines-in-bracketss=False]`             |

(Note: if `--keep-blank-lines-in-brackets` is `True`, multiple consecutive blank lines
are compressed into one blank line after formatting.)

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
        args: [--function-definition-extra-indent=False, --line-length=79]
  - repo: https://github.com/jsh9/cercis
    rev: 0.1.0
    hooks:
      - id: cercis-jupyter
        args: [--function-definition-extra-indent=False, --line-length=79]
```

The value in `rev` can be any _Cercis_ release, or it can be `main`, which means to
always use the latest (including unreleased) _Cercis_ features.

### 4.4. Specify options in `tox.ini`

Currently, _Cercis_ does not support a config section in `tox.ini`. Instead, you can
specify the options in `pyproject.toml`.

### 4.5. How to fall back to Black's behavior

Here are the configuration options to fall back to Black's behavior. Put them in
`pyproject.toml`:

```toml
[tool.cercis]
line-length = 88
single-quote = false
use-tabs = false
base-indentation-spaces = 4
function-definition-extra-indent = false
other-line-continuation-extra-indent = false
closing-bracket-extra-indent = false
wrap-line-with-long-string = true
collapse-nested-brackets = false
wrap-comments = true
wrap-pragma-comments = true
```
