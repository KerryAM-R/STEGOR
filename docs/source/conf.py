# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'STEGO.R'
copyright = '2021, Graziella'
author = 'Mullan'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
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

# -- Custom Patched HTML Translator to open links in new tab

from sphinx.writers.html import HTMLTranslator, HTML5Translator
from sphinx.util.docutils import is_html5_writer_available

class PatchedHTMLTranslator(HTML5Translator if is_html5_writer_available() else HTMLTranslator):
    def visit_reference(self, node):
        if 'target' not in node.attributes and 'refuri' in node.attributes:
            node.attributes['target'] = '_blank'
        super(PatchedHTMLTranslator, self).visit_reference(node)

def setup(app):
    app.set_translator('html', PatchedHTMLTranslator)
