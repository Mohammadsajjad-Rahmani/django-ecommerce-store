from django.urls import path

from order_module import views

urlpatterns = [
    path('add-to-product-order', views.Add_to_order, name='add-to-product-order'),
]