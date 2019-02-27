from django.urls import path
from . import views

# paths for forms
urlpatterns = [
    path('', views.index, name='index'),
    path('newPost/', views.newPost, name='newPost')
]
