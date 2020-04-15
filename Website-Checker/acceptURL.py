import urllib.request
from bs4 import BeautifulSoup
import json
import time
import requests

class acceptURL():
    def __init__(self, url):
        self.url = url


    def setURL(self, url):
        self.url = url
    #
    # def printURL(self):
    #     print(self.url)

    def parseURL(self):
        """Passes the html of the site
        into the page variable and then
        store the html in a Beautiful
        Soup format
        """
        # r = requests.get(self.url)
        # FormattedData = r.json()
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')
        time.sleep(2)
        self.json_obj = json.loads(self.soup.find('script', type='application/ld+json').text)
        self.printHTMLToFile()
        print(self.json_obj)

    def printHTMLToFile(self):
        metaList = self.soup.find_all("meta")
        with open("WebsiteHtml.txt", "w") as f:
            f.write(str(self.json_obj))
            # for meta in metaList:
            #     if "author" in str(meta) and "content" in str(meta):
            #         f.write(str(meta))
            # print(self.soup.body)

        # print(self.soup.prettify())
