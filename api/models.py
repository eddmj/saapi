from django.db import models
from mongoengine import *
connect('testing')

class Customer(Document):
    u_id = StringField(null=True)
    name = StringField(null=True)
    balance = DecimalField(null=True, precision=2)
    currency = StringField(null=True)
    customer_status = StringField(null=True)
    identifiers = ListField(null=True)
    customer_id = StringField(null=True)
    external_reference = StringField(null=True)

