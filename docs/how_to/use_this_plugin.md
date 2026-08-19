# How to Use This Plugin

This plugin can be used in a NOMAD Oasis installation that has been configured to point at a
built `mpes-igor` image -- see [Install this Plugin](install_this_plugin.md) if that hasn't
happened yet.

## Launching mpes-igor

Once installed and configured, **mpes-igor** shows up in NORTH's tool launcher for any file in
an upload with one of the following extensions: `ipynb`, `nxs`, `h5`, or `hdf5`. Selecting it
starts a container with:

- the full [`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes){:target="_blank" rel="noopener"} NORTH tool -- JupyterLab, and the mpes community analysis stack (sed-processor, specsanalyzer, arpes, silx, ...) -- opened directly into the desktop (`default_url: /desktop`);
- Igor Pro, available as a desktop icon
- the triggering upload mounted at `/home/jovyan`, so files in that upload are visible from
  both the Python tools and, via symlinks set up at container start, Igor's own file dialogs.

## A typical workflow

1. Reduce and export MPES/ARPES data using the Python tools (see
   [`pynxtools-mpes`'s own docs](https://fairmat-nfdi.github.io/pynxtools-mpes/){:target="_blank" rel="noopener"}).
2. Open Igor Pro from the desktop icon and continue the analysis there, loading the
   Python-exported data.
3. Save results back under the mounted upload directory so they're persisted as part of the
   upload.

!!! note "Attention"
    Only files saved back under the mounted upload directory are persisted as part of the
    upload. Anything written elsewhere in the container -- including inside the Wine prefix
    itself -- is lost when the session ends.
