#!/usr/bin/env python3

# from urllib.request import urlopen
import dryscrape
from bs4 import BeautifulSoup
import copy

# This function grabs all the categories to be used in the Kijiji links
def getCategories():
    categories = []
    url = 'http://kijiji.ca/'
    # html = urlopen(url).read()
    session = dryscrape.Session()
    session.visit(url)
    html = session.body()
    soup = BeautifulSoup(html, 'html.parser')
    # return soup.text
    links = soup.find(id='Categories').find('ul').find_all('a')
    for thing in links:
        thing = thing.get('href')
        category = thing.split('/')[1]
        categories.append(category)
    return categories
