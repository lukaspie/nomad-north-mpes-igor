from importlib.metadata import entry_points


def test_north_tool_entry_point_registered():
    # exercises the actual mechanism NOMAD uses to discover the tool at runtime
    # (pyproject.toml's [project.entry-points.'nomad.plugin']), not just a direct import
    from nomad_north_mpes_igor.north_tools import mpes_igor

    (entry_point,) = entry_points(group='nomad.plugin', name='mpes_igor_north_tool')
    assert entry_point.load() is mpes_igor


def test_north_tool_id_url_safe():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_mpes_igor.north_tools import mpes_igor

    assert mpes_igor.id_url_safe == 'mpes-igor', (
        'NORTHTool entry point has incorrect id_url_safe'
    )


def test_north_tool_metadata():
    from nomad_north_mpes_igor.north_tools import mpes_igor_north_tool

    assert mpes_igor_north_tool.display_name == 'mpes-igor'
    assert mpes_igor_north_tool.default_url == '/desktop'
    assert mpes_igor_north_tool.maintainer, 'NORTHTool must list at least one maintainer'
