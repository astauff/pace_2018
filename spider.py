import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll(id="gene_info"):
            link.get('href')
            print(link.text)
            #if(link.text == 'Entrez Gene'):
                #web(1, )




web(1,'https://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/clingen_gene.cgi?sym=cftr&subject')

#'https://en.wikipedia.org/wiki/List_of_libraries'