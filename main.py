# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# </body>
# </html>
# """



# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')




# print in structured way
# print(soup.prettify())



# обращение к тэгам
# title = soup.title
# print(title)
# p = soup.p
# print(p)

# a = soup.a
# print(a)
#
# aref = a['href']
# print(aref, a['class'],a['id'])

# Поиск элементов
# sisters = soup.find_all("a",class_="sister")


#Поиск элементов 2 способ
# sisters = soup.find_all(attrs={
#     "class":"sister"
# })
# for sister in sisters:
#     # print(f"sister tag{sister}")
#     print(f"name:{sister.string}")
#     # print(f"name:{sister.text}")



#Поиск элемента (найдет первое совпадения)
# sister = soup.find("a", class_="sister")
# print(sister)


from bs4 import BeautifulSoup

html = """  
<div class="product">  
    <h2>iPhone 15</h2>  
    <p class="price">85000</p>  
    <a href="/iphone-15">Подробнее</a>  
</div>  

<div class="product">  
    <h2>Samsung S24</h2>  
    <p class="price">79000</p>  
    <a href="/samsung-s24">Подробнее</a>  
</div>  
"""



# result = [
#     {"name":"iphone 15",
#      "price": 850000,
#      "link": "/iphone-15"
#      },
#     {
#      "name":"samsung s24",
#      "price": 800000,
#      "link": "/samsung-s24"
#     }
# ]
soup = BeautifulSoup(html, "html.parser")
result = []
products = soup.find_all('div', class_='product')
for product in products:
    name = product.find('h2').text
    price = product.find('p', class_='price').text
    link = product.find('a')['href']

    result.append({'name':name, 'price':price, 'link':link})

print(result)