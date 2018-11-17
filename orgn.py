from bs4 import BeautifulSoup
import os
import re
import urllib
page = urllib.urlopen('http://top.zhan.com/toefl/read/practicereview-122-13.html')
htmlcode = page.read()
soup=BeautifulSoup(htmlcode)
fo = open("temp.txt", "w+")
for p in soup.find_all(name='h1',attrs={"class":"last_crumbs"}):
    fo.write(p.get_text().encode('utf-8'))
    print p.get_text().encode('utf-8')
    po=p.get_text().encode('utf-8')[6]+p.get_text().encode('utf-8')[7]+p.get_text().encode('utf-8')[8]+p.get_text().encode('utf-8')[9]+p.get_text().encode('utf-8')[10]
for p in soup.find_all(name='span',attrs={"class":"article_tit"}):
    fo.write(p.get_text().encode('utf-8'))
    po = po+p.get_text().encode('utf-8')
fo.write('\n\n')
for link in soup.find_all(name='span',attrs={"class":"text"}):
    fo.write(link.get_text().encode('utf-8'))
print('finish')
fo.close()
os.rename('temp.txt',po+'.txt')
