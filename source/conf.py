# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../sphinx'))

from datetime import datetime


# -- Project information -----------------------------------------------------

project = 'COUNTER Code of Practice Release 5'
copyright = '2017-%d, COUNTER' % datetime.now().year
author = 'COUNTER'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '5.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '3.5.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'rstFlatTable'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [ ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

rst_prolog = '''
    .. |br| raw:: html

       <br />
    .. |lb| raw:: latex

       {\linebreak}
    .. |clearpage| raw:: latex

       {\clearpage}
    .. |blscape| raw:: latex

       \\begin{landscape}
    .. |elscape| raw:: latex

       \\end{landscape}
'''

today_fmt = '%d %b %Y'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
try:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
except ImportError:
    sys.stderr.write('Warning: sphinx_rtd_theme not found, using default.\n');
    html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': 3,
    'logo_only': True,
    'display_version': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_css_files = [ 'css/custom.css' ]
html_logo = '_static/img/counter-logo.png'
html_secnumber_suffix = ' '
html_show_sourcelink = False


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'COUNTER_Code_of_Practice_R5'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    'preamble': r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}

        \usepackage{titlesec}
        \newcommand\sectionbreak{\clearpage}
        \usepackage{pdflscape}

        \usepackage{datetime}
        \newdateformat{ddmonthyyyy}{\THEDAY\ \monthname[\THEMONTH] \THEYEAR}

        \setcounter{secnumdepth}{4}

        \renewcommand\sphinxtableofcontents{%
           \pagenumbering{arabic}
           \tableofcontents}

        \usepackage{etoolbox}
        \preto\sphinxatlongtablestart{\begin{small}}
        \appto\sphinxatlongtableend{\end{small}}
        \preto\sphinxattablestart{\begin{small}}
        \appto\sphinxattableend{\end{small}}
        \renewcommand\sphinxtablecontinued[1]{}

        \newlength{\tparskip}
        \setlength{\tparskip}{\parskip}
    ''',
    'maketitle': r'''
        \hypersetup{
            pdftitle={COUNTER Code of Practice Release 5.1},
            pdfauthor={COUNTER}
        }
        \pagenumbering{Roman}
        \begin{titlepage}
            \noindent\rule{\textwidth}{1pt}\par
            \sffamily
            \begin{flushright}
                \vspace{25pt}
                {\Huge \textbf{\color{TitleColor} COUNTER Code of Practice}}\par
                \vspace{10pt}
                {\Huge \textbf{\color{TitleColor} Release 5.1}}\par
                \vspace{50pt}
                {Published: April 2023}\par
                {PDF created: \ddmonthyyyy\today}\par
                \vspace{5pt}
            \end{flushright}
            \noindent\rule{\textwidth}{1pt}\par
            \vspace{30pt}
            \vfill
            \noindent\rule{\textwidth}{1pt}\par
            \vspace{8pt}
            \textbf{\large \color{TitleColor} Abstract}\par
            \vspace{5pt}
            \rmfamily
            {COUNTER’s library and content provider members have contributed to the development of Release 5.1 (R5.1) of the COUNTER Code of Practice.}\par
            {The Code of Practice enables content providers to produce consistent, comparable and credible usage data for their online content. This allows librarians and other interested parties to compare the usage data they receive, and to understand and demonstrate the value of the electronic resources to which they subscribe.}\par
            {Release 5.1 (published April 2023) will become the current Code of Practice and the requirement for COUNTER compliance effective from January 2025.}\par
            \noindent\rule{\textwidth}{1pt}\par
            \vfill
            \setlength{\fboxrule}{1pt}
            \setlength{\fboxsep}{10pt}
            \centering
            \fbox{%
                \begin{minipage}{0.80\textwidth}
                    The Code of Practice is available from the \href{https://www.projectcounter.org/}{COUNTER website} as an interactive code. This online version is the version of record for Release 5 of the Code of Practice.
                \end{minipage}
            }
            \vspace{50pt}
        \end{titlepage}
        \clearpage
    ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'figure_align': 'H',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'COUNTER_Code_of_Practice_R5.tex', 'COUNTER Code of Practice',
     'COUNTER', 'howto'),
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'COUNTER_Code_of_Practice_R5', 'COUNTER Code of Practice',
     author, 'COUNTER_Code_of_Practice_R5', 'COUNTER Code of Practice Release 5.1',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

epub_basename = 'COUNTER_Code_of_Practice_R5'


# -- Extension configuration -------------------------------------------------
