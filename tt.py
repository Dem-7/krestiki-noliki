import requests
from bs4 import BeautifulSoup
url ="http://quotes.toscrape.com/"
response = requests.get(url)
pp = response.text
klo = BeautifulSoup(pp, "html.parser")
nn = klo.find_all("span", class_="text")
pdf = klo.find_all("small",class_="author")
for a in range(len(nn)):
    print(f"Номер цитаты - {a + 1}")
    print(nn[a].text)
    print(f"Автор : {pdf[a].text}\n")
    
