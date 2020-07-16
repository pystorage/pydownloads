from .api import API
from .utils import Utils


class Stats(API, Utils):
    def __init__(self, package_name):
        self.response_api = self.request(package_name)

    @property
    def total(self):
        try:
            return self.response_data(
                self.response_api, 'total_downloads')
        except Exception as e:
            return e

    @property
    def week(self):
        try:
            return self.count_downloads(
                self.date_range(self.response_data(
                    self.response_api, 'downloads'), 7))
        except Exception as e:
            return e

    @property
    def month(self):
        try:
            return self.count_downloads(
                self.date_range(self.response_data(
                    self.response_api, 'downloads'), 30))
        except Exception as e:
            return e

    def custom_count(self, days, version=None):
        try:
            if days <= 30:
                return self.count_downloads(
                    self.date_range(self.response_data(
                        self.response_api, 'downloads'), int(days)), version)
            else:
                return self.count_downloads(
                    self.date_range(self.response_data(
                        self.response_api, 'downloads'), 30), version)
        except Exception as e:
            return e
