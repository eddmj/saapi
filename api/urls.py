from django.conf.urls import url
from .views import unauth_id, unauth_custid, unauth_balance, unauth_status, register, auth_id, auth_custid, auth_balance, auth_status

urlpatterns = [
    url(r'^api/id/(?P<id>.+)/?/$', unauth_id, name='unauth_id'),
    url(r'^api/customer/(?P<id>.+)/?/$', unauth_custid, name='unauth_custid'),
    url(r'^api/balance/(?P<balance>\d+\.\d{1,2})/op/(?P<op>.+)/?/$', unauth_balance, name='unauth_balance_opt'),
    url(r'^api/balance/(?P<balance>\d{1,})/op/(?P<op>.+)/?/$', unauth_balance, name='unauth_balance_opt'),
    url(r'^api/balance/(?P<balance>\d+\.\d{1,2})/$', unauth_balance, name='unauth_balance'),
    url(r'^api/balance/(?P<balance>\d{1,})/$', unauth_balance, name='unauth_balance'),
    url(r'^api/status/(?P<st>.+)/?/$', unauth_status, name='unauth_status'),
    url(r'^register', register, name='register'),
    url(r'^auth/id/(?P<id>.+)/?/$', auth_id, name='auth_id'),
    url(r'^auth/customer/(?P<id>.+)/?/$', auth_custid, name='auth_custid'),
    url(r'^auth/balance/(?P<balance>\d+\.\d{1,2})/op/(?P<op>.+)/?/$', auth_balance, name='auth_balance_opt'),
    url(r'^auth/balance/(?P<balance>\d{1,})/op/(?P<op>.+)/?/$', auth_balance, name='auth_balance_opt'),
    url(r'^auth/balance/(?P<balance>\d+\.\d{1,2})/$', auth_balance, name='auth_balance'),
    url(r'^auth/balance/(?P<balance>\d{1,})/$', auth_balance, name='auth_balance'),
    url(r'^auth/status/(?P<st>.+)/?/$', auth_status, name='auth_status'),
]