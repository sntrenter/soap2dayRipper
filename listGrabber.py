from bs4 import BeautifulSoup
import requests
from cookies import cookies
url = "https://soap2day.to/movielist?page={}"


#get all links from the page beautiful soup
def getLinks(url):
    html = requests.get(url,cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    return links

#print all buttons on page
def getButtons(url):
    html = requests.get(url,cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    buttons = soup.find_all('button')
    return buttons

#get all elements with class beautiful soup
def getElements(url):
    html = requests.get(url,cookies=cookies).text
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="btn btn-success")
    return elements



def main():
    print("Start")
    print(cookies)
    print("Getting links from page 1")
    links = getElements(url.format(1))
    print(links)
    #print(getButtons(url.format(1)))

    print("End")

if __name__ == "__main__":
    main()