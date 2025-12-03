from django.urls import path
from . import views

app_name='ownerapp'

urlpatterns = [

path('ownerhomepage/',views.ownerhompage,name='ownerhomepage'),

    path('login_or_register1/', views.login_or_register1, name='login_or_register1'),
    path('ohomepage1/', views.ohomepage1, name='ohomepage1'),
    path('upload_property/', views.upload_property, name='upload_property'),
    path('property_list/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),

    path('properties/edit/<int:pk>/', views.edit_property, name='edit_property'),
    path('properties/delete/<int:pk>/', views.delete_property, name='delete_property'),

    path('owner_profile/', views.owner_profile, name='owner_profile'),

    path('rental_contract/',views.rental_contract,name='rental_contract'),


    path('messages/', views.owner_messages, name='owner_messages'),
    path('messages/reply/<int:message_id>/', views.reply_to_tenant, name='reply_to_tenant'),

    path('chatbot/',views.chatbot,name='chatbot'),

    ]
