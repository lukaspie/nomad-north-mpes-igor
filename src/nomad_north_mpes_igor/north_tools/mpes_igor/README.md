# `mpes_igor` - NORTH tool

This directory contains the Dockerfile and desktop-integration config for the `mpes-igor` NORTH
tool: Wine + Igor Pro layered on top of the `pynxtools-mpes` NORTH tool image.

## Base image

Builds `FROM ghcr.io/fairmat-nfdi/pynxtools-mpes:main` — the published `pynxtools-mpes` NORTH
tool image, not `nomad-north-jupyter`/`nomad-north-desktop-base` directly. That image already
provides the full mpes community-tool stack (sed-processor, specsanalyzer, arpes, silx, ...) on
top of `nomad-north-desktop-base`; this Dockerfile only adds Wine and Igor.

## Prerequisite: a local, licensed Igor Wine prefix

Igor Pro is proprietary. This build **requires** a Wine prefix with Igor Pro already installed,
placed locally at `./igor-wine` (relative to this directory, i.e.
`src/nomad_north_mpes_igor/north_tools/mpes_igor/igor-wine/`) before running `docker build` —
it is gitignored and must never be committed. See the top-level
[README](../../../../README.md#building-the-image) for how to produce it and the full build
command. There is no automatic CI build for this image.

## Building and testing

```bash
docker build -f src/nomad_north_mpes_igor/north_tools/mpes_igor/Dockerfile \
    -t nomad-north-mpes-igor:dev .
```

```bash
docker run -p 8888:8888 nomad-north-mpes-igor:dev
```

Open `http://localhost:8888/desktop` — Igor should appear as a desktop icon, pre-trusted (no
xfce "untrusted launcher" prompt), alongside the mpes community tools inherited from the base
image.

## Documentation

For comprehensive documentation on creating and managing NORTH tools, including:

- Entry point configuration and `NORTHTool` API
- Docker image structure and best practices
- Dependency management

See the [NOMAD NORTH Tools documentation](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html).
