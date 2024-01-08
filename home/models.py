from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
     email= models.ForeignKey(User,null = True, on_delete=models.CASCADE, )
     username = models.CharField(max_length=100)
    


# Create your models here.
    
   
    

   


