# Register your models here.
from django.contrib import admin
from .models import Sites, SiteData

class PostSite(admin.ModelAdmin):
    ordering = ['site_id']
    list_display = ['site_name', 'site_id' ]
    class Meta:
        model = Sites
admin.site.register(Sites, PostSite)

class PostSiteData(admin.ModelAdmin):

    list_display = [ 'site' , 'record_date' , 'a_value' , 'b_value'  ]
    fieldsets = (
    (("Site"), {'fields': ('site', ) }),
    (("Data Values"), {'fields': ('record_date', 'a_value', 'b_value' )  }),
    )
    class Meta:
        model = Sites
admin.site.register(SiteData, PostSiteData)
