from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelProfileView.as_view(), name='user-panel'),
    path('edit-profile', views.EditProfileView.as_view(), name='edit-profile-panel'),
    path('change-profile-pass', views.ChangeProfilePassword.as_view(), name='change-profile-password'),
    path('user-basket', views.user_panel_basket, name='user-basket'),
    path('user-order-history', views.order_history.as_view(), name='user-order-history'),
    path('full-order-history/<int:id>', views.full_order_history, name='full-order-history'),
    path('remove-order-detail', views.remove_order_detail, name='remove-order-detail'),
    path('change-order-detail', views.change_order_detail, name='change-order-detail-count')

]
