#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re, os, sys

##############################
# pelican configuration file
##############################

# General theme info


# -----------------------
# SET THIS

# Local viewing:
SITEURL = ''

### # Github hosting
### SITEURL = 'linear-models'

# OK TNX 
# ----------------------


# Destination (hosting dir)
OUTPUT_PATH = 'docs/'



# Site info

SITENAME = u'linear-models'
AUTHOR = u'charlesreid1'
THEME = 'charlesreid1-notes-theme'
PATH = 'content'



# ======================================
# Configure pelican plugin location:
HOME = os.environ.get('HOME')
PLUGIN_PATHS = [HOME+'/codes/pelican-plugins/']

# all the maths
PLUGINS = ['render_math']


# ======================================
# Static content
# 
# css files, images, etc.
# goes in content/img

STATIC_PATHS = ['img']


# =====================================
# HTML/Markdown mixing
# 
# This requires a bit of an explanation.
# Page content can be made 3 ways:
# - Markdown
# - HTML Templates: HTML files that use Jinja templates
# - HTML (raw)
# (images/style files are covered by static content above).

# Don't try to turn HTML files into pages
READERS = {'html': None}


EXTRA_TEMPLATES_PATHS = []


# Markdown:
# --------------------
# 
# Pelican looks for Markdown files in content/ 
# by default. To render Markdown in other directories,
# add them to EXTRA_TEMPLATES_PATHS
EXTRA_TEMPLATES_PATHS.append('content')



# HTML Templates: 
# --------------------

# HTML templates look like normal .html files,
# but with Jinja double-brace {{templates}}.


# The key-value pairs of TEMPLATE_PAGES are the source and destination files.
TEMPLATE_PAGES = {}

# To add template pages in those directories:
#TEMPLATE_PAGES['mynotebook.html'] = 'mynotebook.html'
TEMPLATE_PAGES['splash.html'] = 'index.html'


# Add places to look for templates:
#EXTRA_TEMPLATES_PATHS.append('content')




# Raw HTML:
# --------------------

# Add places to look for raw HTML:
#EXTRA_TEMPLATES_PATHS.append('content')


# ======================================
# Miscellaneous
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
