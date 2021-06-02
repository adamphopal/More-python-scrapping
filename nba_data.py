import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
from string import ascii_lowercase

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata


playerdatasaved=""
for letter in ascii_lowercase:
    soup = make_soup("http://www.basketball-reference.com/players/a/")
    for record in soup.findAll('tr'):
        playerdata=""
        for data in record.findAll('td'):
            playerdata=playerdata+","+data.text
        if len(playerdata)!=0:
            playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "From,To,Pos,Ht,Wt,Birthdate,College" + "/n"
file = open(os.path.expanduser("Basketball.csv"), "wb")
file.write(bytes(header, encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

print(playerdatasaved)


#print(data.text)
