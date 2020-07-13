import requests


class API:
    URL = 'https://api.pepy.tech/api/v2/projects/{}'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    def request(self, package_name):
        response = requests.get(
            url=self.URL.format(package_name),
            headers=self.HEADERS
        )
        return response
