from bs4 import BeautifulSoup
import csv

BASE_URL = "https://enter.kg"

with open("page.html","r",encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")

products = soup.find_all("div",{"class":"product vm-col vm-col-1"})
products_list = []

for product in products:

    # ссылка на товар
    a_tag = product.find("a", class_="product-image-link")
    product_link = BASE_URL + a_tag["href"]

    # ссылка на картинку
    img_tag = a_tag.find("img")
    img_link = BASE_URL + img_tag["src"]

    #название продукта
    name_tag = product.find("span", class_="prouct_name")
    name = name_tag.text.strip()

    # цена
    rows = product.find_all("div",{"class","rows"})
    price_row = rows[1] if len(rows) > 1 else None
    if price_row is not None:
        price = price_row.find("span", {"class", "price"}).text.strip()
    else:
        price = None

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


