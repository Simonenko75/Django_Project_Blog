from django.urls import path

from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('tab/', views.index_tab, name='blog'),
    path('posts/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/view/', views.post_view, name='post_view'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
]