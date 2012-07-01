sentry-geo
==========

A plugin for Sentry which works with geo data. This adds
a ``sentry_geo.interfaces.Geo`` interface which allows you to
draw maps on your event pages.

This is just a hack to see how easy it would be to add custom
interfaces to Sentry via plugins.  Support for additional geo
data types could be added, but this is probably not the ideal
way to write interfaces.


Interface
---------

Geographic points use following interface::

    {
        "sentry_geo.interfaces.Geo": {
            "lat": 12.321,
            "lon": 45.654,
        }
    }


Install
-------

Install the package via ``pip``::

    pip install sentry-geo

Add ``sentry_geo`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'sentry',
        'sentry_geo',
    )

You'll need to add the following lines to your ``urls.py``::

    import sentry_geo
    sentry_geo_static_root = os.path.join(os.path.dirname(sentry_geo.__file__), 'static')

    urlpatterns = patterns('',
        url(r'^_sentry_geo_static/(?P<path>.*)$', generic.static_media,
            kwargs={'root': sentry_geo_static_root},
            name='sentry-geo-static'),
    ) + urlpatterns

I'm still looking for a solution that doesn't involve overwriting ``urls.py.``