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