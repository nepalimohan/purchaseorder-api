from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers
# Create your views here.


class PurchaseOrderListAPIView(APIView):
    def get(self, request):
        queryset = models.PurchaseOrders.objects.all()
        serializer = serializers.PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PurchaseOrderCreateAPIView(APIView):
    def post(self, request):
        serializer = serializers.PurchaseOrderSerializer(data=request.data)
        
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)