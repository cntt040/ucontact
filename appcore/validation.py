from flask import request
from appcore.exception import *
from validator import Required, Not, Truthy, Blank, Range, Equals, In, validate, Pattern, Length

def validate_params(rules):
    if not request.json:
        result = validate(rules, request.form)
    else:
        result = validate(rules, request.json)

    if result[0] is not True:
        raise ParamsInvalidate('Params is not validated', errors=result[1])

    return result[0]


