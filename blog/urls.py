from django.urls import path

from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('tab/', views.index_tab, name='blog'),
    path('posts/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create_post, name='create_post'),
    path('post/view/<int:id>/', views.post_view, name='post_view'),
    path('post/edit/<int:id>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
]
