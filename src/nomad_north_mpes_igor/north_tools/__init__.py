from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NORTHToolEntryPoint

mpes_igor_north_tool = NORTHTool(
    short_description='Igor Pro (via Wine) on top of the mpes NORTH tool.',
    # Not built or published by public CI: the Igor Wine prefix is a locally-supplied,
    # licensed input that is never committed (see this package's own README). Whoever builds
    # this image should publish it wherever suits their deployment (e.g. an oasis-local
    # registry) and reconfigure this field via `nomad.yaml` — see the NORTH tools how-to.
    image='ghcr.io/fairmat-nfdi/nomad-north-mpes-igor:main',
    description="""### **Igor Pro on the mpes NORTH tool**

    Layers Wine + Igor Pro on top of the `pynxtools-mpes` NORTH tool image, for trARPES data
    reduction workflows that continue in Igor after the Python-based mpes analysis steps.""",
    external_mounts=[],
    file_extensions=['ipynb', 'nxs', 'h5', 'hdf5'],
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[
        {'name': 'Lukas Pielsticker','email': 'lukas.pielsticker@physik.hu-berlin.de'},
        {'name': 'Laurenz Rettig', 'email': 'l.rettig@rptu.de'}
        ],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='mpes-igor',
)

mpes_igor = NORTHToolEntryPoint(
    id_url_safe='mpes-igor',
    north_tool=mpes_igor_north_tool,
)
