from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),

    path('movies/<int:movie_pk>/comments/', views.comment_list),
    path('comments/', views.all_comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),

    # 6. 코멘트 좋아요 구현
    path('comments/<int:comment_pk>/likes/', views.comment_like),
    
    # 7. 유저 pk 가져오기 & 11. 유저간 팔로우 구현
    path('user/<str:username>/', views.user_detail),
    
    # 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)
    path('movies/<int:movie_pk>/wants/', views.movie_want),

    # 12. 코멘트 삭제하기 구현, 13. 코멘트 수정하기 구현
    path('comments/<int:comment_pk>/edit_delete/', views.comment_edit_del), 
    
    # 14. 영화제 수상작 리스트 가져오기
    path('award/movie/<str:festival>/', views.award_list),

    path('jinheung/movies/', views.jin_movie_list),
]

