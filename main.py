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


def search(url: str, search_name: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


def main():
    url=input()
    search_name=input()
    result=search(url, search_name)
