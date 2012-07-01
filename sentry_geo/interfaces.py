from sentry.interfaces import Interface
from sentry.web.helpers import render_to_string


class Geo(Interface):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def serialize(self):
        return {
            'lat': self.lat,
            'lon': self.lon,
        }

    def to_html(self, event):
        return render_to_string('sentry_geo/partial/interfaces/geo.html', {
            'lat': self.lat,
            'lon': self.lon,
            'show_map': True, # TODO: use actual project settings (are interfaces project-aware?)
        })
