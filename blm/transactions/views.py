from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer, TransactionUserSerializer

class TransactionCRUDView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    models = Transaction
    serializer_class = TransactionSerializer

    def get_queryset(self, *args, **kwargs):
        return self.models.objects.filter(user_created=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return TransactionSerializer
        
        return TransactionUserSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_created=self.request.user)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        try:
            # obj = self.models.objects.get(pk='id', user_created=self.request.user)
            obj = self.models.objects.get(pk=self.kwargs.get('pk'))
            obj.status = Transaction.PAID
            obj.save(update_fields=['status'])

            return Response()
        except self.models.DoesNotExist:
            raise Http404