# -*- coding: utf-8 -*-
from flask import Blueprint

from appcore.handler import *
from model.schemas import *

module = Blueprint('ucontact', __name__)


@module.route('/<string:full_name>', methods=['GET'])
def index(full_name=""):
    try:
        full_name = unicode(full_name)
        data = []
        if full_name != "":
            contacts = Contact.select().where(Contact.full_name.contains(full_name))
            print contacts.sql()
            if contacts:
                for c in contacts:
                    temp = {
                        "full_name": c.full_name,
                        "relationship": c.relationship,
                        "birthday": c.birthday,
                        "folk": c.folk,
                        "address": c.address,
                        "number_family": c.number_family,
                        "number_street": c.number_street
                    }
                    data.append(temp)
        return success(data)
    except Exception as e:
        return error("Không tìm thấy thông tin", code=404, errors=e.message)


@module.route('/', methods=['POST'])
def addContact():
    try:
        full_name = params.full_name
        relationship = params.relationship
        birthday = params.birthday
        folk = params.folk
        address = params.address
        number_family = params.number_family
        number_street = params.number_street
        avatar = params.avatar
        lat = params.lat
        long = params.long

        contact = Contact()
        contact.full_name = full_name
        contact.relationship = relationship
        contact.birthday = birthday
        contact.folk = folk
        contact.address = address
        if number_street is not None:
            contact.number_family = number_family
        if number_street is not None:
            contact.number_street = number_street
        if avatar is not None:
            contact.avatar = avatar
        contact.lat = lat
        contact.long = long
        contact.save()
        return success(contact._data)
    except Exception as e:
        return error("Không tìm thấy thông tin", code=404, errors=e.message)


@module.route('/<int:id>', methods=['PUT'])
def editContact():
    try:
        full_name = params.full_name
        relationship = params.relationship
        birthday = params.birthday
        folk = params.folk
        address = params.address
        number_family = params.number_family
        number_street = params.number_street
        avatar = params.avatar
        lat = params.lat
        long = params.long

        contact = Contact()
        contact.full_name = full_name
        contact.relationship = relationship
        contact.birthday = birthday
        contact.folk = folk
        contact.address = address
        if number_street is not None:
            contact.number_family = number_family
        if number_street is not None:
            contact.number_street = number_street
        if avatar is not None:
            contact.avatar = avatar
        contact.lat = lat
        contact.long = long
        contact.save()
        return success(contact._data)
    except Exception as e:
        return error("Không tìm thấy thông tin", code=404, errors=e.message)