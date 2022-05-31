from django.contrib import admin
from optionTranslation.models import OptionTranslation
from language.models import Language
from option.models import Option
# Register your models here.

class OptionTranslationInline(admin.StackedInline):
    model = OptionTranslation
    extra = 1
    max_num = Language.objects.count()
    list_display = ['language']

class OptionAdmin(admin.ModelAdmin):
    inlines = [OptionTranslationInline,]
    max_num = Language.objects.count()
    list_display = ['customOption','sortOrder','default',]

admin.site.register(Option,OptionAdmin)