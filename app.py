#웹 크롤러

# pip install bs4

from bs4 import BeautifulSoup
from urllib.request import urlopen

# 메모장 초기화
fileName = 'output.txt'
f = open(fileName, 'w', encoding='utf-8')
f.write("")
f.close


# 사용자에게 입력값을 받기
address = input("크롤링할 웹 주소 : ")

# url 파싱 : 컴퓨터가 이해할수 있는 언어로 교체 (url부분으로 인식할수있게)
url = urlopen(address)

#html 파싱
soup = BeautifulSoup(url, 'html.parser')



# a 태그 추출
for i in soup.select('a'):
    link = i.get('href', '/')
    first7Chars = link[0:7]

    if (first7Chars != 'http://' and first7Chars != 'https://'):
        continue

    print(link)

    #메모장에 저장
    fileName = 'output.txt'
    f = open(fileName, 'a', encoding='utf-8') #a는 이어넣기, w는 덮어쓰기
    f.write(link + "\n")
    f.close