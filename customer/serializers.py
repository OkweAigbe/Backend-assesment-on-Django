from django.contrib.auth.models import User
from rest_framework import serializers
from customer.models import Customer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('full_name',
                  'email',
                  'date_of_birth',
                  'address'
                  )



