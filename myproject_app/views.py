from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . models import HomeCarousel
from . models import HomeAbout
from . models import HomePartner,HomeClient
from . models import HomeServices
from . models import Services
from . models import BlogCategory,Blog,MessageClient
from django.db.models import Q

# Create your views here.


def home(request):
    homecarousels = HomeCarousel.objects.all()
    homeabouts = HomeAbout.objects.all()
    homepartners = HomePartner.objects.all()
    homeservices = HomeServices.objects.all()
    homeclients = HomeClient.objects.all()
    

    return render(request, "index.html", {'homecarousels':homecarousels, 'homeabouts':homeabouts, 'homepartners':homepartners, 'homeservices':homeservices, 'homeclients':homeclients})  

def about(request):
    return render(request, "about.html",)


#Services
def services(request):
    services = Services.objects.all()


    return render(request, "service.html", {'services':services})


def blog(request):
    categorys= BlogCategory.objects.all()
    blogs=Blog.objects.all().order_by('-id') # latest
    recentblogs=Blog.objects.all().order_by('-id')[:5] 
    search =request.GET.get('q')
    if search:
        blogs=blogs.filter(
            Q(title__icontains=search)|
            Q(description__icontains=search)
        )


    
    return render(request, "blog.html",{'categorys':categorys, 'blogs':blogs, 'recentblogs':recentblogs})


def contact(request):
    return render(request, "contact.html",)





def getCategory(request):

    blogs=Blog.objects.all

    return render(request, "categorypost.html",{'blogs':blogs} )


def ClientMessage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        messagesclient= MessageClient(Name= name, Email=email, Subject=subject, Message=message)
        messagesclient.save()
        return redirect ('home')
        
    else:
        return redirect ('home')
        
        
        
    return render(request, "contact.html",)


def serviceview(request, id):
    
    service=Services.objects.get(pk=id)

    
    return render(request, "singleservice.html",{'service':service})



def blogview(request, slug):
 
    q = Blog.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {

        'blog': q
    }
    return render(request, 'singleblog.html', context)