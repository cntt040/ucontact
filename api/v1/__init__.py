from flask import Blueprint, abort, jsonify, request
from appcore.settings import *


module = Blueprint('v4_root', __name__)

@module.route('/', methods=['GET'])
def list():
    return 'hello'

@module.route('/<int:id>', methods=['GET'])
def show(id):
    pass

@module.route('/', methods=['POST'])
def create():
    pass

@module.route('/<int:id>', methods=['PUT'])
def update(id):
    pass

@module.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    pass
