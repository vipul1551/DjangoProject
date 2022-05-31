from django.db import models
from tinymce import models as tinymce_models
from language.models import Language
from page.models import Page

# Create your models here.
class PageTranslation(models.Model):
    ptId = models.AutoField(primary_key=True)
    page = models.ForeignKey(Page,on_delete = models.CASCADE,null=False,limit_choices_to={'status': 'enabled'})
    languageCode = models.ForeignKey(Language,on_delete = models.CASCADE,null=False,limit_choices_to={'active': 'yes'})
    title = models.CharField(max_length=100)
    content = tinymce_models.HTMLField()

    #For Checking that selected language is unique or not  
    class Meta:
        unique_together = ('languageCode','page',)

    def __str__(self):
        return str(self.page) + " " +str(self.languageCode)