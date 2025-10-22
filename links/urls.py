from django.urls import path
from .views import index

# Create your views here.
urlpatterns = [
    path('', index),
]