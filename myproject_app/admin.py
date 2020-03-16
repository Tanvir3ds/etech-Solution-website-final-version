from django.contrib import admin

# Register your models here.

admin.site.site_header = 'ETECH SOLUTION LTD. '


from . models import HomeCarousel
from . models import HomeAbout
from . models import HomePartner,HomeClient
from . models import HomeServices
from . models import Services
from . models import BlogCategory
from . models import Blog,MessageClient

admin.site.register(HomeCarousel)
admin.site.register(HomeAbout)
admin.site.register(HomePartner)
admin.site.register(HomeServices)
admin.site.register(Services)
admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(HomeClient)


class MessageDetailsView(admin.ModelAdmin):
    list_display = [
        'Name',
        'Email',
        'Subject',
        'created_at',
    
    ]
admin.site.register(MessageClient,MessageDetailsView)

