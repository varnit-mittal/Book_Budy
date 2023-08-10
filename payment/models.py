from django.db import models

# Create your models here.
class Premium(models.Model):
    is_paid=models.BooleanField(default=False)
    razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razorpay_signature=models.CharField(max_length=100,null=True,blank=True)