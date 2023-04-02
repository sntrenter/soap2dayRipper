from requests_html import HTMLSession
from bs4 import BeautifulSoup
from cookies import cookies
session = HTMLSession()
response = session.get('https://soap2day.to', headers={'User-Agent': 'Mozilla/5.0'})
response.html.render(timeout=10)

#if a tag that has text continue exists, click it
while response.html.find('a', containing='Continue'):
    response.html.find('a', containing='Continue')[0].click()
    response.html.render(timeout=10)


soup = BeautifulSoup(response.html.html, 'html.parser')
links = soup.find_all('a', href=True)
print(links)