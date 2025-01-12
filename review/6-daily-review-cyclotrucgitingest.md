# 🚀 cyclotruc/gitingest

## Usage

```bash
pip install gitingest
```

```shell
Usage: gitingest [OPTIONS] SOURCE

  Analyze a directory and create a text dump of its contents.

Options:
  -o, --output TEXT           Output file path (default: <repo_name>.txt in
                              current directory)
  -s, --max-size INTEGER      Maximum file size to process in bytes
  -e, --exclude-pattern TEXT  Patterns to exclude
  -i, --include-pattern TEXT  Patterns to include
  --help                      Show this message and exit.
```