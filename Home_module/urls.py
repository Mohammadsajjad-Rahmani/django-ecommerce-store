from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home_page'),
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us', views.About_page.as_view(), name='about_page'),
    path('contact', views.contact_page),
    # path('site-header', views.site_header, name='site_header_component')  mishe az in estefade nakard va mostaqiman esm tabe ro bedim chon age user url inja ro pyda kone ba yek sahfe na moratab robero mishe render partial
]
