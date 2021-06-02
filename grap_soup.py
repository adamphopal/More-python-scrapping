from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests

url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing page
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#print(page_soup.h1)

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

# puts data in csv file
filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"
f.write(headers)

#loop
for container in containers:
    #brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    #print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    #puts data in csv file
    f.write(product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
                                        
#brand + "," + 

