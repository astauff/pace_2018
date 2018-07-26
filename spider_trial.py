import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':"mw-redirect"}):
            tet = link.get('title')
            if tet[0] == 'A':
                print(tet)
                tet_2 = WebUrl + link.get('href')
                print(tet_2)



web(1,'https://en.wikipedia.org/wiki/List_of_libraries')


