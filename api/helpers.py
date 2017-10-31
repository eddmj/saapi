import json
from django.core import exceptions
from .models import Customer


def load_data(filename='seed_data.json', clear_db=False):
    if clear_db == True:
        try:
            Customer.objects.all().delete()
        except Exception as e:
            print(e)
    with open(filename) as data_file:
        data = json.load(data_file)
        for n in data['content']:
            print(n)
            if 'externalReference' in n:
                external_reference = n['externalReference']
            Customer(
                u_id=n['id'],
                name=n['name'],
                balance=n['balance'],
                currency=n['currency'],
                status=n['status'],
                identifiers=n['identifiers'],
                customer_id=n['customerId'],
                external_reference=external_reference
            ).save()


load_data(clear_db=False)