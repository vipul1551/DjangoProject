from cProfile import label
from email.policy import default
from django.contrib import admin
from language.models import Language
from .models import Attribute,AttributeTranslation,Option,OptionTranslation
from django.http import HttpResponseRedirect
from django.contrib import messages

# Register your models here.
class attributeTranslationInline(admin.StackedInline):
    model = AttributeTranslation
    extra = 1
    max_num = Language.objects.count()
    list_display = ['language']

class attributeAdmin(admin.ModelAdmin):
    inlines = [attributeTranslationInline,]
    max_num = Language.objects.count()
    list_display = ['code','inputtype','required',]
    # def get_name(self, obj):
    #     return obj.attribute.name
    # get_name.admin_order_field  = 'attribute'  #Allows column order sorting
    # get_name.short_description = 'Attribute Name'  #Renames column head

    def changeform_view(self, request,obj ,form_url,context=None):
        context = context or {}
        language = Language.objects.filter(active='yes').order_by('-default')
        attributes = Attribute.objects.all()
        context["language"]=language
        context["attributes"]=attributes
        label = "add"
        
        if obj==None:
            context['label'] = label
            if request.method == 'POST':
                code = request.POST['code']
                inputType = request.POST['inputtype']
                required = request.POST.get('required')
                if required == 'on':
                    required = True
                else:
                    required = False
                attributeData = Attribute(code=code,inputtype=inputType,required=required)
                attributeData.save()

                for i in language: 
                    name = request.POST[i.code+'name']
                    langcode = request.POST[i.code+'language']
                
                    lang = Language.objects.get(code = langcode)
                    attribute = Attribute.objects.get(code=code)                    
                    attributeTData = AttributeTranslation(attribute=attribute,name=name,language=lang)
                    attributeTData.save()




                # for i in language:  
                #     customOption = request.POST['customOption']
                #     sortOrder = request.POST['sortOrder']
                #     default = request.POST.get('default')
                #     # Optid = Option.objects.get(customOption=customOption)
                #     # if default == 'on':
                #     #     default = 'yes'
                #     # else:
                #     #     default = 'no'                   
                #     optionData = Option(attribute=attribute,customOption=customOption,sortOrder=sortOrder,default=default)
                #     optionData.save()              
                #     optionname = request.POST[i.code+'option']
                #     langcode = request.POST[i.code+'language']
                    
                #     Optid = Option.objects.get(customOption=customOption)
                #     lang = Language.objects.get(code = langcode)
                #     # page = Attribute.objects.get(code=code) 
                    
                #     optionTData = OptionTranslation(id=Optid,name=optionname,language=lang)
                #     optionTData.save()

                # # for i in language:                
                # #     optionname = request.POST[i.code+'option']
                # #     customOption = request.POST['customOption']
                # #     sortOrder = request.POST['sortOrder']
                # #     default = request.POST.get('default')
                # #     Optid = Option.objects.get(customOption=customOption)
                # #     # OptTid = Option.objects.get(customOption=customOption)
                # #     print(Optid)
                # #     lang = Language.objects.get(code = langcode)
                # #     # page = Attribute.objects.get(code=code) 
                # #     if default == 'on':
                # #         default = 'yes'
                # #     else:
                # #         default = 'no'                   
                # #     optionData = Option(id=Optid,customOption=customOption,sortOrder=sortOrder,default=default)
                # #     optionData.save()
                # #     optionTData = OptionTranslation(id=Optid,name=optionname)
                # #     optionTData.save()

                messages.success(request,code+" added successfully")
                return HttpResponseRedirect('/admin/attribute/attribute/')
            else:
                    
                # context['page'] = Page.objects.filter(status="enabled")
                context['label'] = label 

                
        else:                    
            label = "update"
            context['label'] = label   
            attribute = Attribute.objects.filter(id=obj)
            context['attribute'] = attribute
            attributeTranslation = AttributeTranslation.objects.filter(attribute=obj)
            context['attributeTranslation'] = attributeTranslation  
            option = Option.objects.all()
            context['option'] = option
            optionTranslation = OptionTranslation.objects.filter(option=obj)
            context['optionTranslation'] = optionTranslation
            print(option)

            if request.method == 'POST':
                code = request.POST['code']
                inputType = request.POST['inputtype']
                required = request.POST.get('required')
                if required == 'on':
                    required = True
                else:
                    required = False
                attributeData = Attribute.objects.filter(id=obj).update(code=code,inputtype=inputType,required=required)
                
                for i in language:                
                    name = request.POST[i.code+'name']
                    langcode = request.POST[i.code+'language']
                    atId = request.POST[i.code+'nameId']
                    lang = Language.objects.get(code = langcode)
                    attribute = Attribute.objects.get(code=code)   
                    attributeTData = AttributeTranslation.objects.filter(id=atId).update(attribute=attribute,name=name,language=langcode)

                messages.success(request,code+" updated successfully")
                return HttpResponseRedirect('/admin/attribute/attribute/')        
        return super().changeform_view(request, obj ,form_url,context)




class OptionTranslationInline(admin.StackedInline):
    model = OptionTranslation
    extra = 1
    max_num = Language.objects.count()
    list_display = ['language']

class OptionAdmin(admin.ModelAdmin):
    inlines = [OptionTranslationInline,]
    max_num = Language.objects.count()
    list_display = ['customOption','sortOrder','default',]


admin.site.register(Attribute,attributeAdmin)
admin.site.register(Option,OptionAdmin)