from django.conf.urls import url
from .views import *


mainurls = [
    url(r'^$',home,name="home-page"),
    url(r'^sling-it$',shorten,name="shorten"),
    url(r'^(?P<short_string>[a-zA-Z1-9]+)$',redirect_url,name="redirect")
]