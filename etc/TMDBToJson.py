# 첫 데이터 베이스 세팅 (2004~2022년도 관객수 상위 30개씩에서 조금 더 필터링)

import requests
import json


# API_KEY='1c04f38f1d2f0979baea5787bc0cbdd8'
API_KEY='bd7f98121a9d0436318b3160e3374695'
url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page=1'

movies = requests.get(url).json()

print(movies['results'])

