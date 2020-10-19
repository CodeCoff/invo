from rest_framework import serializers
from app.models import Invoice


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ('company_name', 'amount', 'purchase_date', 'invoice_number')
