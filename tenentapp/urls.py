from django.urls import path
from . import views

app_name='tenentapp'

urlpatterns = [
    path('',views.tenenthompage,name='tenenthomepage'),
    path('tenent_profile/',views.tenent_profile,name='tenent_profile'),
    path('about_us/',views.about_us,name='about_us'),
    path('property_list/',views.property_list,name='property_list'),
    path('property_detail/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:property_id>/contact/', views.contact_owner, name='contact_owner'),
    path('messages/', views.tenant_messages, name='tenant_messages'),
    path('messages/<int:message_id>/reply/', views.reply_to_owner, name='reply_to_owner'),
    path('property/<int:property_id>/send_message/', views.send_message, name='send_message'),

    path('chatbot_view',views.chatbot_view,name='chatbot_view'),



]