from django.urls import path
from .views import ip_addresses_view, export_ip_addresses_pdf
urlpatterns = [
    path('ip-addresses/', ip_addresses_view, name='ip_addresses'),
    path('export-ip-addresses/', export_ip_addresses_pdf, name='export_ip_addresses_pdf'),
]
