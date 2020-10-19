from rest_framework import serializers
from app.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'password', 'date_of_creation')