from rest_framework import serializers
from . import models

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrdersItem
        # fields = '__all__'
        exclude = ['grn_status', 'invoice_status', 'new']

        
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True, read_only=True)
    items_write = PurchaseOrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = models.PurchaseOrders
        fields = '__all__'
        # exclude = ['grn_status', 'invoice_status', 'english_cancel_date', 'nepali_cancel_date', 'english_approve_date', 'nepali_approve_date', 'submit_for_approval_nepali_date', 'submit_for_approval_english_date']
        

    def create(self, validated_data):
        items_data = validated_data.pop('items_write', [])
        print(validated_data['supplier'])
        purchase_order = super().create(validated_data)

        for item_data in items_data:
            models.PurchaseOrdersItem.objects.create(orders=purchase_order, **item_data)

        return purchase_order