# Web scraping is used to get contents from a website.
# You can use it to get the titles of blog posts, information,
# and more. All you need is a website url, additional methods
# from the bs4 library and additional codes to get the content you need

import requests
from bs4 import BeautifulSoup


def scrapeContent(url, tag_name, class_name):
    r = requests.get(url)
    if (r.status_code == 200):

        soup = BeautifulSoup(r.content, 'lxml')
        title = soup.find_all('{0}'.format(tag_name), {
                              'class': '{0}'.format(class_name)})

        print(title)
    else:
        print("What your are looking for is not found")


url_link = input("Please input the website : ")
tag_name = input("What tag is the content in? : ")
class_name = input("What is the class name of the content? : ")


scrapeContent(url_link, tag_name, class_name)
