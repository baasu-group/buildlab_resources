from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello this my second time printing this msg in django.")

# Create your views here.
