#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JD Yamokoski'
SITENAME = u'Metal Marionette'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/yamokosk'),
          ('google+', 'https://www.google.com/+JohnYamokoski'),
          ('linkedin', 'https://www.linkedin.com/in/jdyamokoski'),
          ('github', 'https://github.com/yamokosk'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
THEME = 'themes/pelican-bootstrap3'

################################
# Settings in pelican-bootstrap3

# Twitter cards
TWITTER_CARDS = True
USE_OPEN_GRAPH = True

# Twitter timeline
TWITTER_USERNAME = 'yamokosk'
TWITTER_WIDGET_ID = 552890612870291457