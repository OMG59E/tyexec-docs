# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import sphinxcontrib.mermaid

project = 'TyExec'
copyright = '2025, IntelliFusion 云天励飞'
author = 'IntelliFusion-Tech'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# myst_parser is incompatible with recommonmark, myst_parser support mermaid.
extensions = ['sphinxcontrib.mermaid', 'recommonmark', 'sphinx_markdown_tables', 'sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# source_parsers = {
#   '.md': CommonMarkParser,
# }
source_suffix = ['.rst', '.md']

# mermaid
mermaid_output_format = 'raw'
mermaid_version = 'latest'