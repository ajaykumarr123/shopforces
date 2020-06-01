from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('store/', views.store, name="store"),
	path('wishlist/', views.view_wishlist, name="wish"),
	path('update_item/', views.updateItem, name="update_item"),

]
