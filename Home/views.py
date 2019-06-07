from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from .models import Services, WhyUs

# Create your views here.

def index(request):
    services = Services.objects.all()
    whyUs = WhyUs.objects.all()
    context = {
        'services': services,
        'whyUs': whyUs
    }

    return render(request, 'home/index.html', context)


def about(request):

    return render(request, 'home/about.html')
