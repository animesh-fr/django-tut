from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  # return HttpResponse()
  return render(request,'index.html')

def about(request):
  # return HttpResponse("Hello World. You are at chai aur Django About Page")
  return render(request, 'about.html')

def contact(request):
  # return HttpResponse("Hello World. You are at chai aur Django Contact Page")
  return render(request, 'contact.html')