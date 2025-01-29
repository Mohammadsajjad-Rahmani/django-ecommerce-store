from django.contrib import admin
from . import models


# Register your models here.


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'url_title', 'parent']
    list_editable = ['is_active', 'parent', 'url_title']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'slug', 'author', 'date']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        # vaqti article ro save mikonim in function call mishe change : True ham be in mani ke aya article taqir karde ya na
        # vaqti article jadid create mishe change False hast faqat moqe save kardan mishe True
        # obj hamon modelyi hast ke darim
        print('change :', change)
        print('request : ', request.user)
        print('object : ', obj)
        if not change:
            obj.author = request.user
            # vaqti article ro crate mikoni authoresh sabt mishe
        return super().save_model(request, obj, change, form)


class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_date', 'parent']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleComments, ArticleCommentsAdmin)
