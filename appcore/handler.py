from flask import jsonify, request


def success(data, message="", status="SUCCESS"):
    return jsonify({'status': status, 'data': data, 'message': message})


def error(message, code=400, errors=None):
    return jsonify({'status': 'ERROR', 'message': message, "errors": errors}), code


# Make params & args binder
def _params():
    class P(object):
        def __getattribute__(self, name):
            return self(name)

        def __call__(self, name, default=None):
            if not request.json:
                return request.form.get(name, default)
            return request.json.get(name, default)

    return P()


def req_data(*_args):
    root_dict = request.json if request.json else request.form
    data = {}
    for key in _args:
        if key in root_dict:
            data[key] = root_dict[key]
    return data


def _args():
    class A(object):
        def __getattribute__(self, name):
            return self(name)

        def __call__(self, name, default=None):
            return request.args.get(name, default)

    return A()


def _headers():
    class H(object):
        def __getattribute__(self, name):
            return self(name)

        def __call__(self, name, default=None):
            return request.headers.get(name, default)

    return H()

# binding params & args
params = _params()
xargs = _args()
headers = _headers()

# unbind unnessecary method
del _params
del _args
del _headers

