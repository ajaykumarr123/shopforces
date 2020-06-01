from django.conf.urls import url
from django.urls import path,include
from . import views
from rest_framework import routers


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^history/$',views.order_history.as_view(),name='order_list'),
    path('order_detail/<id>',views.order_detail,name='order_detail'),
]
