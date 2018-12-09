import requests
from bs4 import BeautifulSoup

#This is the file for the Clingen website.

#This function works for the main page of each gene. (still under construction)

def clingen_start(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for link in s.findAll('div', attrs={'class':'col-sm-5'}):
        link.get('dl')
        print(link.text)

    for link in s.findAll('div', attrs={'class':'panel panel-primary'}):
        link.get('href')
        print(link.text)
        for thing in s.findAll('a', {'class':"btn btn-xs btn-success"}):#table': "panel-body table table-hover
            if thing.get('href')[0] != 'h':
                clingen_2(1, 'https://search.clinicalgenome.org'+thing.get('href'))
            else:
                #print(link.get('href'))
                if thing.get('href')[-1] == 't':
                    clingen_1(1, thing.get('href'))
                else:
                    clingen_3(1, thing.get('href'))


#This function works for the diagnosis sensitivity page.

def clingen_1(page,WebUrl):
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

#This function works for gene/disease validity.

def clingen_2(page, WebUrl2):
    global info
    if(page>0):
        url = WebUrl2
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for thing in s.findAll('',attrs={'class':'table-heading-bg table-heading'}):
            print(thing.text)

def clingen_3(page, WebUrl3):
    global info
    if(page > 0):
        url = WebUrl3
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for thing in s.findAll('div', attrs={'class':'colHeader lvl1 row'}):
            thing.get('span')
            print(thing.text)

#this is a test of the clingen_start function

def clingen_test(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    #for link in s.findAll('div', attrs={'class': 'col-sm-5'}):
     #   link.get('dl')
      #  print(link.text)

    for link in s.findAll('div', attrs={'class': 'panel panel-primary'} ): #'class': 'panel panel-primary'
        #print(link.text)
        for item in link.findAll('a'):
            if str(item.get('href'))[5:13] != 'conditions':
                print(str(item.get('href')))
            #str(item.get('href'))
            #if item.text[0] != 'h':
                #print('https://search.clinicalgenome.org' + str(item.get('href')))
            #else:
             #   if item.get('href')[-1] == 't':
              #      clingen_1(1, item.get('href'))
               # else:
                #    clingen_3(1, item.get('href'))
            print(item.text)
      #  for button in link:
       #    button.get('href')
        #    print(button)
        #for button in s.findAll('a', attrs={'class':'btn btn-xs btn-success'}):
         #   button.get('href')
          #  print(button)

        #for info in link.get('href'):
            #print(info)
        #for thing in s.findAll('a', {'class': "btn btn-xs btn-success"}):  # table': "panel-body table table-hover
         #   if thing.get('href')[0] != 'h':
          #      clingen_2(1, 'https://search.clinicalgenome.org' + thing.get('href'))
           # else:
                # print(link.get('href'))
            #    if thing.get('href')[-1] == 't':
             #       clingen_1(1, thing.get('href'))
              #  else:
               #     clingen_3(1, thing.get('href'))




#clingin(1,'https://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/clingen_gene.cgi?sym=cftr&subject')

#clingin(1,'https://www.ncbi.nlm.nih.gov/projects/dbvar/clingen/clingen_gene.cgi?sym=brca1&subject')

# attrs={'class':"btn btn-xs btn-success"}
