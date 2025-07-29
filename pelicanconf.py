AUTHOR = 'lento'
SITENAME = 'serial experiments lento'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

TIMEZONE = 'Asia/Tokyo'

THEME = "themes/Flex"

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
)

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images']
PROFILE_PICTURE = "profile.png"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Links', 'https://lit.link/en/seriallain3170'),
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/NieA7_3170'),
          ('github', 'https://github.com/SerialLain3170'),
          ('linkedin', 'https://www.linkedin.com/in/so-hasegawa-5aa509169/'),
          ('envelope', 'crosssceneofwindff@gmail.com')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
