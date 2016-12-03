#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import copy

# This function grabs all the categories to be used in the Kijiji links
def getCategories():
    categories = []
    url = 'http://www.kijiji.ca/'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find(id='Categories').find('ul').find_all('a')
    for thing in links:
        thing = thing.get('href')
        category = thing.split('/')[1]
        categories.append(category)
    return categories
