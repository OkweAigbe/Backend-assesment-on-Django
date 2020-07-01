from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from customer.forms import CusForm
from customer.models import Customer
from customer.serializers import UserSerializer, CustomerSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def customer_list2(request):

    # /cusShow httpResponse/   GET All

      customers = Customer.objects.all()
      customerDict = {'customer' : customers}
      return render(request, 'base.html', customerDict)    


       #Test
   ## if request.method == 'GET':
      ##  customers = Customer.objects.all()
      ##  customers_serializer = CustomerSerializer(customers, many=True)
      ##  return JsonResponse(customers_serializer.data, safe=False)  


def addCus(request):
    form = CusForm()
    if request.method == 'POST':
        form=CusForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)    
    return render(request, 'addcus.html', {'form':form})





class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all()
    serializer_class = UserSerializer


#APIS

@csrf_exempt
def customer_list(request):

    # /cusJson/   GET All

    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)

        

@csrf_exempt
def customer_detail(request, pk):

       # /cusJson with pk/   #Retrive one
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return HttpResponse('customer not found.')   

        if request.method == 'GET':
            customer_serializer = CustomerSerializer(customer)
            return JsonResponse(customer_serializer.data)        




         

@csrf_exempt
def customer_add(request):

    # /cusAdd httpResponse/ ADD One

    if request.method == 'POST':
        customer_data = JSONParser().parser(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
               customer_serializer.save()
               return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)   
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@csrf_exempt
def customer_delete(request):

    # /cusDelete/ Delete one
    if request.method == 'DELETE':
        Customer.objects.get(pk=request.DELETE['pk']).delete()
        return HttpResponse('delete successful')
    return HttpResponse('customer not found')  










