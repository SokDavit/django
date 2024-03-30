from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/show/<int:id>', views.show , name='show'),
    path('testing/', views.testing, name='testing'),    

]