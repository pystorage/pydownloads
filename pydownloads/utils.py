class Utils:
    def response_data(self, data, key):
        if data.status_code == 200:
            return data.json().get(
                key, 'No data available. Data is updated at 01:00 UTC')
        else:
            return data.json().get(
                'message', 'Internal Server Error')
