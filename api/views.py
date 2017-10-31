from django.shortcuts import render
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import exceptions
import json

# Create your views here.
@api_view(['GET'])
def test_api(request):
    c = Customer.objects.all()
    return Response('Success')
