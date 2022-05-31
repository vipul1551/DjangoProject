from django.db import models
from language.models import Language
from attribute.models import Attribute
# Create your models here.

def get_lang():
    return Language.objects.get(default='yes')

class AttributeTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language,on_delete = models.CASCADE,null=False,default='EN')
    attribute = models.ForeignKey(Attribute,on_delete = models.CASCADE,null=False)
    name = models.CharField(verbose_name="Attribute Name",max_length=50)

    class Meta:
        verbose_name = "Attribute Translation"
        unique_together = ('language', 'attribute',)