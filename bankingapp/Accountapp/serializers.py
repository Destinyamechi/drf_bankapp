from rest_framework import serializers
from .models import *

class viewBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountDetails
        fields = ('account_name','account_balance',)
        
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('id', 'receiver', 'amount', 'status','created',)
        read_only_fields = ('status','sender',)

        
        
class airtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airtime
        fields = ('id', 'receiver', 'amount', 'status','network','created',)
        read_only_fields = ('status','sender',)


class transactionHistorySerializer(serializers.ModelSerializer):
    transfers_sent = viewBalanceSerializer(source='sender', read_only = True)
    class Meta:
        model = Transfer
        fields = ('id', 'receiver', 'amount', 'status','transfers_sent','created',)
        


        

    
    