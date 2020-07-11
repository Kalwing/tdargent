#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup
from pelican_jupyter import liquid as nb_liquid
import pelican_youtube

AUTHOR = 'Thomas Dargent'
SITENAME = 'Thomas Dargent'
SITESUBTITLE = 'Data Scientist'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['content/img']
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Navigation sections and relative URL:
SECTIONS = [
    ('Home', 'index.html'),
    ('Archive', 'archives.html'),
    #('Tags', 'tags.html'),
    ('CV', 'pages/cv.html'),
    ('About', 'pages/about-me.html')
]

MARKUP = ("md", "ipynb")

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = [
    # 'i18n_subsites',
    # 'video_privacy_enhancer',
    nb_markup,
    nb_liquid,
    'similar_posts',
    'simple_footnotes',
    'deadlinks',
    'css-html-js-minify',
    # 'optimize_images',
    # 'gzip_cache',
    'pelican-cite',
    'render_math',
    'readtime',
    'pelican_javascript'
]
IGNORE_FILES = ['.ipynb_checkpoints', 'notebooks']
IPYNB_MARKUP_USE_FIRST_CELL = True
IPYNB_SKIP_CSS=True
IPYNB_NB_SAVE_AS="{slug}.ipynb"
LIQUID_CONFIGS = (
    ("IPYNB_SKIP_CSS", "True", ""),
)

DEADLINK_VALIDATION = True

PUBLICATIONS_SRC = 'content/pub.bib'
# Appearance
THEME = 'themes/moineau'
# DEFAULT_PAGINATION = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
