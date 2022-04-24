from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    BORROWS = 'b'
    LENDES = 'l'

    TYPE_CHOICES = (
        (BORROWS, "Borrows"),
        (LENDES, "Lendes"),
    )

    PAID = 'p'
    UNPAID = 'u'

    STATUS_CHOICES = (
        (PAID, "paid"),
        (UNPAID, "unpaid"),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    status = models.CharField(default=PAID ,max_length=2, choices=STATUS_CHOICES)
    date = models.DateField()
    reason = models.TextField()
    
    # todo: user should be allowed to delete account
    # improve logic based on bussiness requirements
    from_user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='from_user')
    user_created = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_created')
