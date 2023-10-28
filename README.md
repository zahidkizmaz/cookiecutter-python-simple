# Cookiecutter Simple Python

This is a simple python project cookiecutter template suitable for creating ready to code project folder.

### Features

- Python: [3.12](https://docs.python.org/release/3.12.0/)
- Testing: [pytest](https://github.com/pytest-dev/pytest/)
- Package manager: [poetry](https://github.com/python-poetry/poetry)
- Linting and formatting: [ruff](https://github.com/astral-sh/ruff)
- Type checker: [mypy](https://github.com/python/mypy)
- Standardizing spaces and tabs: [editorconfig](https://editorconfig.org/)
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit)
- Optional integration with [asdf](https://github.com/asdf-vm/asdf) and [rtx](https://github.com/jdx/rtx) via `.tool_versions` file
- Optional integration with [Github Actions](https://github.com/features/actions)

### Quick Start

Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and generate a new python project:

```bash
$ cookiecutter https://github.com/zahidkizmaz/cookiecutter-python-simple
```

Cookiecutter prompts you for information regarding your project.
```no-highlight
[1/10] project_name (Python Project):
[2/10] project_slug (python_project):
[3/10] author_name (Zahid Kizmaz):
[4/10] email (tech@zahid.rocks):
[5/10] version (0.1.0):
[6/10] description (My Simple Python Project):
[7/10] python_version (3.12.0):
[8/10] use_tool_versions [y/n] (y):
[9/10] use_github_actions [y/n] (y):
[10/10] Select license
  1 - MIT
  2 - BSD-3
  3 - Apache Software License 2.0
  4 - GNU General Public License v3.0
  Choose from [1/2/3/4] (1):
```

That's it! Your simple python project is ready for coding.
```no-highlight
python_project
├── .editorconfig
├── .github
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .tool-versions
├── LICENSE
├── README.md
├── pyproject.toml
├── src
│   └── __init__.py
└── tests
    └── __init__.py
```
