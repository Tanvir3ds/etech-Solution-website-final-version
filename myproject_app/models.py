from django.db import models

# Create your models here.

class HomeCarousel(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title

class HomeAbout(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    
    
    def __str__(self):
        return self.title

class HomePartner(models.Model):
    partner_name = models.CharField(max_length=150)
    partner_img = models.ImageField(upload_to='partner')
    
    
    def __str__(self):
        return self.partner_name

class HomeServices(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    img = models.ImageField(upload_to='partner')
    
    
    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='services')
    
    
    def __str__(self):
        return self.title

class BlogCategory(models.Model):
    category= models.CharField(max_length=150)

    def __str__(self):
        return self.category

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='blog')
    category = models.ForeignKey('BlogCategory',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title


class HomeClient(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='partner')
    
    
    def __str__(self):
        return self.name


class MessageClient(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Subject= models.CharField(max_length=150)
    Message= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


