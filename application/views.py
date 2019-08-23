from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from . import models
from . import serializers

#list out the applications 

class ApplicationViewset(viewsets.ModelViewSet):
    queryset = models.ApplicationObj.objects.all()
    serializer_class = serializers.ApplicationSerializer

#seemingly this is where I would try to check if an identical/similar application JSON already exists with
#a given business name and should be updated or not?

    #checker = models.ApplicationObj.objects.filter()
    #applic, new = models.ApplicationObj.objects.get_or_create(data=checker)



#readonly so a user can only see status
class StatusViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.ApplicationObj.objects.all()
    serializer_class = serializers.StatusSerializer


