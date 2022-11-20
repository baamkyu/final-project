from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Tmdb_Movie, Comment
from .serializers import MovieListSerializer, MovieSerializerTMDB, CommentSerializer, CommentListSerializer, MovieCommentSerializer, MovieAllInfoSerializer, CommentLike, UserDetailSerializer, MovieWant
from rest_framework import status
from django.contrib.auth import get_user_model
from accounts.models import User

@api_view(['GET'])
def movie_list(request):
    movies = Tmdb_Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Tmdb_Movie.objects.get(id=movie_pk)
    serializer = MovieSerializerTMDB(movie)
    return Response(serializer.data)

# 특정 영화에 달린 커멘트 리스트 가져오기(GET)/ 커멘트 작성 후저장 (POST)
@api_view(['GET', 'POST'])
def comment_list(request, movie_pk):
    movie=Tmdb_Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        # comments = get_list_or_404(movie)
        serializer = MovieCommentSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 12. 코멘트 삭제하기 구현, 13. 코멘트 수정하기 구현
@api_view(['PUT', 'DELETE'])
def comment_edit_del(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 특정 영화에 대한 장르, 배우, 감독, 리스트
@api_view(['GET'])
def detail_list(request, movie_pk):
    movie = Tmdb_Movie.objects.get(movie_id=movie_pk)
    if request.method == 'GET':
        serialzer = MovieAllInfoSerializer(movie)
        return Response(serialzer.data)
    

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def all_comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


# 6. 코멘트 좋아요 구현
@api_view(['POST', 'GET'])
def comment_like(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method =='POST':
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
    
    serializer = CommentLike(comment)
    return Response(serializer.data)

# 7. 유저 pk 가져오기, 11. 유저간 팔로우 구현
@api_view(['GET', 'POST'])
def user_detail(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)

    if request.method == 'POST':
        if person != request.user.username:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)

    serializer = UserDetailSerializer(person)
    return Response(serializer.data)

# 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)/ 변경사항 저장
@api_view(['POST', 'GET'])
def movie_want(request, movie_pk):
    movie = Tmdb_Movie.objects.get(pk=movie_pk)

    if request.method == 'POST':
        if movie.wantlist.filter(pk=request.user.pk).exists():
            movie.wantlist.remove(request.user)
        else:
            movie.wantlist.add(request.user)
    
    serializer = MovieWant(movie)
    return Response(serializer.data)