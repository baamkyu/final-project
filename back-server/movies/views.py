from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Tmdb_Movie, Comment
from .serializers import MovieListSerializer, MovieSerializerTMDB, CommentSerializer, CommentListSerializer, MovieCommentSerializer
from rest_framework import status


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

# 특정 영화에 달린 커멘트 리스트 가져오기
@api_view(['GET'])
def comment_list(request, movie_pk):
    movie=Tmdb_Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        # comments = get_list_or_404(movie)
        serializer = MovieCommentSerializer(movie)
        return Response(serializer.data)

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


# 커멘트 생성 view 함수
@api_view(['POST'])
def comment_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Tmdb_Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
