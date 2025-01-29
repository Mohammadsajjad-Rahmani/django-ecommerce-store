from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    path('', views.product_list_view.as_view(), name='product_list'),
    path('add-product-comment', views.CreateProductDetailComment, name='add-product-comment'),
    path('cat/<cat>', views.product_list_view.as_view(), name='product-category'),
    # path('<slug:slug>', views.product_detail, name='product_detail')
    path('favorite-product', views.add_favorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.product_detail_view.as_view(), name='product_detail'),
    path('brand/<brand>', views.product_list_view.as_view(), name='product-brand'),
    # path('<int:pk>', views.product_detai_view.as_view(), name='product_detail')

]
