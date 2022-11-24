from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from django.views.generic import ListView
from .models import Event,Contributer
from django.contrib.auth.decorators import login_required
from home.decorators import check_profile
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
from home.views import Alumni_Profile

settings = {'store_id': 'amsku637db11c9a23d', 'store_pass': 'amsku637db11c9a23d@ssl', 'issandbox': True }
sslcz = SSLCOMMERZ(settings)
# Create your views here.
class IndexView(ListView):
    model = Event
    queryset = Event.objects.order_by('-running','-created_on')
    template_name = 'charity_events/index.html'

@csrf_exempt
def event_details(request,id):
    event = Event.objects.get(id=id)
    return render(request,'charity_events/details.html',{'event':event})

@login_required
@check_profile
def add_money(request,id):
    amount = int(request.POST['amount'])
    if amount == 0:
        return HttpResponseBadRequest('Zero can not be a payment amount')
    user_id = request.user.id
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "1234"
    post_body['success_url'] = f'http://127.0.0.1:8000/charity-events/{id}/payment_success/{user_id}/'
    post_body['fail_url'] = f'http://127.0.0.1:8000/charity-events/{id}/'
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = request.user.username
    post_body['cus_email'] = request.user.email
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcz.createSession(post_body) 
    payment_url = response['GatewayPageURL']
    return redirect(payment_url)
    
@csrf_exempt
def payment_success(request,id,user_id):
    amount  = int(float(request.POST['amount']))
    alumni_profile = Alumni_Profile.objects.get(user__id=user_id)
    event = Event.objects.get(id=id)
    print(amount)

    contributer = Contributer(
        alumni= alumni_profile,
        event = event,
        amount=amount,
    )
    contributer.save()
    event.present_amount += amount
    event.save()

    context = {
        'event':event,
        'amount': amount,
        'name': alumni_profile.user,
    }
    return render(request,'charity_events/success_payment.html',context)


