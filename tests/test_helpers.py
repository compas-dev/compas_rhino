import pytest

import compas_rhino


def test_default_and_explicit_rhino_versions():
    assert compas_rhino._check_rhino_version(None) == "8.0"
    assert compas_rhino._check_rhino_version("7.0") == "7.0"


def test_unsupported_rhino_version():
    with pytest.raises(Exception, match="Unsupported Rhino version"):
        compas_rhino._check_rhino_version("unsupported")


def test_unload_modules(monkeypatch):
    import sys
    from types import ModuleType

    monkeypatch.setitem(sys.modules, "example_host_plugin", ModuleType("example_host_plugin"))
    monkeypatch.setitem(sys.modules, "example_host_plugin.child", ModuleType("example_host_plugin.child"))
    removed = compas_rhino.unload_modules("example_host_plugin")
    assert set(removed) == {"example_host_plugin", "example_host_plugin.child"}
    assert "example_host_plugin" not in sys.modules
    assert "example_host_plugin.child" not in sys.modules
