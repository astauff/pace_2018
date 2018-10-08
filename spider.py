import requests
from bs4 import BeautifulSoup

#This is the function to crawl ClinGin

def clingin(page,WebUrl):
    global info
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll(id="gene_info"):
            stuff = link.text.split(': ')
            for st in stuff:
                print(st)

        for link in s.findAll('a', attrs={'title':'Go to Entrez Gene'}):
            link.get('href')
            print(link.text + '\n')



def clingin_2(WebUrl2):
    url = WebUrl2
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for link in s.findAll():





#clingin(1,'https://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/clingen_gene.cgi?sym=cftr&subject')

#clingin(1,'https://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/clingen_gene.cgi?sym=brca1&subject')
