# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'STEGO.R'
copyright = '2021, Graziella'
author = 'Mullan'

release = '0.1'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube',  # Add this line
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)

html_css_files = [
    'custom.css'
]

html_logo = "logo-removebg-preview_green.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
