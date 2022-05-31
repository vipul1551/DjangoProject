from django.db import models,transaction

# Create your models here.
class Option(models.Model):
    id = models.AutoField(primary_key=True)
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