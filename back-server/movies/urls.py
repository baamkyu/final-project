from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_list),
    # 특정 영화에 대한 장르, 배우, 감독, 리스트
    path('movies/<int:movie_pk>/details/', views.detail_list),
    path('comments/', views.all_comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]