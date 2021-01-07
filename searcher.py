from bs4 import BeautifulSoup
import requests
from bs4.element import Tag

class URIOJSearcher:
    __BASE_URL = "https://www.urionlinejudge.com.br/"
    
    @staticmethod
    def __get_items(HTML_TEXT: str):
        ret = set()
        soup = BeautifulSoup(HTML_TEXT, 'html.parser')
        element = soup.select('.main-content #table .list #element')[0]
        tbody = element.select('table tbody')[0]
        for tr in tbody.select('tr'):
            if len(tr.get_text(strip=True)) == 0:
                break
            pos = tr.findChild('td').text
            name = tr.find(href=True).text.strip()
            ret.add((pos, name))
        return ret
    
    @staticmethod
    def __get_search_store(URL:str):
        search_store = set()
        i = 0
        while True:
            i += 1
            r = requests.get(URL, {'page': i, 'direction': 'DESC'})
            if r.status_code == 200:
                search_store.update(URIOJSearcher.__get_items(r.text))
            else:
                break
        return search_store
    
    @staticmethod
    def __get_results(SEARCH_STORE, SEARCH_TEXT:str):
        ret = set()
        for item in SEARCH_STORE:
            name:str = item[1].upper()
            if name.find(SEARCH_TEXT) != -1:
                ret.add(item)
        return ret
    
    @staticmethod
    def search():
        while True:
            relative_url:str = input("Insert the relative url to search in:\n")
            if len(relative_url.strip()) == 0:
                break
            search_store = URIOJSearcher.__get_search_store(URIOJSearcher.__BASE_URL + relative_url)
            if len(search_store) == 0:
                print("Page not found or table is empty")
            else:
                while True:
                    search_text = input("Insert what you want to search:\n").upper()
                    if len(search_text.strip()) == 0:
                        break
                    results = URIOJSearcher.__get_results(search_store, search_text)
                    for result in results:
                        print(result[0], result[1])
