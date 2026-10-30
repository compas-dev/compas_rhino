import importlib

import pytest


def test_host_integration_imports():
    pytest.importorskip("Rhino")
    importlib.import_module("compas_rhino.conversions")
