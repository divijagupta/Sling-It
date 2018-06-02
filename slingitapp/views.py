# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.conf import settings
from .models import *
from django.http import Http404,HttpResponseRedirect


import random
import re


def home(request):
	return render(request,"index.html",{})
# Create your views here.

def shorten(request):
	if request.POST["long-url"]:
		if re.match("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",request.POST["long-url"]):
			string=generate(6)
			shorturl=str(settings.MY_URL)+string
			url=UrlTable.objects.create(short_url=shorturl,long_url=request.POST["long-url"])
			return render(request,"result.html",{"new_url":url.short_url})
		else: 
			raise Http404("Wrong url entered")
	else: 
	   raise Http404("Wrong url entered")
		

				
def redirect_url(request,short_string):
	request_url=str(settings.MY_URL)+short_string
	try:
		url=UrlTable.objects.get(short_url=request_url)
		url.active_hits+=url.active_hits
		url.save()
		return redirect(url.long_url)
	except:
		raise Http404("wrong page requested")	






def generate(limit):
	characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx1234567890"
	string_append=""
	for a in range(0,limit):
		string_append+=random.choice(characters)
	return string_append	





