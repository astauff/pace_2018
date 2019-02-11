#***** THIS FILE IS FOR CLINGEN ONLY *****#

import requests
from bs4 import BeautifulSoup


# This function works for the main page of each gene. (still under construction)
def clingen_start(Start_Url):
    # gaining access to page, parsing info and turning info into readable data
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    # getting info at top of page
    for topL in s.findAll('dt'):
        print(topL.text)

    for topR in s.findAll('dd'):
        print(topR.text)

    # getting info stored in table
    for info in s.findAll('div', attrs={'class': 'panel panel-primary'}):
        info.get('href')
        print(info.text)

    # getting desired links on page
    for link in s.findAll('div', attrs={'id': 'accordion'}):  # 'class': 'panel panel-primary'
        for item in link.findAll('a'):
            if str(item.get('href'))[4:14] != 'conditions':
                if str(item.get('href'))[0] != 'h':
                    if str(item.get('href'))[0] != 'N':
                        print('https://search.clinicalgenome.org' + str(item.get('href')))
                else:
                    print(str(item.get('href')))

    # second-level scraping of links on page
    #for thing in s.findAll('a', {'class': "btn btn-xs btn-success"}):  # table': "panel-body table table-hover
     #   if thing.get('href')[0] != 'h':
      #      clingen_2(1, 'https://search.clinicalgenome.org' + thing.get('href'))
       # else:
            # print(thing.get('href'))
        #    if thing.get('href')[-1] == 't':
         #       clingen_1(1, thing.get('href'))
          #  else:
           #     clingen_3(1, thing.get('href'))


# This function works for the diagnosis sensitivity page.
def clingen_1(file, page, WebUrl):
    global info
    file_name = file
    open(file_name, "a+")
    if (page > 0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll(id="gene_info"):
            stuff = link.text.split(': ')
            for st in stuff:
                f = open(file_name, "a+")
                f.write(st)

        for link in s.findAll('a', attrs={'title': 'Go to Entrez Gene'}):
            link.get('href')
            f = open(file_name, "a+")
            f.write(link.text + '\n')

        # inserting new line to make more readable
        f = open(file_name, "a+")
        f.write('\n')


# This function works for gene/disease validity.
def clingen_2(file, page, WebUrl2):
    global info
    file_name = file
    open(file_name, "a+")
    if (page > 0):
        url = WebUrl2
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for thing in s.findAll('', attrs={'class': 'table-heading-bg table-heading'}):
            f = open(file_name, "a+")
            f.write(thing.text + '\n')

        #inserting new line to make more readable
        f = open(file_name, "a+")
        f.write('\n')


# This function works for clinical actionability.
def clingen_3(file, page, WebUrl3):
    global info
    file_name = file
    open(file_name, "a+")
    if (page > 0):
        url = WebUrl3
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")

        # getting data at top of table
        # for head in s.findAll('div', attrs={'class':'colHeader lvl1 row'}):
        #   head.get('span')
        #  print(head.text)

        # getting column info
        # for col in s.findAll('span', attrs={'class':'paragraph'}, limit=3):
        #   print(col.text)

        # getting numbered headers
        # for numhead in s.findAll('div', attrs={'class':'sectionName h4 text-left col-xs-12'}):
        # if numhead.text != "Final Consensus Scores":
        # print(numhead.text)

        # getting the main table data stored in paragraphs
        #unwanteds = s.findAll('div', attrs={'class': 'refs text-left col-xs-1'})
        #for unwanted in unwanteds:
        #    unwanted.extract()
        #for par in s.findAll('div', {'class': ['allContentsAndRefs col-xs-10']}):
        #    for thing in par.findAll('span', attrs={'class': 'paragraph'}):
        #        if thing.text != 'Narrative Description of Evidence' and thing.text != 'Ref':
        #            print(thing.text)

        # getting row info
        # for row in s.findAll('div',attrs={'class':'topic text-center col-xs-2'}):
        #   row.get('span')
        #  print(row.text)

        # getting ref
        # for ref in s.findAll('div', attrs={'class':'refs text-left col-xs-1'}):
        #   ref.get_text
        #  print(ref.text)

        # print(ref.text)

    # getting everything in the table at once
    for every in s.findAll(True, {"class": ["data even row", "data odd row", "sectionName h4 text-left col-xs-12"]}):
        every.get('span')
        if every.text != 'Final Consensus Scores':
            f = open(file_name, "a+")
            f.write(every.text)
            # print(every.text)

    # inserting new line to make more readable
    f = open(file_name, "a+")
    f.write('\n')


# this is a test of the clingen_start function to be manipulated for development
def clingen_test(file, Start_Url):
    # gaining access to page, parsing info and turning info into readable data
    file_name = file + ".txt"
    f = open(file_name, "w+")
    f.write("This file is for the gene " + file + 2*'\n')
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    # getting info at top of page
    for topL in s.findAll('dt'):
        f = open(file_name, "a+")
        f.write(topL.text + '\n')
         #print(topL.text)

    # inserting new line to make more readable
    f = open(file_name, "a+")
    f.write('\n')

    for topR in s.findAll('dd'):
        f = open(file_name, "a+")
        f.write(topR.text + '\n')
        # print(topR.text)

    # inserting new line to make more readable
    f = open(file_name, "a+")
    f.write('\n')

    # getting info stored in table
    for info in s.findAll('div', attrs={'class': 'panel panel-primary'}):
        info.get('href')
        f = open(file_name, "a+")
        f.write(info.text)

    # inserting new line to make more readable
    f = open(file_name, "a+")
    f.write('\n')

    # getting desired links on page
    for link in s.findAll('div', attrs={'id': 'accordion'}):  # 'class': 'panel panel-primary'
        for item in link.findAll('a'):
            if str(item.get('href'))[4:14] != 'conditions':
                if str(item.get('href'))[0] != 'h':
                    if str(item.get('href'))[0] != 'N':
                        f.write('https://search.clinicalgenome.org' + str(item.get('href')) + '\n')
                else:
                    f.write(str(item.get('href')) + '\n')

    # inserting new line to make more readable
    f = open(file_name, "a+")
    f.write('\n')

    # second-level scraping of links on page
    for thing in s.findAll('a', {'class': "btn btn-xs btn-success"}):  # table': "panel-body table table-hover
        thing.get('href')
        if thing.get('href')[0] != 'h':
            clingen_2(file_name, 1, 'https://search.clinicalgenome.org' + thing.get('href'))
        else:
            if thing.get('href')[-1] == 't':
                clingen_1(file_name, 1, thing.get('href'))
            else:
                clingen_3(file_name, 1, thing.get('href'))

    f.close()





#working on keeping rows together
def list_trial(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    ref_list = []
    par_list = []

    # getting refs
    for ref in s.findAll('div', attrs={'class':'refs text-left col-xs-1'}):
        ref.findAll('span', limit=1)
        ref.get_text
        ref_list.append(ref.text)

    # getting "paragraphs"
    unwanteds = s.findAll('div', attrs={'class': 'refs text-left col-xs-1'})
    for unwanted in unwanteds:
        unwanted.extract()
    for par in s.findAll('div', {'class':['allContentsAndRefs col-xs-10']}):
        for thing in par.findAll('span', attrs={'class':'paragraph'}):
            if thing.text != 'Narrative Description of Evidence' and thing.text != 'Ref':
                par_list.append(thing.text)
                #print(thing.text)

    #print(str(len(ref_list)) + '\n')
    #print(len(par_list))

    #loop for printing data
    for i in range(0,18):
        print(par_list[i] + ref_list[i])
