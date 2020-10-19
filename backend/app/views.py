from django.shortcuts import render
from rest_framework import viewsets
from .serializers.companySerializer import CompanySerializer
from .serializers.userSerializer import UserSerializer
from .serializers.itemSerializer import ItemSerializer 
from .serializers.invoiceSerializer import InvoiceSerializer
from .models import User, Company, Invoice, Items


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('user_name')
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('company_name')
    serializer_class = CompanySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('item_name')
    serializer_class = ItemSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer