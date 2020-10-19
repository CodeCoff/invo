from rest_framework import serializers
from app.models import Items


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('item_name', 'amount', 'min_price', 'max_price')

