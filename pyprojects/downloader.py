# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import requests
import urllib.request
import re
from bs4 import BeautifulSoup

i = 0

def print_hi(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.contents)
    fomr = soup.find_all('span', class_='download')
    for a in fomr:
        # print(a.contents[0].get('href'))
        doc = requests.get(a.contents[0].get('href'))
        u = a.contents[0].get('href')
        song = u.rsplit('/',1)[1]
        movie = u.rsplit('/',2)[1]
        path = "./"+movie+"/"+song
        if not os.path.exists("./"+movie):
            os.mkdir("./"+movie)
        with open(path, 'wb') as f:
          f.write(doc.content)

    # for a in soup.find_all('a'):
    #     if len(a['href']) > 0:
    #         filename = a['href'][a['href'].rfind("/") + 1:]
    #         print(filename)
    #         # doc = requests.get(a['href'])
    #         # with open(filename, 'wb') as f:
    #         #    f.write(doc.content)


def navigatePage(url):
    array = [""]
    for letter in array:
        s = url
        r = requests.get(s)
        soup = BeautifulSoup(r.content, 'html.parser')
        urllist = soup.find_all('span',class_='folder1')
        for u in urllist:
            try:
                print_hi("https://friendstamilmp3.in//"+u.contents[0].get('href'))
            except:
                print("Exception")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    navigatePage('https://friendstamilmp3.in/index.php?page=Music%20Director%20Hits')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


