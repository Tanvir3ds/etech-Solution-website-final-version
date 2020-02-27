from django.shortcuts import render, redirect, HttpResponse
from . models import HomeCarousel
from . models import HomeAbout
from . models import HomePartner
from . models import HomeServices

# Create your views here.

def home(request):
    homecarousels = HomeCarousel.objects.all()
    homeabouts = HomeAbout.objects.all()
    homepartners = HomePartner.objects.all()
    homeservices = HomeServices.objects.all()

    return render(request, "index.html", {'homecarousels':homecarousels, 'homeabouts':homeabouts, 'homepartners':homepartners, 'homeservices':homeservices})  

def about(request):
    return render(request, "about.html",)


def services(request):
    return render(request, "service.html",)


def blog(request):
    return render(request, "blog.html",)


def contact(request):
    return render(request, "contact.html",)