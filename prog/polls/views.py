from django.shortcuts import render
from polls.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here.
def home(request):
	goods=Good.objects.all()
	context={
	'title':"asdasd",
	'goods':goods,

	}
	return HttpResponse(render_to_string('index.html',context))

def good(request,id):
	goods=Good.objects.get(id=id)
	context={
	'title':"asdasd",
	'goods':goods,

	}
	return HttpResponse(render_to_string('good.html',context))