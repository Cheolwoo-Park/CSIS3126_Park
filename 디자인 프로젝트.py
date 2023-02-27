from urllib.parse import quote_plus
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getHTML_bs(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        #404 not found error, 403 forbidden
        print(e)
    except URLError  as e:
        print('서버를 찾지 못함.')
    else:
        bs=BeautifulSoup(html.read(),'html.parser')
        return bs

bs=getHTML_bs('http://www.pythonscraping.com/pages/warandpeace.html')
#attributeerror 예외처리 필요

#print(bs.get_text())
#.get_text()함수는 문서 내의 모든 html 태그들을 제거하고, 텍스트들만 유니코드로 반환함.

namelist=bs.findAll('span',{'class':'green'})
#bs.tagname을 이용하면 해당 웹페이지의 html파일 내에서 가장 처음으로 등장하는 'tagname' 태그를 한개만 반환함.

list1=bs.find_all(['title','h1','h2'])

list2=bs.find_all('span',{'class':{'red','green'}})
#span 태그들 중에서 class 속성의 값이 red나 green인 모든 태그들을 찾음.

list_recursion=bs.find_all('span',{'class':'red'},False)
#recursive 인수가 True이면, 자식 태그들까지 조건에 맞는 태그들을 모두 찾음, False이면 가장 상위의 태그만 찾음.

list_prince=bs.find_all(string='the prince')
print(len(list_prince))
#string 인수는 태그의 속성이 아니라 태그에 의해 감싸진 텍스트 값을 통해 태그들을 필터링함.

list_limit=bs.find_all('span',limit=5)
'''
limit 인수는 페이지의 처음부터 해당 태그들 x개를 찾을때 이용함, find함수는 find_all함수의 limit 인수가 1임(인수로 입력받은 조건에 해당하는,
페이지 내에서 가장 처음으로 나타나는 태그 1개만 찾아줌.)
'''

list_keyword=bs.find_all(class_='red')
'''
keyword 인수는 어떤 속성 값이 특정한 값을 가진 태그들을 찾을 때 이용함. 원하는 속성 값들을 딕셔너리로 인수로
전달하면 or조건이, keyword는 and 조건이 적용되어 태그들이 필터링됨.
'''



'''
for child in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(child)
'''
