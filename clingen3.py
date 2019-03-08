import requests
from bs4 import BeautifulSoup

def row_sort(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    row_list = []

    # getting row titles
    for row in s.findAll('div', attrs={'class': 'topic text-center col-xs-2'}):
        row.get('span')
        row_list.append(row.text)

    return row_list




# this function gets the paragraphs
def par_sort(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    # getting "paragraphs"
    # filtering out everything but paragraphs
    unwanteds = s.findAll('div', attrs={'class': 'refs text-left col-xs-1'})
    for unwanted in unwanteds:
        unwanted.extract()

    # filtering out row info
    unwanteds_2 = s.findAll('div', attrs={'class': 'topic text-center col-xs-2'})
    for unwanted_2 in unwanteds_2:
        unwanted_2.extract()

    # filtering out the numbered headers
    unwanteds_3 = s.findAll('div', attrs={'class': 'colHeader lvl3 row'})
    for unwanted_3 in unwanteds_3:
        unwanted_3.extract()

    # finding the number of rows
    kid_list = []
    for kid in s.findAll(True, attrs={'class': ['data even row', 'data odd row']}):
        kid_list.append(kid.get('div'))

    # this is where we actually get paragraphs
    par_list = []
    first_div = s.find(True, attrs={'class': ['data even row', 'data odd row']})
    for kiddo in first_div.findChildren('span'):
        par_list.append(kiddo.text)

    for i in range(0, len(kid_list)):
        first_div.find_next_siblings('div')
    for youngn in first_div.find_next_siblings('div'):
        par_list.append(youngn.text)


    #print(len(par_list))
    #print(len(row_list))


    # loop for printing data
    #for i in range(0,len(par_list)):
     #   print(row_list[i] + par_list[i] + ref_list[i])

    return par_list




# trying to put all of the child tags together for equal number of rows
def ref_sort(Start_Url):
    url = Start_Url
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")


    # getting all info in the "paragraphs"

    # filtering out the ref numbers
    unwanteds = s.findAll('div', attrs={'class': 'colHeader data lvl2 row'})
    for unwanted in unwanteds:
        unwanted.extract()

    #filtering out row info
    unwanteds_2 = s.findAll('div', attrs={'class': 'topic text-center col-xs-2'})
    for unwanted_2 in unwanteds_2:
        unwanted_2.extract()

    #filtering out the numbered headers
    unwanteds_3 = s.findAll('div', attrs={'class': 'colHeader lvl3 row'})
    for unwanted_3 in unwanteds_3:
        unwanted_3.extract()

    # the two filters below are for the paragraphs
    unwanteds_4 = s.findAll('span', attrs={'class':'tierText'})
    for unwanted_4 in unwanteds_4:
        unwanted_4.extract()

    unwanteds_5 = s.select('div[class$="text-left col-xs-11"]')
    for unwanted_5 in unwanteds_5:
        unwanted_5.extract()

    # getting number of rows for data organization
    kid_list = [] # this is a list of the number of rows in the table
    for kid in s.findAll(True, attrs={'class':['data even row', 'data odd row']}):
        kid_list.append(kid.get('div'))

    # getting the refs

    # getting first row
    ref_list = []
    first_div = s.find(True, attrs={'class': ['data even row', 'data odd row']})
    for kiddo in first_div.findAll('div', attrs={'class': 'refs text-left col-xs-1'}):
        kiddo.get('a')
        ref_list.append(kiddo.text)

    for i in range(0, len(kid_list)):
        first_div.find_next_siblings('div')
    for youngn in first_div.find_next_siblings('div'):
        youngn.get('a')
        ref_list.append(youngn.text)

    return ref_list



# THIS FUNCTION IN NO LONGER IN USE
# This function works for clinical actionability.
def clingen_3_1(file, page, WebUrl3):
    global info
    file_name = file + ".txt"
    open(file_name, "a+")
    if (page > 0):
        url = WebUrl3
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")

        # here is where we test out the lists
        row = row_sort(WebUrl3)
        par = par_sort(WebUrl3)
        ref = ref_sort(WebUrl3)
        for i in range(0, len(par)):
            #print(row[i] + par[i] + ref[i])
            f = open(file_name, "a+")
            f.write(row[i] + par[i] + ref[i])

        # getting everything in the table at once
        #for every in s.findAll(True,{"class": ["data even row", "data odd row", "sectionName h4 text-left col-xs-12"]}):
         #   every.get('span')
          #  if every.text != 'Final Consensus Scores':
           #     f = open(file_name, "a+")
            #    f.write(every.text)
                        # print(every.text)

            # inserting new line to make more readable
            f = open(file_name, "a+")
            f.write('\n')


def kid_count(file, WebUrl):
    # opening the text file
    file_name = file + ".txt"
    f = open(file_name, "w")

    f.truncate()

    # printing gene name at top of file
    f.write("This file is for the gene: " + file + '\n')

    url = WebUrl
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    sib_list = []

    # getting data at top of table
    for head in s.findAll('div', attrs={'class': 'colHeader lvl1 row'}):
        head.get('span')
        f.write(head.text)

    # getting column info
    for col in s.findAll('span', attrs={'class': 'paragraph'}, limit=3):
        f.write(col.text + 10*" ")

    # calling functions to get structured info
    row = row_sort(WebUrl)
    par = par_sort(WebUrl)
    ref = ref_sort(WebUrl)

    # first numbered header
    first_div = s.find('div', attrs={'class':'colHeader lvl3 row'})
    # printing header
    f.write(first_div.text)

    # variable to gather numbered headers
    count = []
    # variable for position in lists for printing
    pos = 0

    for num in s.findAll('div', attrs={'class': 'sectionName h4 text-left col-xs-12'}):
        # leaving out unwanted header at bottom of page
        if num.text != "Final Consensus Scores":
            # adding header to list, increasing number of headers in list
            count.append(num.text)

    # getting rows under first header
    for goon in first_div.findNextSiblings('div'):
        # how the program knows it has found another header and to stop counting
        if goon.select('div[class="sectionName h4 text-left col-xs-12"]'):
            break
        else:
            # adding a row to the list
            sib_list.append(goon)
            # printing structured info row by row
            f.write(row[pos] + par[pos] + ref[pos])
            # adding 1 to move pos one place
            pos += 1

    # variable used for the loop
    i = 1

    # loop to find other headers
    while i < len(count):
        # list of rows for each header
        sib_list = []
        # finding the next header
        next_div = first_div.findNextSibling('div', attrs={'class':'colHeader lvl3 row'})
        # printing the header
        f.write(next_div.text)

        # finding the rows under the header
        for hope in next_div.findNextSiblings('div'):
            # how the program knows it has found another header and to stop counting
            if hope.select('div[class="sectionName h4 text-left col-xs-12"]'):
                break
            else:
                # adding a row to the list
                sib_list.append(hope)
                # printing structured info row by row
                f.write(row[pos] + par[pos] + ref[pos])
                # adding 1 to move pos one place
                pos += 1

        # moving to next spot in the loop
        i += 1

        # going to next header
        first_div = first_div.findNextSibling('div', attrs={'class': 'colHeader lvl3 row'})
