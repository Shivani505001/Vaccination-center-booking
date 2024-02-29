from django.urls import path, include 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('signup/',views.signup,name='signup'),
   path('admin_login/',auth_views.LoginView.as_view(template_name='userprofile/admin/admin_login.html'),name='admin_login'),#using loginview class for login functionality
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),#using loginview class for login functionality
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),#using logoutview class for logout functionality
    path('myaccount/' ,views.myaccount,name='myaccount'),
    path('admin_details/',views.admin_details,name='admin_details'),
    path('add_center/',views.add_center,name='add_center'),
    path('dosage_details/',views.dosage_details,name='dosage_details'),
    path('delete/<int:center_id>/',views.delete_center,name='delete'),
]