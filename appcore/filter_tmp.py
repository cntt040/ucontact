import time
import datetime


def ctime(s):
    # return time.ctime(s) # datetime.datetime.fromtimestamp(s)
    return datetime.datetime.strptime(time.ctime(s), "%a %b %d %H:%M:%S %Y")

def add_filters(app, filters_list):
    for filter in filters_list:
        app.template_filter(filter['name'])(filter['callback'])
    return app
