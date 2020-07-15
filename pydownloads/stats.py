from .api import API
from .utils import Utils


class Stats(API, Utils):
    def __init__(self, package_name):
        self.response_api = self.request(package_name)

    @property
    def total(self):
        return self.response_data(
            self.response_api, 'total_downloads')
