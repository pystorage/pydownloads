class Error(Exception):
    pass


class ResponseError(Error):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.message)
