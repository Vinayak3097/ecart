from django.shortcuts import  render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("tHIS IS MY ABOUT FUNCTION")

def contact(request):
    return HttpResponse("Contact Information:7785789456")

def tracker(request):
    return HttpResponse("Track Id")

def search(request):
    return HttpResponse("Search Information:")

def productView(request):
    return HttpResponse("Product Information:")

def checkout(request):
    return HttpResponse("Checkout Information:")
