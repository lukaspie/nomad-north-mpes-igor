# References

## `NORTHTool` configuration

Defined in [`src/nomad_north_mpes_igor/north_tools/__init__.py`](https://github.com/FAIRmat-NFDI/nomad-north-mpes-igor/blob/main/src/nomad_north_mpes_igor/north_tools/__init__.py){:target="_blank" rel="noopener"}. See the [`NORTHTool` reference](https://fairmat-nfdi.github.io/nomad-docs/reference/config.html#northtool){:target="_blank" rel="noopener"} for the full field-by-field documentation; the values used here are:

| Field | Value | Meaning |
|---|---|---|
| `image` | `ghcr.io/fairmat-nfdi/nomad-north-mpes-igor:main` | **Placeholder, not a real image** — there is no CI-built target, so this default won't actually pull. It must be overridden via `nomad.yaml` for every deployment, see [Install this Plugin](../how_to/install_this_plugin.md) |
| `file_extensions` | `ipynb`, `nxs`, `h5`, `hdf5` | Which uploaded files show **mpes-igor** in NORTH's tool launcher; primarily works on NeXus files |
| `default_url` | `/desktop` | Opens straight into the `xfce` desktop session |
| `mount_path` | `/home/jovyan` | Where the triggering upload is mounted inside the container |
| `path_prefix` | `lab/tree` | Combined with `with_path`, the URL prefix NORTH uses to build a link straight to the launched file |
| `with_path` | `true` | The specific file that triggered the launch is included in that URL, so NORTH can open directly to it on the JupyterLab side |
| `image_pull_policy` | `Always` | The image is re-pulled on every launch — has no effect for a local-only tag (nothing to pull from), only matters once an image is actually pushed to a registry |
| `privileged` | `false` | Wine and Igor run entirely in userspace at container runtime; nothing here needs elevated container privileges. |
| `display_name` | `mpes-igor` | Name shown in NORTH's tool list |

## Entry point

Registered under `[project.entry-points.'nomad.plugin']` in `pyproject.toml`:

```toml
mpes_igor_north_tool = "nomad_north_mpes_igor.north_tools:mpes_igor"
```

## Base image

The container builds `FROM ghcr.io/fairmat-nfdi/pynxtools-mpes:main` -- the
[`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes){:target="_blank" rel="noopener"} NORTH tool image, not `nomad-north-desktop-base` directly -- so the mpes community-tool stack is already present before Wine/Igor are added on top. See
[Explanation](../explanation/explanation.md) for why.

## Further reading

- [Igor Pro](https://www.wavemetrics.com/){:target="_blank" rel="noopener"} -- WaveMetrics product page (license required)
- [Wine](https://www.winehq.org/){:target="_blank" rel="noopener"} -- project homepage
- [`pynxtools-mpes`](https://github.com/FAIRmat-NFDI/pynxtools-mpes){:target="_blank" rel="noopener"} -- the NORTH tool this image builds on
- [NOMAD Docs > Explanation > NOMAD Remote Tools Hub (NORTH)](https://fairmat-nfdi.github.io/nomad-docs/explanation/north.html){:target="_blank" rel="noopener"}
- [NOMAD Docs > How-to > How to create a NORTH tool](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html){:target="_blank" rel="noopener"}
