from email.policy import default
from django.contrib import admin
from .models import Page
from language.models import Language
from pageTranslation.models import PageTranslation
from django.http import HttpResponseRedirect
from django.contrib import messages
# Register your models here.

class PageTranslationInline(admin.StackedInline):
    model = PageTranslation
    extra = 1
    max_num = Language.objects.count()
    list_display = ['language','page','title','content']

class PageAdmin(admin.ModelAdmin):
    inlines = [PageTranslationInline,]
    list_display = ['slug','status','sortOrder']

    def changeform_view(self, request, object_id, form_url, context=None):
        context = context or {}
        language = Language.objects.filter(active = "yes")
        context["language"] = language
        label = "add"
        if object_id==None:
            language = Language.objects.filter(active='yes')
            page = Page.objects.all()
            pageTranslation = PageTranslation.objects.all()
            
            if request.method == 'POST':
                slug = request.POST['slug']
                status = request.POST['status']
                sortOrder = request.POST['sortOrder']

                pageData = Page(slug=slug,status=status,sortOrder=sortOrder)
                pageData.save()

                for i in language:                
                    title = request.POST[i.code+'title']
                    content = request.POST[i.code+'content']
                    langcode = request.POST[i.code+'language']
                
                    lang = Language.objects.get(code = langcode)
                    page = Page.objects.get(slug=slug)                    
                    pagetranslationData = PageTranslation(page=page,title=title,content=content,languageCode=lang)
                    pagetranslationData.save()
                messages.success(request,slug+" added successfully")
                return HttpResponseRedirect('/admin/page/page/')

            else:
                    
                context['page'] = Page.objects.filter(status="enabled")
                context['label'] = label
                print(context['page'])
                print(context['label'])
        
        else:
            label = "update"
            page = Page.objects.filter(slug=object_id)
            context['page'] = page
            pageTranslation = PageTranslation.objects.filter(page=object_id)
            context['pageTranslation'] = pageTranslation
            context['label'] = label

            if request.method == 'POST':
                slug = request.POST['slug']
                status = request.POST['status']
                sortOrder = request.POST['sortOrder']

                pageData = Page.objects.filter(slug=slug).update(status=status,sortOrder=sortOrder)
                
                for i in language:
                    ptId = request.POST[i.code+'contentId']
                    title = request.POST[i.code+'title']
                    content = request.POST[i.code+'content']
                    langcode = request.POST[i.code+'language']
                    lang = Language.objects.get(code = langcode)
                    page = Page.objects.get(slug=slug)
                    pagetranslationData = PageTranslation.objects.filter(ptId=ptId).update(page=page,title=title,content=content,languageCode=lang)
                messages.success(request,slug+" updated successfully")
                return HttpResponseRedirect('/admin/page/page/')
        
        return super(PageAdmin,self).changeform_view(request,object_id,form_url,context)

admin.site.register(Page,PageAdmin)

