# -*- coding: utf-8 -*-
import codecs

import os
from datetime import datetime
import csv

from flask import Blueprint
from werkzeug import secure_filename

from appcore.handler import *
from model.schemas import *


module = Blueprint('upload', __name__)

UPLOAD_FOLDER = "/uploads"

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@module.route('/', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        # if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = UPLOAD_FOLDER + "/" + datetime.now().strftime("%Y/%m/%d/")
        if not os.path.exists(path):
            os.makedirs(path)
        file.save(path + filename)
        return success({})
        # else:
        #     return error(message="File was not allowed", code=400)
    except:
        return error(message="Bad resquest", code=400)





