from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contact_us_page, name='contact-us')
    path('', views.contact_us_view.as_view(), name='contact-us'),
    path('profile', views.profile_file.as_view(), name='profile-url'),
    path('profile-list', views.profile_list.as_view(), name='profile-pics')
]