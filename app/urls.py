from django.urls import path
from . import views  

urlpatterns = [
     path('',views.home,name='home'),
     path('login/', views.login,name='login'),
     path('list/', views.event_list,name='event_list'),
     path('customer_list/', views.customer_list,name='customer_list'),
     path('create/', views.event_create,name='event_create'),
     path('edit/<int:event_id>/', views.event_edit,name='event_edit'),
     path('delete/<int:event_id>/', views.event_delete, name='event_delete'),
]