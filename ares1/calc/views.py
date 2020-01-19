from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(requests):
    return render(requests,'home.html', {'name':'ares'})

def add(requests):

    val1 = int(requests.POST["num1"])
    val2 = int(requests.POST["num2"])

    res = val1+val2

    return render(requests, "result.html", {'result' : res})
