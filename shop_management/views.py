from django.http import HttpResponse
from django.shortcuts import render,redirect

def homepage(request):
	# return HttpResponse("homepage")

	return redirect('store')

def about(request):
	# return HttpResponse("about")
	return render(request,"about.html")
