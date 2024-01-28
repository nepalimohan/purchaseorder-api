from django.shortcuts import render
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