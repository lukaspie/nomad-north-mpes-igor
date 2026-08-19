# Welcome to the `nomad-north-mpes-igor` documentation

`nomad-north-mpes-igor` is a NOMAD NORTH plugin that layers [Wine](https://www.winehq.org/){:target="_blank" rel="noopener"} and [Igor Pro](https://www.wavemetrics.com/){:target="_blank" rel="noopener"} on top of the [`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes){:target="_blank" rel="noopener"} NORTH tool, for ARPES data-reduction workflows that continue in Igor.

Igor Pro is proprietary and requires a valid license, so unlike most `nomad-north-*` plugins, this one has no published image -- building it is always a manual, local step done by whoever holds a license. Start with [How-to guides > Build the Image](how_to/build_the_image.md).

<div markdown="block" class="home-grid">
<div markdown="block">

### Tutorial

A short walkthrough of launching mpes-igor on a file inside a NOMAD Oasis.

- [Tutorial](tutorial/tutorial.md)

</div>
<div markdown="block">

### How-to guides

How-to guides provide step-by-step instructions for a wide range of tasks, with the overarching topics:

- [Build the Image](how_to/build_the_image.md)
- [Install this plugin](how_to/install_this_plugin.md)
- [Use this plugin](how_to/use_this_plugin.md)
- [Contribute to this plugin](how_to/contribute_to_this_plugin.md)
- [Contribute to the documentation](how_to/contribute_to_the_documentation.md)

</div>

<div markdown="block">

### Explanation

The [Explanation](explanation/explanation.md) section covers what this NORTH tool is, why Igor
is never committed, and how it's built on `pynxtools-mpes`.

</div>
<div markdown="block">

### Reference

The [Reference](reference/references.md) section lists the tool's configuration (file
extensions, mount path, image), entry point, and base image.

</div>
</div>

<h2> Contact </h2>

For questions or suggestions:

- Open an issue on the [`nomad-north-mpes-igor` GitHub](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/issues)
- Join our [Discord channel ](https://discord.gg/Gyzx3ukUw8)
- Get in contact with our [lead developers](contact.md).

<h2>Project and community</h2>

The work is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - [460197019 (FAIRmat)](https://gepris.dfg.de/gepris/projekt/460197019?language=en).
