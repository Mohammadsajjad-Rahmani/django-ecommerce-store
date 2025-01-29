from django.contrib import admin
from . import models


# Register your models here.

class product_admin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['title', 'price', 'is_delete', 'is_active']
    list_editable = ['price', 'is_active']


class product_admin_comment(admin.ModelAdmin):
    list_display = ['autour','is_accepted']


admin.site.register(models.product, product_admin)
admin.site.register(models.product_category)
admin.site.register(models.product_tag)
admin.site.register(models.product_brand)
admin.site.register(models.product_visit)
admin.site.register(models.product_gallery)
admin.site.register(models.productcoment, product_admin_comment)
