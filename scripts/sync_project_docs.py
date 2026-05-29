#!/usr/bin/env python3
"""Stage canonical project docs into this Sphinx source tree."""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote


BRANCH = "main"
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "ftp:")
IMAGE_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
LINK_PATTERN = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
SQL_FENCE_PATTERN = re.compile(r"```sql\n(.*?)```", re.DOTALL)

PYONCOPLOT_TOCTREE = """
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

PYONCOPLOT_DOCS = [
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

ADATA_TOCTREE = """
```{toctree}
:maxdepth: 2
:caption: adata_science_tools

_IO
_column_plots
_corr_dotplots
_diff_test
_expectation_based_covar_correction
_metab_IO
_model_fit
_plots
_plots_depreciated
_row_plots
_simulate_data
_somascan_IO
_utils
_venn_plots
palettes
```
"""

ADATA_DOCS = [
    "README.md",
    "_IO.md",
    "_column_plots.md",
    "_corr_dotplots.md",
    "_diff_test.md",
    "_expectation_based_covar_correction.md",
    "_metab_IO.md",
    "_model_fit.md",
    "_plots.md",
    "_plots_depreciated.md",
    "_row_plots.md",
    "_simulate_data.md",
    "_somascan_IO.md",
    "_utils.md",
    "_venn_plots.md",
    "palettes.md",
]

SINGLE_CELL_TOCTREE = """
```{toctree}
:maxdepth: 2
:caption: single_cell_python_tools

installation
quickstart
DATASET_class
preprocessing-io
preprocessing-qc
preprocessing-transform-data
preprocessing-clustering
plotting
plotting-depreciated
tools-functions-4-scanpy
ingest-verbose
example-notebooks
api-reference
development
troubleshooting
```
"""

SINGLE_CELL_DOCS = [
    "README.md",
    "installation.md",
    "quickstart.md",
    "DATASET_class.md",
    "preprocessing-io.md",
    "preprocessing-qc.md",
    "preprocessing-transform-data.md",
    "preprocessing-clustering.md",
    "plotting.md",
    "plotting-depreciated.md",
    "tools-functions-4-scanpy.md",
    "ingest-verbose.md",
    "example-notebooks.md",
    "api-reference.md",
    "development.md",
    "troubleshooting.md",
]

CHEATSHEETS_TOCTREE = """
```{toctree}
:maxdepth: 2
:caption: Cheatsheets

cheatsheets/github
cheatsheets/conda-environments
cheatsheets/bash
cheatsheets/python
cheatsheets/r
cheatsheets/sql-postgres
```
"""

CHEATSHEET_DOCS = [
    "README.md",
    "cheatsheets/github.md",
    "cheatsheets/conda-environments.md",
    "cheatsheets/bash.md",
    "cheatsheets/python.md",
    "cheatsheets/r.md",
    "cheatsheets/sql-postgres.md",
]


def parse_args() -> argparse.Namespace:
    site_root = Path(__file__).resolve().parents[1]
    parent = site_root.parent

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest-root",
        type=Path,
        default=site_root / "docs",
        help="Sphinx docs source root.",
    )
    parser.add_argument(
        "--pyoncoplot-source",
        type=Path,
        default=Path(os.environ.get("PYONCOPLOT_REPO", parent / "PyOncoplot")),
        help="Path to the PyOncoplot repository.",
    )
    parser.add_argument(
        "--adata-source",
        type=Path,
        default=Path(
            os.environ.get("ADATA_SCIENCE_TOOLS_REPO", parent / "adata_science_tools")
        ),
        help="Path to the adata_science_tools repository.",
    )
    parser.add_argument(
        "--cheatsheets-source",
        type=Path,
        default=Path(
            os.environ.get(
                "GITBENLEWIS_CHEATSHEETS_REPO", parent / "gitbenlewis_cheatsheets"
            )
        ),
        help="Path to the gitbenlewis_cheatsheets repository.",
    )
    parser.add_argument(
        "--single-cell-source",
        type=Path,
        default=Path(
            os.environ.get(
                "SINGLE_CELL_PYTHON_TOOLS_REPO",
                parent / "single_cell_python_tools",
            )
        ),
        help="Path to the single_cell_python_tools repository.",
    )
    return parser.parse_args()


def require_files(root: Path, relative_paths: list[str], label: str) -> None:
    missing_paths = [
        relative_path
        for relative_path in relative_paths
        if not (root / relative_path).is_file()
    ]
    if missing_paths:
        raise SystemExit(f"{label} docs are missing: {', '.join(missing_paths)}")


def copy_project_docs(
    source_root: Path,
    source_docs: Path,
    dest: Path,
    relative_paths: list[str],
    index_source: str,
    toctree: str,
) -> None:
    require_files(source_docs, relative_paths, source_root.name)

    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    for relative_path in relative_paths:
        source_path = source_docs / relative_path
        dest_relative_path = "index.md" if relative_path == index_source else relative_path
        dest_path = dest / dest_relative_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest_path)

    index_path = dest / "index.md"
    index_text = index_path.read_text(encoding="utf-8")
    if "```{toctree}" not in index_text:
        index_path.write_text(index_text.rstrip() + "\n\n" + toctree, encoding="utf-8")


def quote_path(path: Path) -> str:
    return "/".join(quote(part) for part in path.parts)


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def repo_url(repo: str, repo_relative_path: Path, is_image: bool, is_dir: bool) -> str:
    encoded_path = quote_path(repo_relative_path)
    if is_image:
        return f"https://raw.githubusercontent.com/{repo}/{BRANCH}/{encoded_path}"
    if is_dir:
        return f"https://github.com/{repo}/tree/{BRANCH}/{encoded_path}"
    return f"https://github.com/{repo}/blob/{BRANCH}/{encoded_path}"


def rewrite_external_repo_links(
    dest: Path,
    source_root: Path,
    source_docs: Path,
    copied_paths: set[Path],
    repo: str,
) -> None:
    source_root = source_root.resolve()
    source_docs = source_docs.resolve()

    for dest_path in dest.rglob("*.md"):
        source_relative_path = (
            "README.md"
            if dest_path.relative_to(dest) == Path("index.md")
            else dest_path.relative_to(dest).as_posix()
        )
        source_path = (source_docs / source_relative_path).resolve()
        text = dest_path.read_text(encoding="utf-8")

        def replace_link(match: re.Match[str]) -> str:
            bang, label, target = match.groups()
            if target.startswith(EXTERNAL_SCHEMES) or target.startswith("#"):
                return match.group(0)

            target_path, separator, anchor = target.partition("#")
            if not target_path or target_path.startswith("`"):
                return match.group(0)

            source_relative_target = (source_path.parent / target_path).resolve()
            if source_relative_target in copied_paths:
                return match.group(0)

            root_relative_target = (source_root / target_path).resolve()
            if not source_relative_target.exists() and root_relative_target.exists():
                source_relative_target = root_relative_target

            try:
                repo_relative_path = source_relative_target.relative_to(source_root)
            except ValueError:
                return match.group(0)

            is_image = repo_relative_path.suffix.lower() in IMAGE_EXTENSIONS
            rewritten = repo_url(
                repo,
                repo_relative_path,
                is_image=is_image,
                is_dir=source_relative_target.is_dir(),
            )
            if separator:
                rewritten += f"#{anchor}"
            return f"{bang}[{label}]({rewritten})"

        dest_path.write_text(LINK_PATTERN.sub(replace_link, text), encoding="utf-8")


def relax_psql_code_fences(dest: Path) -> None:
    for dest_path in dest.rglob("*.md"):
        text = dest_path.read_text(encoding="utf-8")

        def replace_fence(match: re.Match[str]) -> str:
            block = match.group(1)
            if re.search(r"(?m)^\\", block):
                return f"```text\n{block}```"
            return match.group(0)

        dest_path.write_text(
            SQL_FENCE_PATTERN.sub(replace_fence, text),
            encoding="utf-8",
        )


def sync_pyoncoplot(source_root: Path, dest_root: Path) -> None:
    source_docs = source_root / "docs"
    copy_project_docs(
        source_root,
        source_docs,
        dest_root / "pyoncoplot",
        PYONCOPLOT_DOCS,
        "index.md",
        PYONCOPLOT_TOCTREE,
    )


def sync_adata(source_root: Path, dest_root: Path) -> None:
    source_docs = source_root / "docs"
    remove_path(dest_root / "adata-science-tools")
    dest = dest_root / "adata_science_tools"
    copy_project_docs(
        source_root,
        source_docs,
        dest,
        ADATA_DOCS,
        "README.md",
        ADATA_TOCTREE,
    )
    copied_paths = {(source_docs / relative_path).resolve() for relative_path in ADATA_DOCS}
    rewrite_external_repo_links(
        dest,
        source_root,
        source_docs,
        copied_paths,
        repo="gitbenlewis/adata_science_tools",
    )


def sync_single_cell(source_root: Path, dest_root: Path) -> None:
    source_docs = source_root / "docs"
    dest = dest_root / "single_cell_python_tools"
    copy_project_docs(
        source_root,
        source_docs,
        dest,
        SINGLE_CELL_DOCS,
        "README.md",
        SINGLE_CELL_TOCTREE,
    )
    copied_paths = {
        (source_docs / relative_path).resolve() for relative_path in SINGLE_CELL_DOCS
    }
    rewrite_external_repo_links(
        dest,
        source_root,
        source_docs,
        copied_paths,
        repo="gitbenlewis/single_cell_python_tools",
    )


def sync_cheatsheets(source_root: Path, dest_root: Path) -> None:
    dest = dest_root / "cheatsheets"
    copy_project_docs(
        source_root,
        source_root,
        dest,
        CHEATSHEET_DOCS,
        "README.md",
        CHEATSHEETS_TOCTREE,
    )
    copied_paths = {(source_root / relative_path).resolve() for relative_path in CHEATSHEET_DOCS}
    rewrite_external_repo_links(
        dest,
        source_root,
        source_root,
        copied_paths,
        repo="gitbenlewis/gitbenlewis_cheatsheets",
    )
    relax_psql_code_fences(dest)


def main() -> None:
    args = parse_args()
    sync_pyoncoplot(args.pyoncoplot_source, args.dest_root)
    sync_adata(args.adata_source, args.dest_root)
    sync_single_cell(args.single_cell_source, args.dest_root)
    sync_cheatsheets(args.cheatsheets_source, args.dest_root)
    print(f"Synced project docs into {args.dest_root}")


if __name__ == "__main__":
    main()
