from django.urls import path, include
from . import views

app_name='adminapp'

urlpatterns = [
    path('homepage/',views.hompage,name='homepage'),

    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('homepage1/', views.homepage1, name='homepage1'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_owner/<int:owner_id>/', views.edit_owner, name='edit_owner'),
    path('edit-tenant/<int:tenant_id>/', views.edit_tenant, name='edit_tenant'),
    path('delete_owner/<int:owner_id>/', views.delete_owner, name='delete_owner'),
    path('delete_tenant/<int:tenant_id>/', views.delete_tenant, name='delete_tenant'),
    path('admin/messages/', views.admin_messages, name='admin_messages'),

    path('upload_property/',views.upload_property,name='upload_property'),
]