from django.db import models
from mongoengine import *
connect('testing')

class Test(Document):
    name = StringField(required=True, max_length=255)

class Customer(Document):
    u_id = StringField(null=True)
    name = StringField(null=True)
    balance = FloatField(null=True)
    currency = StringField(null=True)
    status = StringField(null=True)
    identifiers = ListField(null=True)
    customer_id = StringField(null=True)
    external_reference = StringField(null=True)