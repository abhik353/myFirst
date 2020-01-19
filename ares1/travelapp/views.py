from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(requests):

    dests = Destination.objects.all()


    return render(requests,'index.html', {'dests' : dests})
