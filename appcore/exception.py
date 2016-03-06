class RuntimeError(Exception):

    def __init__(self, message, status_code=400, errors={}):
        Exception.__init__(self, message)
        self.status_code = status_code
        self.errors = errors

class ParamsInvalidate(RuntimeError):
    def __init__(self, message, status_code=400, errors={}):
        RuntimeError.__init__(self, 'Params:' +  message, status_code, errors)

class ConnectionError(RuntimeError):
    def __init__(self, message, status_code=400, errors={}):
        RuntimeError.__init__(self, 'Params:' +  message, status_code, errors)
