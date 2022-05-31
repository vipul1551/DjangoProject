from django.db import models
from tinymce import models as tinymce_models
from django.db import transaction
# Create your models here.


class Language(models.Model):    
    name = models.CharField(max_length=100)
    code = models.CharField(primary_key=True,max_length=128,unique=True)
    image = models.ImageField(upload_to="images/")
    CHOICES = (
   ('yes', 'Yes'),
   ('no', 'No')
    )
    default = models.CharField(choices=CHOICES, max_length=128,default='no')  
    active = models.CharField(choices=CHOICES, max_length=128,default='yes')  
    
    def __str__(self):
        return self.code

    # Funtion for changing default value to 'NO' for all, when new one is set to default while save    
    def save(self, *args, **kwargs):
        if not self.default:
            return super(Language,self).save(*args, **kwargs)
        with transaction.atomic():
            Language.objects.filter(default='yes').update(default='no')
            return super(Language,self).save(*args, **kwargs)    

     