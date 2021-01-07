"""
author: @oluiscabral

This code has the objective to search names of either universities
and people profile in the platform https://www.urionlinejudge.com.br/

The idea is to provide the URL of a list on this site,
then the program will return the searched profile if it exists
"""

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
from page import Page

BASE_URL = "https://www.urionlinejudge.com.br/"


def search(relative_url: str):
    ret = []
    search_store = set()
    i = 0
    while True:
        i += 1
        r = requests.get(BASE_URL + relative_url, {'page': i, 'direction': 'DESC'})
        if r.status_code == 200:
            search_store.add(Page(r))
        else:
            break


def main():
    relative_url = input()
    result = search(relative_url)
