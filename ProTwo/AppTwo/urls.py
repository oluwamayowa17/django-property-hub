from django.urls import path  
from AppTwo import views

app_name = 'AppTwo'
urlpatterns =[
    path('', views.myfunc, name ='myfunc'),
    path('about/',views.AboutView.as_view(), name='myAbout'),
    path('contact/', views.myContact, name='myContact'),
    path('services/', views.myService, name ='myService'),  
    path('properties/', views.myProperties, name ='myProperties'),  
    path('rent/', views.rent, name ='rent'),  
    path('sale/', views.sale, name ='sale'),  
    path('details/<int:property_id>/', views.property_detail, name ='property_detail'),  
]
