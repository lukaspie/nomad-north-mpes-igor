# Tutorial

This is a short walkthrough of launching `mpes-igor` on an MPES file from inside a NOMAD Oasis. It assumes the plugin is already installed, built, and configured (see
[How-to > Build the Image](../how_to/build_the_image.md) and [How-to > Install this Plugin](../how_to/install_this_plugin.md)).

## Prerequisites

- Access to a NOMAD Oasis with this plugin enabled and NORTH running, pointed at an image you built yourself (see the how-to guides above).
- An upload containing at least one file with one of the supported extensions: `ipynb`, `nxs`, `h5`, or `hdf5`.

## Steps

1. **Open your upload.** In the NOMAD GUI, navigate to the upload that contains the MPES file
   you want to work with.
2. **Launch mpes-igor.** From the upload's file browser, open the tool launcher for that file
   (or the upload's list of available NORTH tools) and select **mpes-igor**. The first launch
   pulls and starts the container, which can take a moment.
3. **Work in the desktop.** NORTH opens a remote desktop session with your upload's files
   mounted and visible, JupyterLab and the mpes Python tools ready to use, and an Igor Pro
   desktop icon.
4. **Reduce data in Python, continue in Igor.** Use the mpes community tools
   (sed-processor, specsanalyzer, arpes) for the initial reduction and binning steps, then open
   Igor Pro from the desktop for whatever analysis continues there. See
   [How-to > Use this Plugin](../how_to/use_this_plugin.md) for what's available in each.
5. **Save results back to the upload.** Files you save under the mounted upload directory
   become part of the upload and can be reprocessed like any other upload file.

!!! tip "Important"
    Anything you save outside the mounted upload directory -- including inside Igor's own Wine
    environment -- is lost once the container session ends.
