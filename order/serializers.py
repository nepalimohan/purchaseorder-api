import requests
from rest_framework import serializers
# from django.db.models import get_or_create
from . import models

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.PurchaseOrdersItem
		fields = '__all__'
		# exclude = ['grn_status', 'invoice_status', 'new']

		
		
class PurchaseOrderSerializer(serializers.ModelSerializer):
	items = PurchaseOrderItemSerializer(many=True, read_only=True)
	items_write = PurchaseOrderItemSerializer(many=True, write_only=True)

	class Meta:
		model = models.PurchaseOrders
		fields = '__all__'
		# exclude = ['grn_status', 'invoice_status', 'english_cancel_date', 'nepali_cancel_date', 'english_approve_date', 'nepali_approve_date', 'submit_for_approval_nepali_date', 'submit_for_approval_english_date']
		

	def create(self, validated_data):
		items_data = validated_data.pop('items_write', [])
		purchase_order = super().create(validated_data)

		for item_data in items_data:
			models.PurchaseOrdersItem.objects.create(orders=purchase_order, **item_data)

		return purchase_order
	
	def update(self, instance, validated_data):
		items_data = validated_data.pop('items_write', [])
		print(items_data)
		
		for field in validated_data:
			setattr(instance, field, validated_data[field])
		instance.save()
   
		requisition_item_data = instance.items.all()
  
		for requisition_item_data, item_data in zip(requisition_item_data, items_data):
			for item_attr, item_value in item_data.items():
				if item_attr == 'item':
					response = requests.get(f'http://127.0.0.1:8010/stock-item-check/?stock_id={item_value}')
					if not response.status_code == 200:
						raise Exception("Item doesnot exists")

				setattr(requisition_item_data, item_attr, item_value)
			requisition_item_data.save()
		return instance
		