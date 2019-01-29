#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Jorna'
SITENAME = 'David Jorna'
#SITEURL = 'http://davidjorna.com'
SITEURL = 'http://localhost:8000' # for development

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Books', '/books'),
         ('Contact', '/contact'),)

THEME = './themes/FlexMod'

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/david-jorna/'),
          ('Github', 'https://github.com/djorna'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../plugins']
PLUGINS = ['pelican_dynamic']

STATIC_PATHS = ['./content/pages']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True