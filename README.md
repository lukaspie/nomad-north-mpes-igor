# nomad-north-mpes-igor

NOMAD NORTH plugin for Igor Pro on the mpes NORTH tool via Wine.

## About

This plugin registers a NORTH tool that layers [Wine](https://www.winehq.org/) and [Igor Pro](https://www.wavemetrics.com/) on top of the [`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes) NORTH tool image, for ARPES data reduction workflows that continue in Igor after the Python-based mpes analysis steps.

Because Igor Pro is proprietary and requires a valid license, **the Igor installer and Wine prefix are never committed to this repository**, and unlike other `nomad-north-*` packages, this one has no automated CI build or publishing workflow -- the image has to be built manually by someone with a license.

This `nomad` plugin was generated with `Cookiecutter` along with `@nomad`'s [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin) template.

## Docs

More information about this plugin is available in the [documentation](https://fairmat-nfdi.github.io/nomad-north-mpes-igor/), including how to
[build the image](https://fairmat-nfdi.github.io/nomad-north-mpes-igor/how_to/build_the_image/).

## Adding this plugin to NOMAD

Currently, NOMAD has two distinct flavors that are relevant depending on your role as an user:
1. [A NOMAD Oasis](#adding-this-plugin-in-your-nomad-oasis): any user with a NOMAD Oasis instance.
2. [Local NOMAD installation and the source code of NOMAD](#adding-this-plugin-in-your-local-nomad-installation-and-the-source-code-of-nomad): internal developers.

### Adding this plugin in your NOMAD Oasis

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

### Adding this plugin in your local NOMAD installation and the source code of NOMAD

We now recommend using the dedicated [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev) repository to simplify the process. Please refer to that repository for detailed instructions.

### Template update

We use [`cruft`](https://github.com/cruft/cruft) to update the project based on template changes. To run the check for updates locally, run `cruft update` in the root of the project. More details see the instructions on [`cruft` website](https://cruft.github.io/cruft/#updating-a-project).

## Main contributors
| Name | E-mail     |
|------|------------|
| Lukas Pielsticker | [lukas.pielsticker@physik.hu-berlin.de](mailto:lukas.pielsticker@physik.hu-berlin.de)
| Laurenz Rettig | [rettig@fhi-berlin.mpg.de](mailto:rettig@fhi-berlin.mpg.de) / [l.rettig@rptu.de](mailto:l.rettig@rptu.de) |
