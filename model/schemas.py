# -*- coding: utf-8 -*-
import time

from appcore.database import *

class Contact(BaseModel):
    full_name = CharField(null=True)
    relationship = CharField(null=True)
    gender = CharField(null=True, default='Nam')
    birthday = CharField(null=True)
    folk = CharField(null=True, default='Kinh')
    address = CharField(null=True)
    number_family = CharField(null=True)
    number_street = CharField(null=True)
    lat = CharField(null=True)
    long = CharField(null=True)
    avatar = TextField(null=True)
    create_time = IntegerField(default=int(time.time()))
    update_time = IntegerField(default=int(time.time()))

