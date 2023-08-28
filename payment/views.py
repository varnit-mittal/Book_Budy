from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import razorpay
from .models import Premium
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()


@login_required(login_url='/login')
def gateway(request):
    context={}
    if request.user.payment==False:
        client=razorpay.Client(auth=(settings.RAZOR_PAY_KEY_ID, settings.RAZOR_KEY_SECRET))

        payment=client.order.create({
            'amount': 60000,
            'currency':'INR',
            'payment_capture':1,
        })

        context['user']=request.user,
        context['payment']=payment

        Premium.objects.create(razorpay_order_id=payment['id'])
    else:
        context['error']=True

    return render(request,'payments/index.html',context=context)

def success(request):
    user=User.objects.get(username=request.user)
    user.payment=True
    user.save()
    order_id=request.GET.get('razorpay_order_id')
    premium_user=Premium.objects.get(razorpay_order_id=order_id)
    premium_user.is_paid=True
    premium_user.save()
    return redirect('/books/home/')