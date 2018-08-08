# -*- coding: utf-8 -*-
import re
import urllib

import requests
import bs4


root_url = 'http://10.16.117.191:18092'
index_url = root_url + '/UsageScenario/deployiamge.html'


def get_video_page_urls():
    page = urllib.urlopen(index_url)
    html = page.read()
    soup = bs4.BeautifulSoup(html)
    # iiii=soup.find_all("li", class_="header")
    iiii = soup.select('.header ')
    for ii in iiii:
        print ii.string
    reg=r'<li class="chapter" data-level="(1.\d.*)</li>'
    imgre = re.compile(reg)
    htmllist1 = re.findall(imgre, html)

    return iiii,imgre
print(get_video_page_urls().htnl.__len__())