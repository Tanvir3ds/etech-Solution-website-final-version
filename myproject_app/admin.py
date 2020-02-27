from django.contrib import admin

# Register your models here.
from . models import HomeCarousel
from . models import HomeAbout
from . models import HomePartner
from . models import HomeServices

admin.site.register(HomeCarousel)
admin.site.register(HomeAbout)
admin.site.register(HomePartner)
admin.site.register(HomeServices)