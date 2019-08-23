from django.db import models
import random
from django.contrib.postgres.fields import JSONField
import datetime


   

def default_dict():
    return {'Primary': 'Standin value since jsonfield left blank'}

class ApplicationObj(models.Model):

   name = models.CharField(max_length=100, null=True)

   #this field will seemingly take up most of the work. Big case of technical debt in
   #the end though.

   data = JSONField(db_index=True,default=default_dict)
   
   created_at = models.DateTimeField(auto_now_add=True)
   




 
	
	
