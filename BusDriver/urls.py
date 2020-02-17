from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driver/<int:pk>/',views.driver,name = 'driver-page'),
    path('update_driver/<int:pk>/',views.update_driver,name = 'update_driver'),
    path('delete_driver/<int:pk>/',views.delete_driver,name = 'delete_driver'),
    path('create_driver/',views.create_driver,name= 'create_driver'),


    path('bus/<int:pk>/', views.bus, name='bus-page'),
    path('update_bus/<int:pk>/', views.update_bus, name='update_bus'),
    path('delete_bus/<int:pk>/', views.delete_bus, name='delete_bus'),
    path('create_bus/', views.create_bus, name='create_bus'),

]