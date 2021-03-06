#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '金发萌音'
SITENAME = '金发萌音'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('创梦空间', 'http://python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/coco/aq2004723/medius"

MEDIUS_AUTHORS = {
    '金发萌音': {
        'description': """
            pyhon和闹酱都萌的不要不要的 --by 九条可怜
        """,
        'cover': 'http://7xiate.com1.z0.glb.clouddn.com/d146ed202608066f262b91263a035a15.jpg?imageView2/1/w/1920/h/1380/interlace/0/q/40',
        'image': 'http://7xiate.com1.z0.glb.clouddn.com/1456430471245157.jpg?imageView2/2/w/128/h/128/interlace/0/q/100',
        'links': (('github', 'https://github.com/aq2004723'),
                  ('weibo', 'http://weibo.com/u/1805754061')),
    }
}

MEDIUS_CATEGORIES = {
    'Category Name': {
        'description': 'A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas and dust, and dark matter.',
        'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/NGC_3923_Elliptical_Shell_Galaxy.jpg/220px-NGC_3923_Elliptical_Shell_Galaxy.jpg'
    }
}

DISQUS_SITENAME='hloli'

