# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contractor(models.Model):
	name=models.CharField(max_length=20)
	location=models.CharField(max_length=20)
	qualification=models.CharField(max_length=200)
	email=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Foreman(models.Model):
	name=models.CharField(max_length=20)
	location1=models.CharField(max_length=20)
	qualification=models.CharField(max_length=200)
	email=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)

	def __str__(self):
		return self.name

class KYM(models.Model):
	name=models.CharField(max_length=20)
	location2=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=20)

	def __str__(self):
		return self.name

class client(models.Model):
	name=models.CharField(max_length=20)
	location3=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	

	def __str__(self):
		return self.name
