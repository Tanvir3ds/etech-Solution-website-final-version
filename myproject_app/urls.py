from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    path('services', views.services, name= 'services'),
    path('blog', views.blog, name= 'blog'),
    path('blogview/<id>/', views.blogview, name= 'blogview'),
    path('contact', views.contact, name= 'contact'),
    path('blog/category', views.getCategory, name="category"),
    path('message', views.ClientMessage, name="message"),
    path('serviceview/<id>/', views.serviceview, name= 'serviceview'),

  
]
