from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment


# Create your views here.
def payment_view(request):
    payments = Payment.objects.all()
    return render(request, "payment_check/base.html", {"payments": payments})
