from django import forms

from sentry.plugins import Plugin

import sentry_geo


class GeoOptionsForm(forms.Form):
    show_map = forms.BooleanField(help_text="Show map", required=False)


class GeoPlugin(Plugin):
    author = 'Chris Faulkner'
    author_url = 'http://github.com/faulkner/sentry-geo'
    title = 'Geo'
    conf_title = 'Geo'
    conf_key = 'geo'
    version = sentry_geo.VERSION
    project_conf_form = GeoOptionsForm

    def is_configured(self, project):
        return self.get_option('show_map', project) != None
