from django.shortcuts import render
from django.http import HttpResponse
from .models import Solve
from .scrambles import scramblegen

# Create your views here.
def timer(request):
    current_scramble=scramblegen(20)
    return render(request, 'timer/template.html', {"current_scramble":current_scramble})
