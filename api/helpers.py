import json
from django.core import exceptions
from .models import Customer, AbstractUser
import re
from functools import wraps
from rest_framework import status
from rest_framework.response import Response




def load_data(filename='seed_data.json', clear_db=False):
    if clear_db == True:
        try:
            Customer.objects.all().delete()
        except Exception as e:
            print(e)
    with open(filename) as data_file:
        data = json.load(data_file)
        for n in data['content']:
            external_reference = None
            print(n)
            if 'externalReference' in n:
                external_reference = n['externalReference']
            Customer(
                u_id=n['id'],
                name=n['name'],
                balance=n['balance'],
                currency=n['currency'],
                customer_status=n['status'],
                identifiers=n['identifiers'],
                customer_id=n['customerId'],
                external_reference=external_reference
            ).save()

def email_validation(email):
    """
    Email must be in format xx@xx.xx
    """
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return False
    else:
        return True

def password_validation(password):
    """
    Password must be at least 8 characters. Must have at least one letter and one number
    """
    try:
        # Regex - minimum eight characters, at least one letter and one number
        password_validate = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        valid = re.match(password_validate, password)
        return True if valid else False
    except exceptions.ValidationError as e:
        return False
    if len(password) <= 8:
        return False
    elif not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
        return False
    else:
        return True

def is_authenticated(f):
    """Wrapper function to check if the API Key is valid for this user """
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        try:
            AbstractUser.objects.get(token=request.META['HTTP_AUTHORIZATION'])
        except Exception as e:
            payload = {'status':'failed', 'verbose': 'token invalid'}
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)
        return f(request,*args, **kwargs)
    return decorated_function
