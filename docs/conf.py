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


def _set_edit_context(app, pagename, templatename, context, doctree):
    if pagename.startswith("pyoncoplot/"):
        context["github_repo"] = "PyOncoplot"
        context["conf_py_path"] = "/docs/"
        context["pagename"] = pagename.removeprefix("pyoncoplot/")


def setup(app):
    app.connect("html-page-context", _set_edit_context)
