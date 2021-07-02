from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    facilities = Facility.objects.all()
    template_name = 'main/home.html'
    return render(request, template_name, {'facilities': facilities})
