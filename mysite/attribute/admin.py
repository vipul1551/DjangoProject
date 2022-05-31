from django.contrib import admin
from .models import Attribute
# Register your models here.

class AttributeAdmin(admin.ModelAdmin):
    list_display = ['code','inputtype','required']

admin.site.register(Attribute,AttributeAdmin)
