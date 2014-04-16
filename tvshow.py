import urllib
from BeautifulSoup import BeautifulSoup
x= urllib.urlopen('http://moviesnow.co.in/schedule')
data=x.readlines()
soup = BeautifulSoup(''.join(data))
films=soup.findAll('a','txt15')
film=[f.string for f in films if f.string]
for f in film: print f