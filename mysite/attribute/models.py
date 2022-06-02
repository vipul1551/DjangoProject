from django.db import models,transaction
from language.models import Language
# Create your models here.

def get_lang():
    return Language.objects.get(default='yes')

class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100,unique=True)
    INPUTCHOICES = (
   ('textbox', 'TextBox'),
   ('textarea', 'TextArea'),
   ('boolean', 'Boolean'),
   ('radiobutton', 'RadioButton'),
   ('checkbox', 'CheckBox'),
   ('select', 'Select'),
   ('multiselect', 'MultiSelect')
    )
    inputtype = models.CharField(verbose_name="Input Type",choices=INPUTCHOICES, max_length=100)  
    required = models.BooleanField()  

    def __str__(self):
        return str(self.code) 

class AttributeTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language,on_delete = models.CASCADE,null=False)
    attribute = models.ForeignKey(Attribute,on_delete = models.CASCADE,null=False)
    name = models.CharField(verbose_name="Attribute Name",max_length=50)

    class Meta:
        verbose_name = "Attribute Translation"
        unique_together = ('language', 'attribute',)

    def __str__(self):
        return str(self.name) 

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE,null=False)
    customOption = models.CharField(verbose_name="Custom Option",max_length=100,unique=True)
    sortOrder = models.IntegerField(verbose_name="Sort Order",default=0)
    CHOICES = (
   ('yes', 'Yes'),
   ('no', 'No')
    )
    default = models.CharField(choices=CHOICES,max_length=100,default="no")

    def save(self,*args,**kwargs):
        if not self.default:
            return super(Option, self).save(*args,**kwargs)
        with transaction.atomic():
            Option.objects.filter(
                default="yes").update(default="no")
            return super(Option,self).save(*args,**kwargs)

class OptionTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language,on_delete = models.CASCADE,null=False)
    option = models.ForeignKey(Option,on_delete = models.CASCADE,null=False)
    name = models.CharField(verbose_name="Option Name",max_length=50)

    class Meta:
        verbose_name = "Option Translation"
        unique_together = ('language', 'option',)

    def __str__(self):
        return str(self.name)             