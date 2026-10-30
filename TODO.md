# Deferred migration work

## COMPAS 3.x

- Migrate imports of removed COMPAS internals such as `compas._os` and audit all
  public geometry and scene API changes against the target COMPAS branch.
- Adapt plugin implementations to COMPAS 3.x plugin signatures and metadata-based
  discovery. Register entry points only once imports are safe outside the host;
  the recovered `__all_plugins__` declarations serve the historical loader.
- Replace backend-specific Brep subclasses with operations on the shared COMPAS Brep class.
- Update curve, surface, NURBS layout, conversion, and scene adapters for COMPAS 3.x.
- Decouple the historical Rhino installer default package list from Grasshopper.
- Set an independent release version and synchronize package `__version__`,
  project metadata, dependency bounds, and release notes when migration is complete.
- Validate a host/Python version matrix compatible with the Python 3.12+ floor;
  historical host constants and installers do not establish current support.

## Validation and documentation

- Run integration tests inside Rhino, covering conversions, scene objects,
  transformations, installation, and plugin registration.
- Migrate archived Sphinx pages and source docstrings to MkDocs-compatible Markdown.
- Expand Ruff coverage to restored sources as they are modernized.
- Configure the eventual Git hosting remote and PyPI trusted publisher, verify
  package-name ownership, and enable the protected `pypi` environment before release.
