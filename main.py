"""
author: @oluiscabral

This code has the objective to search names of either universities
and people profile in the platform https://www.urionlinejudge.com.br/

The idea is to provide the URL of a list on this site,
then the program will return the searched profile if it exists
"""

from searcher import URIOJSearcher

def main():
    URIOJSearcher.search()

main()