from django.db import models

from datetime import *

# Create your models here.


			
class Donation(models.Model):
	"""docstring for ClassName"""
	nickname = models.CharField(max_length=50, verbose_name="Nickname" )
	email = models.CharField(max_length=50, verbose_name="E-mail" )
	text = models.CharField(max_length=300,verbose_name="Text")
	amount=models.FloatField(verbose_name="Amount")

	
	
	class Meta:
		verbose_name= "Donation"
		verbose_name_plural="Donations"
	def __str__(self):
		return 'Donation %s' % self.nickname


class ReqToken(models.Model):
	"""docstring for ClassName"""
	DonationID=models.ForeignKey(Donation)
	key = models.CharField(max_length=25, verbose_name="Key" )
	isUsed= models.BooleanField( verbose_name="isUsed" )
	class Meta:
		verbose_name= "ReqToken"
		verbose_name_plural="ReqTokens"
	def __str__(self):
		return 'ReqToken %s' % self.key


class Request(models.Model):
	"""docstring for ClassName"""
	DonationID=models.ForeignKey(Donation)
	TokenID=models.ForeignKey(ReqToken)
	word = models.CharField(max_length=30, verbose_name="Word" )
	image=models.ImageField(max_length=400,verbose_name="Image")
	pathArray = models.SlugField( verbose_name="PathArray" )
	CurrentStatus = models.CharField(max_length=15, verbose_name="Current Status" )
	class Meta:
		verbose_name= "Request"
		verbose_name_plural="Requests"
	def __str__(self):
		return 'Request %s' % self.word

class Winner(models.Model):
	"""docstring for ClassName"""
	Username = models.CharField(max_length=50, verbose_name="Username" )
	RequestID = models.ForeignKey(Request)
	class Meta:
		verbose_name= "Winner"
		verbose_name_plural="Winners"
	def __str__(self):
		return 'Winner %s' % self.Username
