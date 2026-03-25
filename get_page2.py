import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent (browsers=["Edge","Chrome"])
BASE_URL = "https://techstore.kg"
ENDPOINT = "/tehnika_bishkek"

headers = {"User-Agent": ua.random}

response = requests.get(url=f"{BASE_URL}{ENDPOINT}",headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
with open("index.html", "w")as file:
    file.write(soup.prettify())
