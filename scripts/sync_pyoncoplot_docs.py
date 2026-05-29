#!/usr/bin/env python3
"""Sync canonical PyOncoplot Markdown docs into the Sphinx source tree."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


TOCTREE = """

```{toctree}
:maxdepth: 2
:caption: PyOncoplot

installation
quickstart
data-inputs
api-reference
options-reference
palettes
metadata-and-tmb
pathways-and-sorting
rendering-backends
gallery
example-plot-source-citations
examples/basic
examples/metadata
examples/brca-gallery
examples/structural-variation-panel
migration-from-ggoncoplot
development
troubleshooting
```
"""

REQUIRED_DOCS = [
    "index.md",
    "installation.md",
    "quickstart.md",
    "data-inputs.md",
    "api-reference.md",
    "options-reference.md",
    "palettes.md",
    "metadata-and-tmb.md",
    "pathways-and-sorting.md",
    "rendering-backends.md",
    "gallery.md",
    "example-plot-source-citations.md",
    "examples/basic.md",
    "examples/metadata.md",
    "examples/brca-gallery.md",
    "examples/structural-variation-panel.md",
    "migration-from-ggoncoplot.md",
    "development.md",
    "troubleshooting.md",
]


def parse_args() -> argparse.Namespace:
    site_root = Path(__file__).resolve().parents[1]
    default_source = Path(
        os.environ.get("PYONCOPLOT_REPO", site_root.parent / "PyOncoplot")
    )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        help="Path to the PyOncoplot repository.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=site_root / "docs" / "pyoncoplot",
        help="Destination inside this Sphinx source tree.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_docs = args.source / "docs"
    dest = args.dest

    if not source_docs.is_dir():
        raise SystemExit(f"PyOncoplot docs directory not found: {source_docs}")

    missing_docs = [
        relative_path
        for relative_path in REQUIRED_DOCS
        if not (source_docs / relative_path).is_file()
    ]
    if missing_docs:
        missing_list = ", ".join(missing_docs)
        raise SystemExit(f"PyOncoplot docs are missing required pages: {missing_list}")

    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source_docs, dest)

    index_path = dest / "index.md"
    index_text = index_path.read_text(encoding="utf-8")
    if "```{toctree}" not in index_text:
        index_path.write_text(index_text.rstrip() + TOCTREE, encoding="utf-8")

    print(f"Synced PyOncoplot docs from {source_docs} to {dest}")


if __name__ == "__main__":
    main()
