from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
     username= models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)


# Create your models here.
    
   
    

   


