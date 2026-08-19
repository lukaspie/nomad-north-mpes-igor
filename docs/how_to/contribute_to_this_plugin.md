# Contribute to This Plugin

This guide walks through setting up a working environment for developing `nomad-north-mpes-igor`.

!!! info "Structure of this repository"
    The plugin's Python side (the `NORTHTool`/`NORTHToolEntryPoint` definition) lives in
    [`src/nomad_north_mpes_igor`](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/tree/main/src/nomad_north_mpes_igor){:target="_blank" rel="noopener"}.
    The container itself -- Dockerfile and Igor/Wine desktop-integration config -- lives in
    [`src/nomad_north_mpes_igor/north_tools/mpes_igor`](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/tree/main/src/nomad_north_mpes_igor/north_tools/mpes_igor){:target="_blank" rel="noopener"},
    which has its own [README](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/blob/main/src/nomad_north_mpes_igor/north_tools/mpes_igor/README.md){:target="_blank" rel="noopener"}
    covering the Docker side in more detail.

## Setup

It is recommended to use Python 3.12 with a dedicated virtual environment. We recommend [`uv`](https://github.com/astral-sh/uv){:target="_blank" rel="noopener"}, an extremely fast Python package and project manager; a more classical `venv`/`pip` approach works too.

=== "uv"
    `uv` is capable of creating a virtual environment and installing the required Python version at the same time.

    ```bash
    uv venv --python 3.11
    ```

=== "venv"
    Note that you will need to install the Python version manually beforehand.

    ```bash
    python3.11 -m venv .venv
    . .venv/bin/activate
    ```

## Development installation

Clone the repository:

```console
git clone https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor.git
cd nomad-north-mpes-igor
```

Install the package in editable mode, together with its dev dependencies:

=== "uv"

    ```bash
    uv pip install -e ".[dev]"
    ```

=== "pip"

    ```bash
    pip install --upgrade pip
    pip install -e ".[dev]"
    ```

## Linting, formatting, and pre-commit hooks

We use [Ruff](https://docs.astral.sh/ruff/){:target="_blank" rel="noopener"} for linting/formatting and mypy for type checking. `.pre-commit-config.yaml` also runs pyupgrade, nbstripout, and cspell. We use [`prek`](https://github.com/j178/prek){:target="_blank" rel="noopener"} -- a drop-in, faster reimplementation of `pre-commit` that reads the same config file -- as the runner; it's installed as part of the `dev` extra above, so you just need to enable the hook once per clone:

```console
prek install           # installs the git hook
prek run --all-files   # run all hooks against the whole repo once
```

You can also run Ruff directly:

```console
ruff check .
ruff format . --check
```

If `cspell` flags a real (correctly spelled) word, add it to `.cspell/custom-dictionary.txt`, or regenerate it from the current source/docs:

```console
scripts/generate_custom_dict.sh
```

## Working on the Docker image

Unlike most sibling `nomad-north-*` plugins, there is **no CI build** for this image -- Igor Pro
is proprietary and can't be built or tested from a public GitHub Actions runner. If you're
changing the [Dockerfile](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/blob/main/src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile){:target="_blank" rel="noopener"}
or the Wine/Igor desktop-integration config, you need a local, licensed Igor Wine prefix to test
against -- see [How-to guides > Build the Image](build_the_image.md) for how to produce one and
build/run the image locally.

Changes that don't touch the Igor-specific steps (e.g. the generic WineHQ install block) can be
tested against just the Wine layer, without a real Igor installation:

```console
mkdir -p src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine  # empty placeholder
docker build -f src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile \
    -t nomad-north-mpes-igor:dev .
docker run -p 8888:8888 nomad-north-mpes-igor:dev
```

Then point `NORTHTool.image` in
[`src/nomad_north_mpes_igor/north_tools/__init__.py`](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/blob/main/src/nomad_north_mpes_igor/north_tools/__init__.py){:target="_blank" rel="noopener"}
at your local tag to test it end-to-end from within a running NOMAD -- see
[How-to guides > Install this Plugin](install_this_plugin.md) and the
[NORTH tools how-to](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html){:target="_blank" rel="noopener"}
for details on testing local images. Revert that change before merging.

## Testing

Unit tests are written with [pytest](https://docs.pytest.org/en/stable/){:target="_blank" rel="noopener"}:

```console
pytest -sv tests
```

These test the Python entry point only (registration, field values) -- they don't build the
Docker image or need Igor/Wine installed.

## Contributing on GitHub

Fork the repository, commit your changes on a branch in your fork, and open a pull request
against `FAIRmat-NFDI/nomad-north-mpes-igor`. CI checks linting, runs the tests, and builds the
docs -- it does **not** build the Docker image (see
[Working on the Docker image](#working-on-the-docker-image) above). Once checks pass and a review
happens, the PR can be merged.

Changing something in `docs/`? See [How-to guides > Contribute to the Documentation](contribute_to_the_documentation.md) for the writing conventions, how to build the docs locally, and how to add a new page.

### Template updates

This project was generated from, and stays in sync with, FAIRmat's [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin){:target="_blank" rel="noopener"} template via [`cruft`](https://github.com/cruft/cruft){:target="_blank" rel="noopener"}. To check for and apply template updates, run `cruft update` in the repository root -- see the [`cruft` documentation](https://cruft.github.io/cruft/#updating-a-project){:target="_blank" rel="noopener"} for details. `.github/*` workflow files are excluded from these updates to avoid permissions issues.

### Releasing

Unlike siblings that embed a NORTH tool, this package's release workflow does **not**
auto-update the image tag in `NORTHTool` before publishing -- there's no CI-built image for it
to point at. See the [project README > Publish note](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor#publish-note){:target="_blank" rel="noopener"}.

## Developing this plugin as part of NOMAD

If you're testing this plugin's NORTH integration against a full NOMAD instance -- not just its own unit tests -- use [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}, FAIRmat's development environment for NOMAD and its plugins. See [How-to guides > Install this Plugin](install_this_plugin.md) for how this repo is wired into that workspace.

## Troubleshooting

If you hit an issue with the tool or with setting up the development environment, open a [GitHub issue](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/issues/new){:target="_blank" rel="noopener"}.
