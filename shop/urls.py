from django.urls import path
from . import views

urlpatterns =[
    path('', views.catalogue, name='catalogue'),
    path('acheter/<int:article_id>/', views.acheter, name='acheter'),
]
