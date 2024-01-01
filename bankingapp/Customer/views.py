from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import *

# Create your views here.
class customerRegisterView(RegisterView):
    serializer_class = customerRegisterSerializer
