from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:slug>/', views.DetailView.as_view(), name='detail'),
    path('kategori/<str:slug>', views.CategoryView.as_view(), name='category'),
]