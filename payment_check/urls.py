from django.urls import path
from . import views

urlpatterns = [
    path("", views.payment_view, name="payment"),
    path("payment/csv/", views.payment_csv_view, name="payment_csv"),
    path("payment/pdf/", views.payment_pdf_view, name="payment_pdf"),
]
