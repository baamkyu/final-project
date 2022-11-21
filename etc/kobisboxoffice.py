import requests
import json
from datetime import datetime, timedelta

YESTERDAY = datetime.today() - timedelta(1)
YESTERDAY = YESTERDAY.strftime("%Y%m%d")
API_KEY = 'a222b6703b63955f330a30797f941c12'
print(YESTERDAY)

url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&targetDt={YESTERDAY}'
print(url)
movie = requests.get(url).json()
print(movie)

