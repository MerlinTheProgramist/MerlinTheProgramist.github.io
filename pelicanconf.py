AUTHOR = 'Merlin'
SITENAME = "Merlin's_portfolio"
SITEURL = ''

PLUGINS = ["pelican_katex"]

THEME = "themes/custom/"

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github',  'https://github.com/MerlinTheProgramist'),
          ('twitter', 'https://x.com/Merlin85994834'),
          )

DEFAULT_PAGINATION = 10

DEFAULT_DATE_FORMAT = '%d-%m-%Y'

IGNORE_FILES = [".#*", "drafts"]

INDEX_SAVE_AS = "Projects.html"

# all articles from the drafts folder get assigned a draft status automaticly
# EXTRA_PATH_METADATA = {
    # "drafts": {"status": "draft"},
# }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
