import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_detail_data(soup):
    try:
        title = soup.find('h1', id='itemTitle').text.strip()[16:]
    except:
        title = 'Nope'
    print(title)
    try:
        try:
            p = soup.find('span', id='prcIsum').text.strip()
        except:
            p = soup.find('span', id='mm-saleDscPrc').text.strip()
        currency, price = p.split(' ')
    except:
        currency = 'US'
        price = '0'
    print(price)
    print(currency)

    try:
        sold = soup.find('span', class_='vi-qtyS').find('a').text.strip().split(' ')[0]
    except:
        sold = '0'
    print(sold)

    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total sold': sold
    }

    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links]

    return urls

   
def write_csv(data, url):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], data['currency'], data['total sold'], url + "\t"]
        writer.writerow(row)



def main():
    csv_file = open('output.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'price', 'currency', 'total sold', 'link'])
    csv_file.close()
    url = 'https://www.ebay.com/sch/i.html?_nkw=python+programming&_ipg=200&_pgn=1'
    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        write_csv(data, link)
        #print(data)
       
  

if __name__ == '__main__':
    main()
