from urllib.parse import quote_plus
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests
import tkinter as tk

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

#bs=getHTML_bs('https://www.pythonscraping.com/pages/page3.html')
#attributeerror 예외처리 필요
'''
find(),find_all() 함수 공부.

print(bs.get_text())
#.get_text()함수는 문서 내의 모든 html 태그들을 제거하고, 텍스트들만 유니코드로 반환함.

namelist=bs.findAll('span',{'class':'green'})
#bs.tagname을 이용하면 해당 웹페이지의 html파일 내에서 가장 처음으로 등장하는 'tagname' 태그를 한개만 반환함.

list1=bs.find_all(['title','h1','h2'])

list2=bs.find_all('span',{'class':{'red','green'}})
#span 태그들 중에서 class 속성의 값이 red나 green인 모든 태그들을 찾음.

list_recursion=bs.find_all('span',{'class':'red'},False)
#recursive 인수가 True이면, 자식 태그들까지 조건에 맞는 태그들을 모두 찾음, False이면 가장 상위의 태그만 찾음.

list_prince=bs.find_all(string='the prince')
#string 인수는 태그의 속성이 아니라 태그에 의해 감싸진 텍스트 값을 통해 태그들을 필터링함.

list_limit=bs.find_all('span',limit=5)
#limit 인수는 페이지의 처음부터 해당 태그들 x개를 찾을때 이용함, find함수는 find_all함수의 limit 인수가 1임(인수로 입력받은 조건에 해당하는,
#페이지 내에서 가장 처음으로 나타나는 태그 1개만 찾아줌.)


list_keyword=bs.find_all(class_='red')
#keyword 인수는 어떤 속성 값이 특정한 값을 가진 태그들을 찾을 때 이용함. 원하는 속성 값들을 딕셔너리로 인수로
#전달하면 or조건이, keyword는 and 조건이 적용되어 태그들이 필터링됨.
'''

'''
beautifulsoup로 DOM tree 이용하기.

table_row_list=bs.find('table',{'id':'giftList'}).children
for a in table_row_list:
    print(a)
#beautifulsoup는 현재 선택된 태그들을 중심으로 자손(descendant) 태그들을 찾기 때문에 child 태그들만 찾으려면 .children를 써야됨.
#a.tag.subtag를 실행하면, tag밑의 자손 태그들 중에 가장 처음에 나타나는 subtag 1개만 선택됨.(child ∈ descendant)


for b in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(b)
#next_siblings는 선택된 태그의 부모를 기준으로 선택된 태그의 형제 태그들을 선택된 태그를 제외하고 찾아줌.


print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
#td 태그는 table 태그안의 하나의 행인 tr태그 의 자식인 하나의 셀을 의미하므로, td 안에 있는 이미지 태그의 부모는 td 태그임, 이 td태그의
#앞에 있는 형제는, tr태그를 부모로 기준으로 두면 이미지를 담은 td태그의 왼쪽에 있는 셀이므로 가격이 출력됨.
'''


def getHTML_bs_request(url):
    headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko',
    # 'cookie': 'session-id=132-7751821-0541661; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=133-3229317-0907535; session-token=P0Uz8E0v/hYpSJrs/6qcOjRRX516CHoi87Maf5bGXwCT7XcqCAe37TVpTQBM6KVMgJDZeDXaea4tlKYZ6ivuAAJbVeCzuF8iOO8Y/zfhuk2dnm6ziQlW48U6R06lyHIOesnsC/lOk+W1kCjU+zZNWvhd/FUYY0K7yDpkVlp20hENXbf5fwhhcrpJvLWRKmolc71Njh0/huZ78pBTJD1L7ajjmCiCFqgKNADGLGpN4fc=; csm-hit=s-XH340TZXD0V83AS7CWMM|1678390618333',
    'device-memory': '4',
    'downlink': '10',
    'dpr': '0.9',
    'ect': '4g',
    'referer': 'https://www.amazon.com/s?k=laptop&crid=30E3EBYZKEI9V&sprefix=%2Caps%2C122&ref=nb_sb_ss_recent_1_0_recent',
    'rtt': '0',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '0.9',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-viewport-width': '444',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'viewport-width': '444',
}
    
    #try:
    request=requests.get(url,headers=headers)

    #else:
    bs=BeautifulSoup(request.content,'html.parser')
    return bs

window=tk.Tk()
window.title('laptop spec comparision web crawler')
window.mainloop()



