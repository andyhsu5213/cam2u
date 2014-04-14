# coding: utf-8
from django.db import models

class Member(models.Model):
	account = models.CharField(max_length=20)
	mail = models.CharField(max_length=40)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.account
