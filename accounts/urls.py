from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup,name="signup"),
    path('login_user/', views.login_view , name='login_user'),
    path('logout_user/', views.logout_view , name='logout_user'),

    path('signup-employee/', views.signup_employee,name="signup_employee"),
    path('signup-Customer/',views.signup_customer,name="signup_customer"),
    # path('login-employee',views.login_employee,name="login-employee"),
    # path('login-Customer',views.login_Customer,name="login-Customer"),
    path('edit-details/',views.edit_details,name="edit_details"),
    path('profile/',views.profile,name='profile'),
]
