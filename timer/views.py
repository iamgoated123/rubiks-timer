from django.shortcuts import render
from django.http import HttpResponse
from .models import Solve
from .scrambles import scramblegen

# Create your views here.
def timer(request):
    return HttpResponse(scramblegen(20))
