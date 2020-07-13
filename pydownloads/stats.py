from .utils import API


class Stats(API):
    def __init__(self, package_name):
        self.package_name = package_name
        self.data = self.request(self.package_name)

    @property
    def total(self):
        if self.data.status_code == 200:
            return self.data.json().get('total_downloads', 'Data not updated, try again later')
        elif self.data.status_code == 404:
            return self.data.json().get('message', None)
