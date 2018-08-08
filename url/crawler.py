import re
import urllib

# from bs4 import BeautifulSoup
import BeautifulSoup as BeautifulSoup


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html



def getImg(html):
    reg = r'href="(.+\.html)"'
    imgre = re.compile(reg)
    htmllist1 = re.findall(imgre, html)
    htmllist=list()
    for html in htmllist1:
        if html not in htmllist:
            htmllist.append(html)
            print  html

    return htmllist


html = getHtml('http://10.16.117.191:18092')
# print html
print html