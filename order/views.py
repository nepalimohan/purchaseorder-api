from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from . import models
from . import serializers
# Create your views here.


class PurchaseOrderListAPIView(APIView):
    def get(self, request):
        queryset = models.PurchaseOrders.objects.all()
        # queryset = models.PurchaseOrders.objects.prefetch_related('items').all()
        serializer = serializers.PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

class PurchaseOrderCreateAPIView(APIView):
    def post(self, request):
        serializer = serializers.PurchaseOrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PurchaseOrderCreateViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    def list(self, request):
        queryset = models.PurchaseOrders.objects.all()
        serializer = serializers.PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = serializers.PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = models.PurchaseOrders.objects.get(pk=pk)
        serializer = serializers.PurchaseOrderSerializer(queryset)
        return Response(serializer.data)
        
