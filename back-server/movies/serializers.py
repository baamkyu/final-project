from rest_framework import serializers
from .models import Movie, Tmdb_Movie, Comment


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
        read_only_fields = ('movie',)

# 특정 영화에 달린 커멘트 리스트 가져오기
class MovieCommentSerializer(serializers.ModelSerializer):
    comment_set = CommentListSerializer(many=True)
    class Meta:
        model = Tmdb_Movie
        fields = ('id', 'comment_set',)





