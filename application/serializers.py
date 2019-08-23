from rest_framework import serializers
from . import models
import random

import datetime

time_0 = datetime.datetime.now()


#the purpose of these will be clear shortly

def minute(timed):
    return round(int(timed.minute))

def is_prime(n):

  #quick little prime test
   if n == 2 or n == 3: return True
   if n < 2 or n%2 == 0: return False
   if n < 9: return True
   if n%3 == 0: return False
   r = int(n**0.5)
   f = 5
   while f <= r:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f +=6
   return True    



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicationObj
        fields = "__all__"
    data = serializers.JSONField()

    #get a value to compare against the database for duplicates
    businessName = serializers.SerializerMethodField(method_name='getName')

    def getName(self,obj):
       return obj.data['Business']['Name']
  

class StatusSerializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField(method_name='approver')
    
    class Meta:
        model = models.ApplicationObj
        fields = ('id','status')

    def approver(self, obj):
	
       result="Rejected"
       #it'll only be approved if the creation time (rounded to the nearest minute) was prime!
       if is_prime(minute(obj.created_at)):
          result = "Approved"
       return result


