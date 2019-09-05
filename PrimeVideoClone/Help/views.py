from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def help_home(request):
	return render(request, 'Help/home.html')