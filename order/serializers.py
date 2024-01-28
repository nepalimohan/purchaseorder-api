from rest_framework import serializers
from . import models

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrdersItem
        # fields = '__all__'
        exclude = ['grn_status', 'invoice_status', 'new']

        
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    items_read = PurchaseOrderItemSerializer(many=True, read_only=True)
    items_write = PurchaseOrderItemSerializer(many=True, write_only=True)
    exclude = ['grn_status', 'invoice_status', 'english_cancel_date', 'nepali_cancel_date', 'english_approve_date', 'nepali_approve_date', 'submit_for_approval_nepali_date', 'submit_for_approval_english_date']