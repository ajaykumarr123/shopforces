from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = (
    # urls for Product
    path('product/list/', views.ProductListView.as_view(), name='product_manager_product_list'),
    path('product/create/', views.ProductCreateView, name='product_manager_product_create'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_manager_product_detail'),
    path('product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_manager_product_update'),
    path('product/delete/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_manager_product_delete'),
    path('success', views.success, name = 'success'),
)
