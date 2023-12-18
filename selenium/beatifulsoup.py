import requests
from bs4 import BeautifulSoup

url = 'https://water.taiwanstat.com/'
web = requests.get('https://www.google.com.tw')
soup = BeautifulSoup(web.text, "html.parser")
reservoir = soup.select('gNO89b')     # 取得所有 class 為 reservoir 的 tag
for i in reservoir:
  print(i.find('div', class_='name').get_text(), end=' ')  # 取得內容的 class 為 name 的 div 文字
  print(i.find('h0').get_text(), end=' ')   # 取得內容 h5 tag 的文字
  print()