from django.db import models
from django.contrib.auth.models import User
from .choices import StatusChoices, UsedStatusChoices, VatChoices
# Create your models here.


class PurchaseOrders(models.Model):
	# tenant_id = models.ForeignKey(dashmodel.Tenant, on_delete=models.PROTECT, blank=True, null=True, related_name='tenant_purhcasorders')
	unique_id = models.CharField(max_length=255, default='', null=True, blank=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	supplier = models.CharField(max_length=100, null=True, blank=True)
	#po_date is entry_date for this entry
	po_date = models.CharField(max_length=255, null=True, blank=True)
	validity_till = models.CharField(max_length=255, null=True, blank=True)
	english_po_date = models.CharField(max_length=255, null=True, blank=True)
	english_validity_till = models.CharField(max_length=255, null=True, blank=True)
	# requisition = models.ForeignKey(
	# 	PurchaseRequisition, null=True, blank=True, on_delete=models.SET_NULL
	# )
	non_vatable_amount = models.FloatField(null=True, blank=True, default=0)
	discount_percentage = models.FloatField(null=True, blank=True, default=0)
	vatable_amount = models.FloatField(null=True, blank=True, default=0)
	vat_amount = models.FloatField(null=True, blank=True, default=0)
	grand_total = models.FloatField(null=True, blank=True, default=0)
	status = models.CharField(
		max_length=255,
		choices=StatusChoices.choices,
		null=True,
		blank=True,
		default='draft',
	)
	payment_term = models.CharField(max_length=100, blank=True, null=True)
	entry_by = models.CharField(max_length=255, null=True, blank=True)
	grn_verified = models.BooleanField(default=False)
	invoice_created = models.BooleanField(default=False)
	close = models.BooleanField(default=False)
	narration = models.CharField(max_length=5000, null=True, blank=True, default="")
	approval_user = models.ForeignKey(User, on_delete=models.PROTECT ,null=True, blank=True)
	approved_by = models.CharField(max_length=255, null=True, blank=True)
	cancelled_by = models.CharField(max_length=255, null=True, blank=True)
	english_cancel_date = models.CharField(max_length=255, null=True, blank=True)
	nepali_cancel_date = models.CharField(max_length=255, null=True, blank=True)
	english_approve_date = models.CharField(max_length=255, null=True, blank=True)
	nepali_approve_date = models.CharField(max_length=255, null=True, blank=True)
	submit_for_approval_nepali_date = models.CharField(max_length=255, null=True, blank=True)
	submit_for_approval_english_date = models.CharField(max_length=255, null=True, blank=True)
	grn_status = models.CharField(max_length=50, blank=True, null=True, choices=UsedStatusChoices.choices, default="not used")
	invoice_status = models.CharField(max_length=50, blank=True, null=True, choices=UsedStatusChoices.choices, default="not used")

	class Meta:
		db_table = u'PurchaseOrders'
		ordering = ['-id']

	def __str__(self) -> str:
		return self.unique_id
		# return f"{self.id}"

	# def save(self, *args, **kwargs):
	# 	if self.unique_id == '' or self.unique_id is None:
	# 		self.unique_id = ID.createID("PO", self.tenant_id.tenant_id)
	# 	super().save(*args, **kwargs)


class PurchaseOrdersItem(models.Model):
	orders = models.ForeignKey(
		PurchaseOrders,
		null=True,
		blank=True,
		on_delete=models.PROTECT,
		related_name="items",
	)
	item = models.PositiveIntegerField()
	# requisition_item = models.ForeignKey(PurchaseRequisitionItem, blank=True, null=True, on_delete=models.PROTECT)
	item_code = models.CharField(max_length=255, null=True, blank=True)
	item_name = models.CharField(max_length=255, null=True, blank=True)
	uom = models.CharField(max_length=255, null=True, blank=True)
	quantity = models.FloatField(null=True, blank=True, default=0)
	grn_count = models.FloatField(default=0)
	invoice_count = models.FloatField(default=0)
	rate = models.FloatField(null=True, blank=True, default=0)
	discount = models.FloatField(null=True, blank=True,default=0)
	amount = models.FloatField(null=True, blank=True, default=0)
	vat = models.CharField(choices=VatChoices.choices ,max_length=255, null=True, blank=True, default="non vatable")
	item_total = models.FloatField(null=True, blank=True, default=0)
	new = models.BooleanField(default=False)
	grn_status = models.CharField(max_length=50, blank=True, null=True, choices=UsedStatusChoices.choices, default="not used")
	invoice_status = models.CharField(max_length=50, blank=True, null=True, choices=UsedStatusChoices.choices, default="not used")

	class Meta:
		db_table = u'PurchaseOrdersItem'