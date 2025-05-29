# co.py — Smart File Copy and Transform Tool

**co.py** is a Python utility that copies files—single, multiple, or wildcard-matched—and optionally:

- Changes file extensions (e.g., `.svg` to `.ejs`)
- Applies regex-based transformations to file contents
- Writes to a different destination directory

---

## 🔧 Features

- Supports shell-style globbing (`*.svg`, `file1.txt file2.txt`)
- Changes file extension with `--to-ext`
- Applies content transformation using `--pattern` and `--replace`
- Outputs to a new directory with `--dest-dir`

---

## 📦 Installation

Copy the `co.py` script to your project. Requires Python 3.6+.

```bash
python3 --version
python co.py <source-files> [options]
```

## Options

| Option       | Description                                      |
| ------------ | ------------------------------------------------ |
| `--to-ext`   | Change file extension to this (e.g., `.ejs`)     |
| `--dest-dir` | Directory to place output files                  |
| `--pattern`  | Regex pattern to search in file contents         |
| `--replace`  | Replacement string to insert in place of matches |

## 📂 Examples

1. Copy .txt files to a new directory without changing them

```bash
python co.py notes/*.txt --dest-dir archived/
```

2. Convert .svg files to .ejs and add a class before viewBox=

```bash
python co.py hero/*.svg \
        --to-ext .ejs \
        --dest-dir ../some/other/path/ \
        --pattern 'viewBox=' \
        --replace 'class="<%= className %>" viewBox='
```

3. Copy two specific files and replace tabs with four spaces

```bash
python co.py file1.txt file2.txt \
        --pattern '\t' \
        --replace '    '
```
