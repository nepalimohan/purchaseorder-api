from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



urlpatterns = [
    path('', views.PurchaseOrderListAPIView.as_view(), name='purchase_order_list'),
    path('update/<int:pk>/', views.PurchaseOrderUpdateApiview.as_view(), name='purchase_order_update'),
    # path('create/', views.PurchaseOrderCreateAPIView.as_view(), name='purchase_order_create'),
]
