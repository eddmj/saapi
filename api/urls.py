from django.conf.urls import url
from .views import test_api

urlpatterns = [
    url(r'^test/', test_api, name='test'),
]