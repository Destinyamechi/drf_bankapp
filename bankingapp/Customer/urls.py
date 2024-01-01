from django.urls import path
from .views import *

urlpatterns = [
    path('register/',customerRegisterView.as_view()),
]