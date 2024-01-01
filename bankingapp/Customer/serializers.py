from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from . models import *


class customerRegisterSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only =True)
    bvn = serializers.IntegerField(required = True)
    account_number = serializers.IntegerField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    age = serializers.CharField(required = True)
    address = serializers.CharField(required = True)
    state_of_origin = serializers.CharField(required = True)
    nationality = serializers.CharField(required = True)
    phone_number = serializers.CharField(required = True)
    gender = serializers.CharField(required = True)
    

    def get_cleaned_data(self):
        data = super(customerRegisterSerializer,self).get_cleaned_data()
        extra_data = {
            'bvn':self.validated_data.get('bvn',''),
            'first_name': self.validated_data.get('first_name',''),
            'last_name': self.validated_data.get('last_name',''),
            'age': self.validated_data.get('age',''),
            'address': self.validated_data.get('address',''),
            'state_of_origin': self.validated_data.get('state_of_origin',''),
            'nationality': self.validated_data.get('nationality',''),
            'phone_number': self.validated_data.get('phone_number',''),
            'gender': self.validated_data.get('gender',''),
        }
        data.update(extra_data)
        return data
    
    def save(self, request):
        user = super(customerRegisterSerializer,self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.age = self.cleaned_data.get('age')
        user.address = self.cleaned_data.get('address')
        user.state_of_origin = self.cleaned_data.get('state_of_origin')
        user.nationality = self.cleaned_data.get('nationality')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.gender = self.cleaned_data.get('gender')

        user.save()

        customer = customerAccountProfile(
            user=user,
            bvn = self.cleaned_data.get('bvn'),
        )
        customer.save()
        return user
        
