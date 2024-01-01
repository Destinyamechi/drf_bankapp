from django.urls import path
from .views import *

urlpatterns =[
    path('balance/',viewBalanceView.as_view()),
    path('transfer/',transferView.as_view()),
    path('history/',transactionHistoryView.as_view()),
    path('airtime/',airtimeView.as_view()),


]