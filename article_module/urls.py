from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-page'),
    path('cat/<str:category>', views.ArticleListView.as_view(), name='articles-category-list'),
    path('<pk>/', views.ArticleDetailView.as_view(),    name='articles-detail'),
    # havaset be tartib irl tarif kardan bayad bashe masalan age pk/str qable cat / str tarif beshe cat ro be onvane pk mikhone
    path('add-article-comment', views.CreateArticleComment, name='add-article-comment')
]
