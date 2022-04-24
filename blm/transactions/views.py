from statistics import mode
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionSerializer

class TransactionCRUDView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    models = Transaction
    serializer_class = TransactionSerializer
    queryset = models.objects.all()
