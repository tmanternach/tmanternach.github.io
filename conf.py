# -*- coding: utf-8 -*-

import time

# Data about this site
BLOG_AUTHOR = "Trevor Manternach"
BLOG_TITLE = "Trevor Manternach"
SITE_URL = "https://trevormanternach.com/"
BLOG_EMAIL = "trevor@trevormanternach.com"
BLOG_DESCRIPTION = "This is my personal weblog."

DEFAULT_LANG = "en"
TRANSLATIONS = {
    DEFAULT_LANG: "",
}
TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/archive.html", "Archive"),
        ("/about/", "About"),
        ("/blogroll/", "Blogroll"),
        ("/feed.xml", "RSS feed"),
    ),
}

NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

THEME="trevor-bootblog4"
THEME_COLOR = '#d63900'

THEME_CONFIG = {
    DEFAULT_LANG: {
        'featured_large': False,
        'featured_small': False,
        'featured_on_mobile': True,
        'featured_large_image_on_mobile': True,
        'featured_strip_html': False,
        'sidebar': ''
    }
}

POSTS = (
    ("posts/*.md", "", "post.tmpl"),
    ("posts/*.rst", "", "post.tmpl"),
    ("posts/*.txt", "", "post.tmpl"),
    ("posts/*.html", "", "post.tmpl"),
)
PAGES = (
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
)

TIMEZONE = "America/Denver"
DATE_FORMAT = 'MMM d, yyyy h:mm a'
DATE_FANCINESS = 0

COMPILERS = {
    "rest": ['.rst', '.txt'],
    "markdown": ['.md', '.mdown', '.markdown'],
    "textile": ['.textile'],
    "txt2tags": ['.t2t'],
    "bbcode": ['.bb'],
    "wiki": ['.wiki'],
    "ipynb": ['.ipynb'],
    "html": ['.html', '.htm'],
    "php": ['.php']
}

NEW_POST_DATE_PATH = True
NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

HIDDEN_TAGS = ['mathjax']
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

HIDDEN_CATEGORIES = []

HIDDEN_AUTHORS = ['Guest']

# Allow multiple, comma-separated authors for a post? (Requires theme support, present in built-in themes)
# MULTIPLE_AUTHORS_PER_POST = False

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

RSS_EXTENSION = ".xml"
RSS_FILENAME_BASE = "feed"
ATOM_FILENAME_BASE = "feed"

REDIRECTIONS = [
    ("routing-wireguard-networks-with-ospf-on-linux/", "/2023/11/10/routing-wireguard-networks-with-ospf-on-linux/"),
    ("python-script-to-retrieve-dhcp-leases-from-palo-alto-firewall/", "/2023/11/03/python-script-to-retrieve-dhcp-leases-from-palo-alto-firewall")
    ]


GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'
GITHUB_REMOTE_NAME = 'origin'
GITHUB_COMMIT_SOURCE = True

GALLERIES_USE_THUMBNAIL = False
GALLERIES_DEFAULT_THUMBNAIL = None

IMAGE_FOLDERS = {'images': 'images'}


META_GENERATOR_TAG = False

INDEX_TEASERS = True

INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'
FEED_LINKS_APPEND_QUERY = False

LICENSE = ""

CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> {license}'
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

STRIP_INDEXES = True

PRETTY_URLS = True

MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

FEED_TEASERS = False

SEARCH_FORM = """
 <!-- DuckDuckGo custom search -->
 <form method="get" id="search" action="https://duckduckgo.com/" class="navbar-form pull-left">
 <input type="hidden" name="sites" value="%s">
 <input type="hidden" name="k8" value="#444444">
 <input type="hidden" name="k9" value="#D51920">
 <input type="hidden" name="kt" value="h">
 <input type="text" name="q" maxlength="255" placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
 </form>
 <!-- End of custom search -->
 """ % SITE_URL

TYPES_TO_HIDE_TITLE = ["micro"]

USE_BUNDLES = False

USE_TAG_METADATA = False

WARN_ABOUT_TAG_METADATA = False

GLOBAL_CONTEXT = {}

GLOBAL_CONTEXT_FILLER = []
