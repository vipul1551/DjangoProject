from django.db import models
# Create your models here.

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

    # def __str__(self):
    #     return str(self.code) 

