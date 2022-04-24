from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import UserSerializer

class GetUsers(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    models = User
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return self.models.objects.exclude(id=self.request.user.id)