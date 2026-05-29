# gitbenlewis.github.io

This repository builds the GitHub Pages documentation hub for
`gitbenlewis.github.io`.

The site is built with Sphinx and `sphinx-rtd-theme`. Project documentation is
kept canonical in sibling repositories and copied into this Sphinx source tree at
build time.

## Local Build

```bash
python3 -m pip install -r requirements-docs.txt
python3 scripts/sync_project_docs.py
sphinx-build -W -b html docs _build/html
```

Open `_build/html/index.html` to view the docs hub locally.

## Documentation Sources

- `docs/index.md` is the root docs hub.
- `scripts/sync_project_docs.py` stages canonical docs from sibling project
  repositories into generated Sphinx source directories.
- `docs/pyoncoplot`, `docs/adata_science_tools`,
  `docs/single_cell_python_tools`, and `docs/cheatsheets` are generated and
  intentionally ignored by git.
- `docs/_extra/adata-science-tools` contains generated redirects for the old
  adata URL slug.
