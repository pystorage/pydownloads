import datetime
from .exceptions import ResponseError


class Utils:
    def response_data(self, data, key):
        if data.status_code == 200:
            response = data.json().get(key, None)
            if response:
                return response
            else:
                code = 200
                message = 'Key not found'
                raise ResponseError(code, message)
        else:
            code = data.json().get('error', 500)
            message = data.json().get('message', 'Internal Server Error')
            raise ResponseError(code, message)

    def count_downloads(self, data, version=None):
        amount = 0
        for key, value in data.items():
            for key, value in value.items():
                if not version:
                    amount += value
                elif key == version:
                    amount += value
        return amount

    def date_range(self, data, days):
        start_date = datetime.datetime.utcnow() - datetime.timedelta(days=1 + int(days))
        new_data = dict()
        for key, value in data.items():
            date = datetime.datetime(
                *[int(number) for number in key.split('-')])
            if date >= start_date:
                new_data[key] = value
        return new_data
