from requests import Response


class Page:
    def __init__(self, r: Response):
        self.__url = r.url
        self.__text = r.text

    def get_url(self):
        return self.__url

    def get_text(self):
        return self.__text
