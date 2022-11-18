from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_list),
    path('comments/', views.all_comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
