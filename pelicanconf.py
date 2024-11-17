AUTHOR = "Huy Truong"
SITENAME = "Huy Truong"
SITEURL = "."

PATH = "content/"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = False
# # Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget

SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/huy-cuong-truong/"),
    ("orcid", "https://orcid.org/0009-0006-9079-321X"),
    ("github", "https://github.com/cuongth95/"),
)


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/pelican-mockingbird"

# Whether to display categories on the menu of the template.
DISPLAY_CATEGORIES_ON_MENU = False
