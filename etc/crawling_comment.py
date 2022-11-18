import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

wb = load_workbook('./연도별 박스오피스 순위.xlsx')
ws = wb.active

# for r in range(4, ws.max_row+1):
for r in range(4, 5):
    print(ws.cell(row=r, column=1).value)
    movie_title = ws.cell(row=r, column=1).value

    url = f'https://movie.naver.com/movie/bi/mi/basic.naver?code=99702'
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        # print(soup.title)

        soup = soup.find_all('div', {'class': 'score_reple'})
        soup = soup.find_all('p')
        print(soup)

# x_path = //*[@id="main_pack"]/div[2]/div[2]/div[2]/div/div[2]/div[6]/ul


# soup.title.string
# soup.title.get_text()