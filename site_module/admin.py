from django.contrib import admin
from . import models


# Register your models here.

class Footer_link_admin(admin.ModelAdmin):
    list_display = ['title', 'url']


class Slider_admin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['is_active', 'url']


class Site_banner_admin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'position', 'url_title'   ]


admin.site.register(models.site_setting)
admin.site.register(models.footer_links_title)
admin.site.register(models.footer_link, Footer_link_admin)
admin.site.register(models.Slider, Slider_admin)
admin.site.register(models.SiteBanner, Site_banner_admin)
