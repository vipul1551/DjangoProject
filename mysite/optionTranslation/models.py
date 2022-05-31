from django.db import models
from language.models import Language
from option.models import Option
from attribute.models import Attribute
# Create your models here.
def get_lang():
    return Language.objects.get(default='yes')

class OptionTranslation(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language,on_delete = models.CASCADE,null=False,default='EN')
    option = models.ForeignKey(Option,on_delete = models.CASCADE,null=False)
    attribute = models.ForeignKey(Attribute,on_delete = models.CASCADE,null=False,default=None)
    name = models.CharField(verbose_name="Option Name",max_length=50)

    class Meta:
        verbose_name = "Option Translation"
        unique_together = ('language', 'option',)

    def __str__(self):
        return str(self.name) 