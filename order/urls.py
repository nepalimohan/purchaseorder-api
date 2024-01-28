from django.urls import path
from . import views

urlpatterns = [
    path('', views.PurchaseOrderListAPIView.as_view(), name='purchase_order_list'),
    path('create/', views.PurchaseOrderCreateAPIView.as_view(), name='purchase_order_create'),
]
