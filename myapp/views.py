from django.shortcuts import render
from django.http import HttpResponse
from pypaystack import Transaction, Customer, Plan
from django.http import JsonResponse
from django.conf import settings
import json
# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {"pk_public" : settings.PAYSTACK_PUBLIC_KEY})

def verify(request, id):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SCRET_KEY)
    response = transaction.verify(id)
    data = JsonResponse(response, safe=False)
    return data