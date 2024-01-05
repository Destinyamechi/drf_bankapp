from django.shortcuts import render
from .models import *
from  Customer.models import customerAccountProfile
from .serializers import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# Create your views here.
class viewBalanceView(GenericAPIView):
    serializer_class = viewBalanceSerializer
    queryset = accountDetails.objects.all()

    def get(self,request):
        user = customerAccountProfile.objects.get(user=self.request.user)
        details = accountDetails.objects.get(account_owner=user)
        serializer = viewBalanceSerializer(details,many=False)
        return Response(serializer.data)





# transfer View
@method_decorator(never_cache, name='dispatch')
class transferView(APIView):
    serializer_class = TransferSerializer

    def post(self, request):

        # Fetch the accountDetails associated with the logged-in user
        try:
            user_profile = customerAccountProfile.objects.get(user=request.user)
            sender_details = accountDetails.objects.get(account_owner=user_profile)
        except customerAccountProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except accountDetails.DoesNotExist:
            return Response({'error': 'Account details not found'}, status=status.HTTP_404_NOT_FOUND)
        if not sender_details:
            return Response({'error': 'Sender details not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransferSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            transfer_instance = serializer.save(sender=sender_details)
            result = transfer_instance.transfer_funds()

            if 'error' in result:
                # Transfer failed, return an error response
                response_data = {
                'error': result['error'],
                'status': result['status'],
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Transfer successful, return a success response
            response_data = {
                'new_account_balance': result['new_account_balance'],
                'message':result['message'],
                'status': result['status'],
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




# transaction history view
class transactionHistoryView(APIView):
    serializer_class = transactionHistorySerializer

    def get(self,request):
        user = customerAccountProfile.objects.get(user=self.request.user)
        details = accountDetails.objects.get(account_owner=user)
        transaction = Transfer.objects.filter(sender=details).order_by('-created')
        serializer = transactionHistorySerializer(transaction,many=True)
        return Response(serializer.data)



# airtime view
class airtimeView(APIView):
    serializer_class = airtimeSerializer

    def post(self, request, *args, **kwargs):

        # Fetch the accountDetails associated with the logged-in user
        try:
            user_profile = customerAccountProfile.objects.get(user=request.user)
            sender_details = accountDetails.objects.get(account_owner=user_profile)
        except customerAccountProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except accountDetails.DoesNotExist:
            return Response({'error': 'Account details not found'}, status=status.HTTP_404_NOT_FOUND)
        if not sender_details:
            return Response({'error': 'Sender details not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = airtimeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            transfer_instance = serializer.save(sender=sender_details)
            result = transfer_instance.buy_airtime()

            if 'error' in result:
                # Transfer failed, return an error response
                response_data = {
                'error': result['error'],
                'status': result['status'],
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Transfer successful, return a success response
            response_data = {
                'new_account_balance': result['new_account_balance'],
                'amount_purchased':result['amount_purchased'],
                'message':result['message'],
                'status': result['status'],
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



# transaction History View
class transactionHistoryView(APIView):     
    def get(self, request, *args, **kwargs):
        try:
            user_profile = customerAccountProfile.objects.get(user=request.user)
            sender_details = accountDetails.objects.get(account_owner=user_profile)
        except customerAccountProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except accountDetails.DoesNotExist:
            return Response({'error': 'Account details not found'}, status=status.HTTP_404_NOT_FOUND)
        if not sender_details:
            return Response({'error': 'Sender details not found'}, status=status.HTTP_404_NOT_FOUND)
        # Retrieve and order airtime data by date and time

        airtime_data = Airtime.objects.filter(sender=sender_details).order_by('-created')
        airtime_serializer = airtimeSerializer(airtime_data, many=True)

        # Retrieve and order transfer data by date and time
        transfer_data = Transfer.objects.filter(sender=sender_details).order_by('-created')
        transfer_serializer = TransferSerializer(transfer_data, many=True)

        # Combine the data into a single response
        combined_data = {
            'airtime': airtime_serializer.data,
            'transfers': transfer_serializer.data,
        }

        return Response(combined_data, status=status.HTTP_200_OK)

