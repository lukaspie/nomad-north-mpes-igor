# Install This Plugin

Installing this plugin is two independent steps: getting the Python package installed (so NOMAD
discovers the `mpes-igor` entry point at all), and pointing NOMAD at an actual built image (since, unlike most `nomad-north-*` plugins, **the default `image` field is a placeholder with nothing real behind it** — see [Explanation](../explanation/explanation.md#why-igor-is-never-committed-here) for why). Skipping the second step means the entry point loads fine, but launching the tool fails trying to pull a nonexistent image.

## 1. Build the image

There is no published image to fall back on. Follow [How-to guides > Build the Image](build_the_image.md) first — you'll end up with a local Docker tag (or a tag pushed to your own registry).

## 2. Install the package

### In your NOMAD Oasis

If your Oasis is built from [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}, add `nomad-north-mpes-igor` as a dependency in your distro project's `pyproject.toml`, and rebuild/redeploy the Oasis image. See the [template README > Adding a plugin](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#adding-a-plugin){:target="_blank" rel="noopener"}
for the exact steps.

### In `nomad-distro-dev`

Add `nomad-north-mpes-igor` as a workspace dependency — see the
[`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}
README for how packages are wired into that workspace.

## 3. Point `nomad.yaml` at the image you built

This is the step that's easy to skip and not optional for this plugin. In the `nomad.yaml` of
the NOMAD instance you're running (your Oasis, or your local `nomad-distro-dev` checkout), add:

```yaml
plugins:
  entry_points:
    options:
      nomad_north_mpes_igor.north_tools:mpes_igor:
        north_tool:
          image: nomad-north-mpes-igor:latest # the tag you built/pushed in step 1
```

The key is the entry point's full `<module>:<object>` path (matching
`[project.entry-points.'nomad.plugin']` in `pyproject.toml`), not the short entry-point name.
See [Reference > `NORTHTool` configuration](../reference/references.md#northtool-configuration)
for the other fields you can override the same way (e.g. `display_name`), and the NOMAD docs'
[NORTH tools how-to > How to connect and use specific NORTH tools in a NOMAD deployment](https://fairmat-nfdi.github.io/nomad-docs/explanation/north.html#how-to-connect-and-use-specific-north-tools-in-a-nomad-deployment)
for the general mechanism.

If you pushed the image to a private registry rather than keeping a local tag, make sure the
machine running NORTH has pull access to it (e.g. a registry login), since it isn't public.

## 4. Restart

Restart the NOMAD instance. The **mpes-igor** tool should then appear in NORTH's tool launcher —
see [Use this Plugin](use_this_plugin.md).
