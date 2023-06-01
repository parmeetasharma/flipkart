from django.shortcuts import render
from customer.models import*
from customer.serializers import*

from rest_framework import status
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework .permissions import AllowAny,IsAuthenticated

# Create your views here.
class GetCustomerView(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        serializers=GetCustomerSerializer(instance,many=True)
        return Response(serializers.data)
    
    def get(self,request):
          params=request.data
          print("data",params)
          serializers=GetCustomerSerializer(data=params)
          serializers.is_valid(raise_exception=True)
          serializers.save()
          return Response(("message""save successfuly"))   
# Create your views here.
class GetCustomerView(APIView):
    def get(self,request):
        instance=CustomerAddress.objects.all()
        serializers=GetCustomerSerializer(instance,many=True)
        return Response(serializers.data)
    
class CustomerDetailAddress(APIView):
    def get(self,request,pk):
        instance=CustomerAddress.objects.filter(pk)
        serializers=CustomerDetailAddressSerializer(instance,many=True)
        return Response(serializers.data)
    