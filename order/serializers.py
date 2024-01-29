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
		
		for field in validated_data:
			setattr(instance, field, validated_data[field])
		instance.save()
   
		requisition_item_data = instance.items.all()
  
		for requisition_item_data, item_data in zip(requisition_item_data, items_data):
			for item_attr, item_value in item_data.items():
				setattr(requisition_item_data, item_attr, item_value)
			requisition_item_data.save()
		return instance
		
		for item_data in items_data:
			item_instance, created = models.PurchaseOrdersItem.objects.get_or_create(pk=pk, **item_data)
			for field in item_data:
				setattr(item_instance, field, item_data[field])
			item_instance.save()
		
		instance.save()
		return instance
	
	# def update(self, instance, validated_data):
	#     items_data = validated_data.pop('items_write', [])

	#     # Update fields on the PurchaseOrders instance
	#     instance.title = validated_data.get('title', instance.title)
	#     instance.supplier = validated_data.get('supplier', instance.supplier)
	#     # ... other fields ...

	#     # Update related items (PurchaseOrdersItem)
	#     for item_data in items_data:
	#         item_instance = instance.items.filter(item=item_data['item']).first()

	#         if item_instance:
	#             # Update existing item
	#             item_instance.item_code = item_data.get('item_code', item_instance.item_code)
	#             item_instance.item_name = item_data.get('item_name', item_instance.item_name)
	#             # ... other fields ...
	#             item_instance.save()
	#         else:
	#             # Create new item if it doesn't exist
	#             PurchaseOrdersItem.objects.create(orders=instance, **item_data)

	#     # Save the updated PurchaseOrders instance
	#     instance.save()

	#     return instance