try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-geo').version
except Exception, e:
    VERSION = 'unknown'
