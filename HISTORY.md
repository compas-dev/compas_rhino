# Extraction history

Upstream: https://github.com/compas-dev/compas

- Removal commit: `7e009ac0dd6b48a120041864308e10b499779ae3`.
- Last source snapshot: `6fb509e1f1a831b9f0832aa3d67309b39cdefc62` (the removal commit's first parent).
- Filtered snapshot: `c79b9b8aeb39b63f550d558c365a64dc12ac2b69`, tagged `compas-extraction`.
- Scope: `src/compas_rhino/`, the upstream license, and host-specific API pages,
  user guides, and images under `docs/`.

All ancestors of the source snapshot were filtered using git-filter-repo 2.47.0.
Commits affecting this scope retain their authors, dates, messages, and surviving
merge relationships. Unrelated commits and empty merges are pruned. Filtering
necessarily changes commit hashes; references inside messages may be rewritten.
Upstream branches and version tags covering all of COMPAS were not imported.
The result is a self-contained Git repository with no alternate object store
and no remote pointing at the original COMPAS repository.

The extraction tag contains the original file layout. A subsequent bootstrap
commit moves historical documentation to `archive/compas-docs` and adds standalone
project files. Package source files remain byte-for-byte identical.

`provenance/commit-map.txt` maps original commit IDs to filtered IDs; zero IDs
identify pruned commits. `provenance/ref-map.txt` records the filtered branch.
`provenance/extraction.json` records every original source file's blob ID and mode.
`git log --follow -- src/compas_rhino/<file>` follows its retained development history.

To reproduce, fetch the source snapshot into a fresh repository and filter:

```bash
git init -b main extraction
git -C extraction fetch --no-tags /path/to/compas 6fb509e1f1a831b9f0832aa3d67309b39cdefc62
git -C extraction reset --hard FETCH_HEAD
cd extraction
git filter-repo --force --path src/compas_rhino/ --path LICENSE \
  --path-glob 'docs/api/compas_rhino*' \
  --path-glob 'docs/userguide/cad.rhino*' \
  --path-glob 'docs/_images/userguide/cad.rhino*' \
  --path docs/_images/rhino_scripteditor.png
git tag compas-extraction
```

No remote repository has been created or published. Add the intended remote after
review, then push `main` and `compas-extraction` explicitly.
