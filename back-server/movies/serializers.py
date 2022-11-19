from rest_framework import serializers
from .models import Movie, Tmdb_Movie, Comment, Genre, Actor, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 영화 상세정보
class MovieSerializerTMDB(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'


# 영화 전체 리스트
class MovieListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'

# 전체 커멘트 리스트
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user')

# 특정 영화에 달린 커멘트 리스트 가져오기
class MovieCommentSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True)
    class Meta:
        model = Tmdb_Movie
        fields = ('id', 'comment_set',)

# 전체 장르 리스트
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        models = Genre
        fields = '__all__'

# 전체 배우 리스트
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Actor
        fields = '__all__'

# 전체 감독 리스트
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Director
        fields = '__all__'

# 특정 영화에 대한 장르, 배우, 감독 리스트
class MovieAllInfoSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'genres', 'actors', 'directors',)





