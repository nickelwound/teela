import os


def env_var(key, default=None, required=False):
    """ Parse environment variable accordingly. """
    if required:
        # Throw KeyError for missing requirements
        val = os.environ[key]
    else:
        # Use default or None
        val = os.environ.get(key, default)

    # Replace booleans
    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    return val


class Config(object):

    """ Configure application with envionment variables. """
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = env_var('DEBUG', default=False)
    SERVER_NAME = env_var('SERVER_NAME', required=True)

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = env_var('CACHE_TYPE', default='simple')
    CACHE_DEFAULT_TIMEOUT = env_var('CACHE_DEFAULT_TIMEOUT', default=60)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db.sqlite' % PROJECT_ROOT
