import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Bars&find_loc='
loc = 'Ventura,CA'
current_page = 0


while current_page < 201:
    print(current_page)
    url = base_url + loc +"&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)

    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
        for biz in businesses:
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            print(title)
            try:
                address = biz.findAll('address')[0].contents
                second_line = ""
                first_line = ""
                #print(address)
                for item in address:
                    if "br" in str(item):
                        #print(item.getText())
                        second_line += item.getText()
                    else:
                        first_line = item.strip(" \n\t\r")
                        #print(item.strip(" \n\t\r"))
                print(first_line)
                print(second_line)
            except:
                pass
         #   try:
         #       address = biz.findAll('address')[0]#.text.replace('', '')
         #   except:
          #      address = None
           # print(address)
            print('\n')
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(" \n\t\r")
            except:
                phone = None
            print(phone)
            page_line = "Title: {title}\nAddress: {address_1}\n{address_2}\nPhone: {phone}\n\n".format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    phone=phone
                )
            textfile.write(page_line)
        current_page += 10



#print(yelp_r.status_code)







    
#print(yelp_soup.prettify())
#print(yelp_soup.findAll('li', {'class': 'regular-search-result'}))

#print(yelp_soup.findAll('a', {'class': 'biz-name'}))

#for name in yelp_soup.findAll('a', {'class': 'biz-name'}):
#   print(name.text)
