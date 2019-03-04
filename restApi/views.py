from rest_framework import generics

from . import models
from . import serializers


# class UserListView(generics.ListCreateAPIView):
#    queryset = models.CustomUser.objects.all()
#    serializer_class = serializers.UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
