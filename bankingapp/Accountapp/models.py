from django.db import models
from Customer.models import customerAccountProfile


# Create your models here.

class accountDetails(models.Model):
    account_owner = models.OneToOneField(customerAccountProfile, on_delete=models.CASCADE,null =True, blank = True,)
    account_name = models.CharField(max_length=60,null =True, blank = True)
    account_number = models.BigIntegerField (null =True, blank = True)
    account_balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)

    def __str__(self):
        return f'{self.account_name}||{self.account_owner}'



class Transfer(models.Model):
    sender = models.ForeignKey(accountDetails,on_delete=models.CASCADE,null =True, blank = True, related_name='transfers_sent')
    receiver = models.CharField(max_length=10, null =True, blank = True)
    amount = models.IntegerField(null =True, blank = True)
    status = models.CharField(max_length=60, default='PENDING', null =True, blank = True)
    created = models.DateTimeField(auto_now_add=True,null =True, blank = True)

    def __str__(self):
        return f'{self.sender}||{self.receiver}'
    
    def transfer_funds(self):
        completed = 'COMPLETED'
        failed = 'FAILED'
        
        # checking that the receiving account number has a length of 10
        if len(str(self.receiver)) != 10:
            self.status = failed
            error_msg = 'Incorrect receiving account number'
            return {
                'error':error_msg,
                'status': self.status,     
            }

        # checking that the amount is less than or equal to balance
        elif self.amount <= self.sender.account_balance:
            self.sender.account_balance -= self.amount
            new_account_balance = self.sender.account_balance
            self.status = completed
            self.sender.save()  # Save the updated account balance

            # Save the updated status in the Transfer model
            self.save()

            return {
            'new_account_balance': new_account_balance,
            'message':'Transaction Successful',
            'status': self.status,
        }

        # return statement when amount is greater than the balance
        self.status = failed
        self.save()
        error_msg = 'Insufficient funds. Please try again later.'
        return {
            'error':error_msg,
            'status': self.status,     
        }

     
class Airtime(models.Model):
    airtel = 'AIRTEL'
    _9mobile = '9MOBILE' 
    mtn = 'MTN' 
    glo = 'GLO' 
    
    NETWORKS = [
        (airtel,('AIRTEL')),
        (_9mobile,('9MOBILE')),
        (mtn,('MTN')),
        (glo,('GLO'))
    ]

    sender = models.ForeignKey(accountDetails,on_delete=models.CASCADE,null =True, blank = True, related_name='airtime')
    network = models.CharField(max_length=10, choices=NETWORKS,null =True, blank = True)
    receiver = models.CharField(max_length=11, null =True, blank = True)
    amount = models.IntegerField(null =True, blank = True)
    status = models.CharField(max_length=60, default='PENDING', null =True, blank = True)
    created = models.DateTimeField(auto_now_add=True,null =True, blank = True) 

    def __str__(self):
        return f'{self.network}||{self.amount}'


    def buy_airtime(self):
        completed = 'COMPLETED'
        failed = 'FAILED'
        
        # checking that the receiving account number has a length of 11
        if len(str(self.receiver)) != 11:
            self.status = failed
            error_msg = 'Incorrect receiving phone number'
            return {
                'error':error_msg,
                'status': self.status,     
            }

        # checking that the amount is less than or equal to balance
        elif self.amount <= self.sender.account_balance:
            self.sender.account_balance -= self.amount
            new_account_balance = self.sender.account_balance
            self.status = completed
            self.sender.save()  # Save the updated account balance

            # Save the updated status in the Transfer model
            self.save()

            return {
            'amount_purchased':self.amount,
            'new_account_balance':new_account_balance,
            'message':'Transaction Successful',
            'status': self.status,
        }

        # return statement when amount is greater than the balance
        self.status = failed
        self.save()
        error_msg = 'Insufficient funds. Please try again later.'
        return {
            'error':error_msg,
            'status': self.status,     
        }
    
    
            
        

