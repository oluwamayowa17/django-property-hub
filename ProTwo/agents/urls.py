from django.urls import path
from agents import views

app_name = 'agents'

urlpatterns =[
    path('register/', views.register, name='register'),  
    path('login/', views.user_login, name='user_login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add-location/', views.add_location, name='add_location'),
    path('add-property/', views.add_property, name='add_property'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('delete-prop/<int:property_id>/', views.delete_property, name='delete_property'),
    path('edit-property/<int:property_id>/', views.edit_property, name='edit_property'),
      
] 
