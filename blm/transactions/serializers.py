from rest_framework import serializers

from .models import Transaction
from accounts.serializers import UserSerializer

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        exclude = ('user_created', )

class TransactionUserSerializer(serializers.ModelSerializer):
    user_created = UserSerializer()
    from_user = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
