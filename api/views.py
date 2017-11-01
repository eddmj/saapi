from django.shortcuts import render
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import exceptions
from decimal import Decimal
import json

@api_view(['GET'])
def unauth_id(request, id):
    """Accepts id from URI. Get as unique"""
    try:
        d = Customer.objects.filter(u_id=id)
        list = []
        for c in d:
            content = {
                "id": c.u_id,
                "name": c.name,
                "balance": str(c.balance),
                "currency": c.currency,
                "status": c.customer_status,
                "identifiers": c.identifiers,
                "customerId": c.customer_id,
            }
            if 'external_reference' in c and not None:
                content['externalReference'] = c.external_reference
            list.append(content)
        payload = {'content': list,
                    'size': len(list),
                    'totalSize': '6094',
                    'page': '0',
                    'totalPages': '407'}
        return Response(payload, status=status.HTTP_200_OK)
    except Exception as e:
        content = {
            "status":"failed",
            "reason":"No matching IDs"
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def unauth_custid(request, id):
    """Accepts Customer ID in URI, accepts contains to make it more complicated. Vary id to get more out"""
    try:
        d = Customer.objects.filter(customer_id__contains=id)
        list = []
        for c in d:
            content = {
                "id": c.u_id,
                "name": c.name,
                "balance": str(c.balance),
                "currency": c.currency,
                "status": c.customer_status,
                "identifiers": c.identifiers,
                "customerId": c.customer_id,
            }
            if 'external_reference' in c and not None:
                content['externalReference'] = c.external_reference
            list.append(content)
        payload = {'content': list,
                    'size': len(list),
                    'totalSize': '6094',
                    'page': '0',
                    'totalPages': '407'}
        return Response(payload, status=status.HTTP_200_OK)
    except Exception as e:
        content = {
            "status":"failed",
            "reason":"No matching IDs"
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def unauth_balance(request, balance, op=''):
    """Accepts Balance in URI, accepts contains to make it more complicated. Vary id to get more out"""
    try:
        if op == 'gte':
            d = Customer.objects.filter(balance__gte=Decimal(balance))
        elif op == 'lte':
            d = Customer.objects.filter(balance__lte=Decimal(balance))
        else:
            d = Customer.objects.filter(balance=Decimal(balance))
        list = []
        for c in d:
            content = {
                "id": c.u_id,
                "name": c.name,
                "balance": str(c.balance),
                "currency": c.currency,
                "status": c.customer_status,
                "identifiers": c.identifiers,
                "customerId": c.customer_id,
            }
            if 'external_reference' in c and not None:
                content['externalReference'] = c.external_reference
            list.append(content)
        payload = {'content': list,
                    'size': len(list),
                    'totalSize': '6094',
                    'page': '0',
                    'totalPages': '407'}
        return Response(payload, status=status.HTTP_200_OK)
    except Exception as e:
        content = {
            "status":"failed",
            "reason":"No valid matching balance"
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def unauth_status(request, st):
    """Accepts id from URI. Get as unique"""
    try:
        d = Customer.objects.filter(customer_status=st)
        list = []
        for c in d:
            content = {
                "id": c.u_id,
                "name": c.name,
                "balance": str(c.balance),
                "currency": c.currency,
                "status": c.customer_status,
                "identifiers": c.identifiers,
                "customerId": c.customer_id,
            }
            if 'external_reference' in c and not None:
                content['externalReference'] = c.external_reference
            list.append(content)
        payload = {'content': list,
                    'size': len(list),
                    'totalSize': '6094',
                    'page': '0',
                    'totalPages': '407'}
        return Response(payload, status=status.HTTP_200_OK)
    except Exception as e:
        content = {
            "status":"failed",
            "reason":"No matching status"
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
