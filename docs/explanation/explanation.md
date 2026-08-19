# Explanation

## What this tool is

`nomad-north-mpes-igor` is a NORTH tool for multi-dimensional photoemission spectroscopy (MPES)
groups whose ARPES data-reduction pipeline runs in [Igor Pro](https://www.wavemetrics.com/){:target="_blank" rel="noopener"} after the Python-based mpes analysis steps. It builds `FROM ghcr.io/fairmat-nfdi/pynxtools-mpes:main` (the [`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes){:target="_blank" rel="noopener"} NORTH tool and adds [Wine](https://www.winehq.org/){:target="_blank" rel="noopener"} + Igor Pro on top, so one
container offers both halves of the pipeline instead of running two NORTH tools side by side.

## Why Igor is never committed here

Igor Pro is proprietary and requires a license — only some institutions and oasis operators hold a license. The Dockerfile and desktop-integration steps (Wine install, `Igor.desktop` shortcut, autostart wiring) live in this open repository, but the actual licensed Igor installer/Wine prefix is supplied locally at build time by whoever has a license, and is never committed (see [How-to guides > Build the Image](../how_to/build_the_image.md) for the build steps). Because of this, the package also has **no** automatic CI build/publish workflow for the Docker image, and the `image` field on its `NORTHTool` entry point is a placeholder rather than something CI keeps up to date — expect to reconfigure it per-deployment via `nomad.yaml`