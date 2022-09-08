from django.urls import path
from . import views

urlpatterns = [
    path('', views.picture_list),
    path('<int:pk>/', views.picture_detail),
    
]