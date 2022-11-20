from rest_framework import serializers
from .models import Movie, Tmdb_Movie, Comment, Genre, Actor, Director
from accounts.models import User

# 특정 영화 상세정보
class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)
    nations = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

# 영화 상세정보
class MovieSerializerTMDB(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Tmdb_Movie
        fields = '__all__'


# 영화 상세항목 리스트
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
        read_only_fields = ('movie', 'user', 'like_users',)

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

# 6. 코멘트 좋아요 구현
class CommentLike(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('like_users',)

# 7. 유저 pk 가져오기, 11. 유저간 팔로우 구현
class UserDetailSerializer(serializers.ModelSerializer):
    
    followings = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True) # 유저 팔로워 수
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'followings', 'followers', 'followings_count', 'followers_count')

# 10. 보고싶어요 구현하기 - 현재 상태 확인 (이미 보고 싶어요 눌렀는지)/ 변경사항 저장
class MovieWant(serializers.ModelSerializer):
    class Meta:
        model = Tmdb_Movie
        fields = ('wantlist',)

