from django.db import models
# from tinymce import models as tinymce_models
# from django.urls import reverse

# Create your models here.

# class page(models.Model):
#     pageId = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     slug = models.SlugField(null=True, unique=True)
#     content = tinymce_models.HTMLField()
#     statusChoice = (
#         ('enabled','Enabled'),
#         ('disabled','Disabled'),
#     )
#     status = models.CharField(max_length=10,choices=statusChoice,default='enabled')
#     sortOrder = models.IntegerField(default=0)
    
#     def __str__(self):
#         return str(self.title)   

class Page(models.Model):
    slug = models.SlugField(primary_key=True,unique=True)
    statusChoice = (
        ('enabled','Enabled'),
        ('disabled','Disabled')
    )
    status = models.CharField(max_length=10,choices=statusChoice,default='enabled')
    sortOrder = models.IntegerField(default=0)

    def __str__(self):
        return self.slug
  