from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name='Blog'),
    path('blogpost/<int:id>', views.blogpost, name='BlogPost')
]