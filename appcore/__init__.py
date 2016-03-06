from flask import Flask, send_file
from appcore import dispatcher
from appcore.handler import *
from appcore.exception import *
from appcore.filter_tmp import *
app = Flask(__name__)

@app.errorhandler(ParamsInvalidate)
def raising_invalid_params(e):
    return error(e.message, e.status_code, errors=e.errors)

@app.errorhandler(ConnectionError)
def raising_database_error(e):
    return error(e.message, e.status_code, errors=e.errors)

@app.errorhandler(RuntimeError)
def raising_runtime_error(e):
    return error(e.message, e.status_code, errors=e.errors)

def create_app():
    application = dispatcher.do(app)
    application = add_filters(application, [{"name": "ctime", "callback": ctime}])
    return application
