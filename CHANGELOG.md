# Change Log

## [0.2.1] - 2023-07-23

- Changed
  - Rebased `Cercis` to be head to head with `Black`
- Fixed
  - Fixed a pytest regression where Python warnings are treated as errors
    (https://github.com/jsh9/cercis/commit/1229b9dd18f861423e26f8de3f4b5e714d72bd9c)
- Diff
  - https://github.com/jsh9/cercis/compare/0.2.0...0.2.1

## [0.2.0] - 2023-07-12

- Changed
  - Rebased `Cercis` to be head to head with `Black`
    [version 23.7.0](https://github.com/psf/black/releases/tag/23.7.0)
- Diff
  - https://github.com/jsh9/cercis/compare/0.1.7...0.2.0

## [0.1.7] - 2023-06-19

- Changed
  - Pulled in the latest changes from psf/black (code diff:
    https://github.com/jsh9/cercis/pull/27)

## [0.1.6] - 2023-05-23

- Added
  - A new option `--wrap-comments` to not wrap any comments (not just pragma comments)
  - A new option `--keep-blank-lines-in-brackets`
- Changed
  - Improved the CLI output text colors because the current colors are confusing or not
    quite legible

## [0.1.5] - 2023-05-09

- Added
  - Configurability to use tabs instead of spaces (two new options: `--use-tabs` and
    `--tab-width`)
  - Configurability on base indentation spaces and extra indentation at different line
    continuation situations

## [0.1.4] - 2023-05-07

- Added
  - A new configurable option: `--closing-bracket-extra-indent`

## [0.1.3] - 2023-05-07

- Added

  - A new configurable option: `--collapse-nested-brackets`
  - A new configurable option: `--wrap-pragma-comments`
  - Some Github workflow actions to make sure CHANGELOG.md is updated

- Changed

  - Changed the default quote to single quote
  - Changed the default line length to 79 characters

- Removed
  - Some unrelated documentation and config files

## [0.1.2] - 2023-05-04

- Added
  - Merged 2 changes from psf/black:main ([#5](https://github.com/jsh9/cercis/pull/5))
  - Added option to not wrap "simple" lines with long strings
    ([#6](https://github.com/jsh9/cercis/pull/6))
- Full changelog
  - https://github.com/jsh9/cercis/compare/0.1.1...0.1.2

## [0.1.1] - 2023-05-03

- Added
  - A configurable option: `single-quote`, for formatting code into single quotes
- Full changelog
  - https://github.com/jsh9/cercis/compare/0.1.0...0.1.1

## [0.1.0] - 2023-04-30

- This is the initial version that branches away from Black (commit:
  [e712e4](https://github.com/psf/black/commit/e712e48e06420d9240ce95c81acfcf6f11d14c83))
- Changed
  - The default indentation within a function definition (when line wrap happens) is now
    8 spaces. (Black's default is 4, which is
    [not PEP8-compatible](https://github.com/psf/black/issues/1127))
  - Updated README, because `cercis` now branches away from Black
- Added
  - A configurable option (`function-definition-extra-indent`) is added instead of
    enforcing 8 spaces for everyone
