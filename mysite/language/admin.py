from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name','code','img','default','active']
    readonly_fields = ['img']

    #  Function for displaying thumbnail image
    def img(self,obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:55px;width:90px;">')

admin.site.register(Language,LanguageAdmin)
