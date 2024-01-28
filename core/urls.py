from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()
router.register(r'purchase-order-viewset', views.PurchaseOrderCreateViewset, basename='purchase_order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('purchase-order/', include('order.urls')),
    path('' ,include(router.urls)),
]
