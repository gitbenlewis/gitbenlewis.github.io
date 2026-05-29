# gitbenlewis.github.io

This repository builds the GitHub Pages documentation hub for
`gitbenlewis.github.io`.

The site is built with Sphinx and `sphinx-rtd-theme`. PyOncoplot documentation is
kept canonical in the sibling `PyOncoplot` repository and copied into this
Sphinx source tree at build time.

## Local Build

```bash
python3 -m pip install -r requirements-docs.txt
python3 scripts/sync_pyoncoplot_docs.py
sphinx-build -W -b html docs _build/html
```

Open `_build/html/index.html` to view the docs hub locally.

## Documentation Sources

- `docs/index.md` is the root docs hub.
- `scripts/sync_pyoncoplot_docs.py` copies `../PyOncoplot/docs` into
  `docs/pyoncoplot`.
- `docs/pyoncoplot` is generated and intentionally ignored by git.
