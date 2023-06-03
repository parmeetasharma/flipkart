from rest_framework import serializers
from customer.models import*

class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields="__all__"


class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields="__all__"

class CustomerDetailAddressSerializer(serializers.ModelSerializer):
    customer_Adresses = GetCustomerSerializer(many=True)

    class Meta:
        model = Customers
        fields=('first_name','last_name','age','city','pincode')
