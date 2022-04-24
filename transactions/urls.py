from rest_framework.authtoken import views
from django.urls import path

from .views import TransactionCRUDView
urlpatterns = [
    path('get_transactions/', TransactionCRUDView.as_view()),
    path('add_transaction/', TransactionCRUDView.as_view()),

    path('mark_paid/<int:pk>/', TransactionCRUDView.as_view()),
]