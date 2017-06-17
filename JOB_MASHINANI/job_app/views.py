# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request,'login.html')

def signin(request):
	return render(request,'signin.html')

def signup(request):
	return render(request,'signup.html')