from bs4 import BeautifulSoup
import csv

BASE_URL = "https://techstore.kg"

with open("index.html","r",encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")

products = soup.find_all("article",{"class":"product-card"})
products_list = []

for product in products:

    # ссылка на товар
    a_tag = product.find("h3", class_="product-name")
    product_link = BASE_URL + a_tag.find("a")["href"]

    # ссылка на картинку
    img_tag = a_tag.find("img")
    img_link = product.find("div", class_="product-image").text.strip()

    #название продукта
    name_tag = product.find("h3", class_="product-name")
    name = name_tag.text.strip()

    # цена
    price = product.find("span", class_="current-price").text.strip()

    products_list.append({
        "link": product_link,
        "name": name,
        "img": img_link,
        "price": price
    })

print(products_list[:3])

with open("products.csv","w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=products_list[0].keys())
    writer.writeheader()
    writer.writerows(products_list)