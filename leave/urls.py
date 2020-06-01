from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'leave'

urlpatterns = [
    path('book/', views.book_leave,name="book-leave"),
    path('view/',views.view_leave,name="view-leave"),
    path('cancel/<id>',views.cancel_view,name="cancel-leave"),
    path('approve/<id>',views.approve_view,name="approve-leave"),
    path('reject/<id>',views.reject_view,name="reject-leave"),
    path('edit_cmts/<id>',views.edit_cmts,name="edit-cmts"),
]
