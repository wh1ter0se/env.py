# env.py

Template repository for Python development environments

## About

### VS Code

Settings for a Python development environment in VS code are stored in the `.vscode/` directory, including:

- `extensions.json`: Recommended extensions
- `settings.json` General environment settings
- `tasks.json`: References to `scripts/` in a format VS Code can parse

### Python

- `pyproject.toml` defines the dependencies and other build information for the python module in `src/`

#### Packaging (`uv`)

#### Formatting (`ruff`)

### Markdown

#### Exporting (`)

#### Formatting

### Conventional Commits

This repository complies with the commit message format defined by [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). The list of scopes recognized by this environment is defined in `.vscode/settings.json`.

### Semantic Versioning

As part of this repo's GitHub Actions (pipelines), automatic semantic versioning is run on every commit to `main`. This means that the package version number never needs to be manually generated. Instead, this part of the pipeline will leverage the commit message format to calculate the version.

The version format, in compliance with Semantic Versioning, is `{major}.{minor}.{patch}`. This is stored in the file `{module_name}/_version.py`, and is referenced by `pyproject.toml` when building the package.

The rules that automatically define the version are:

- Types `build`, `chore`, `ci`, `docs`, `fix`, `perf`, `refactor`, `revert`, `style`, and `test` will increment the patch version
- Type `feat` will increment the minor version
- Inclusion of the prefix `BREAKING CHANGE` will increment the major version

## Related repositories

- [**env.py.scripts**](https://github.com/wh1ter0se/env.py.scripts): Scripts for automation of environment setup, dependency installation, and package generation
- [**env.py.scripts.test**](https://github.com/wh1ter0se/env.py.scripts.test): CI/CD tests for the automationm scripts
