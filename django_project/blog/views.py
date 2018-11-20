from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {'now':now})
    
