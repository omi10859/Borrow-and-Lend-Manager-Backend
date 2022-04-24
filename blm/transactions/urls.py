from tkinter import N
from rest_framework.authtoken import views
from django.urls import path

from .views import TransactionCRUDView
urlpatterns = [
    path('list/', TransactionCRUDView.as_view())
]