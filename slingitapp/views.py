# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.conf import settings
from .models import *
from django.http import Http404,HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

import random
import re


def home(request):
	print request.META.get('REMOTE_ADDR')
	return render(request,"index.html",{})

@csrf_exempt
def shorten(request):
	if request.method=="POST":
		if request.POST["long-url"]:
			if re.match("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",request.POST["long-url"]):
				string=generate(6)
				shorturl=str(settings.MY_URL)+"/"+string
				if UrlTable.objects.filter(short_url=shorturl).exists():
					string=generate(7)
					shorturl=str(settings.MY_URL)+"/"+string
				url=UrlTable.objects.create(short_url=shorturl,long_url=request.POST["long-url"])
				return render(request,"result.html",{"new_url":url.short_url})
			else: 
				messages.error(request, 'Url Entered in wrong format')
				return render(request,"index.html",{})
		else: 
		   messages.error(request, 'No Url entered')
		   return render(request,"index.html",{})
	else: 
		return redirect("home-page")

		

				
def redirect_url(request,short_string):
	request_url=str(settings.MY_URL)+"/"+short_string
	try:
		url=UrlTable.objects.get(short_url=request_url)
		url.active_hits+=1
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





