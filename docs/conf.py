from __future__ import annotations


project = "gitbenlewis docs"
author = "Ben Lewis"
copyright = "2026, Ben Lewis"
release = "0.1"

extensions = ["myst_parser"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
root_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
myst_heading_anchors = 3

html_theme = "sphinx_rtd_theme"
html_title = "gitbenlewis docs"
html_baseurl = "https://gitbenlewis.github.io/"
html_extra_path = ["_extra"]
html_show_sourcelink = True
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "titles_only": False,
}

html_context = {
    "display_github": True,
    "github_user": "gitbenlewis",
    "github_repo": "gitbenlewis.github.io",
    "github_version": "main",
    "conf_py_path": "/docs/",
}


EDIT_LINKS = {
    "pyoncoplot/": ("PyOncoplot", "/docs/", None),
    "adata_science_tools/": ("adata_science_tools", "/docs/", {"index": "README"}),
    "single_cell_python_tools/": (
        "single_cell_python_tools",
        "/docs/",
        {"index": "README"},
    ),
    "cheatsheets/": ("gitbenlewis_cheatsheets", "/", {"index": "README"}),
}


def _set_edit_context(app, pagename, templatename, context, doctree):
    context["display_github"] = True
    context["github_user"] = "gitbenlewis"
    context["github_version"] = "main"

    for prefix, (repo, source_path, page_overrides) in EDIT_LINKS.items():
        if not pagename.startswith(prefix):
            continue

        source_page = pagename.removeprefix(prefix)
        if page_overrides:
            source_page = page_overrides.get(source_page, source_page)

        context["github_repo"] = repo
        context["conf_py_path"] = source_path
        context["meta"] = dict(context.get("meta") or {})
        context["meta"]["github_url"] = (
            f"https://github.com/gitbenlewis/{repo}/blob/main"
            f"{source_path.rstrip('/')}/{source_page}"
            f"{context.get('page_source_suffix', '.md')}"
        )
        return


def setup(app):
    app.connect("html-page-context", _set_edit_context)
