#!/usr/bin/env python3

from datetime import datetime

import guzzle_sphinx_theme

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "guzzle_sphinx_theme",
]

source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.rst"]

project = "Nengo design"
copyright = "2017, Applied Brain Research"
author = "Applied Brain Research"
version = release = datetime.now().strftime("%Y-%m-%d")
language = None

todo_include_todos = True

intersphinx_mapping = {
    "nengo": ("https://nengo.github.io/", None)
}

# HTML theming
pygments_style = "sphinx"
templates_path = ["_templates"]
html_favicon = "general/favicon.ico"
html_static_path = ["_static"]
html_use_smartypants = True

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = "guzzle_sphinx_theme"

html_theme_options = {
    "project_nav_name": "Nengo design",
    "base_url": "https://nengo.github.io/design",
}

# Other builders
htmlhelp_basename = "Nengo design"

latex_elements = {
    # "papersize": "letterpaper",
    # "pointsize": "11pt",
    # "preamble": "",
    # "figure_align": "htbp",
}

latex_documents = [
    (master_doc,  # source start file
     "nengo.tex",  # target name
     "Nengo Design",  # title
     "Applied Brain Research",  # author
     "manual"),  # documentclass
]

man_pages = [
    # (source start file, name, description, authors, manual section).
    (master_doc, "nengo", "Nengo Design", [author], 1)
]

texinfo_documents = [
    (master_doc,  # source start file
     "Nengo",  # target name
     "Nengo Design",  # title
     author,  # author
     "Nengo",  # dir menu entry
     "Design assets for Nengo",  # description
     "Miscellaneous"),  # category
]
