
import re
import urllib

import requests
import bs4


root_url = 'http://10.16.117.191:18092'
index_url = root_url + '/UsageScenario/deployiamge.html'


def get_video_page_urls():
    page = urllib.urlopen(root_url)
    html = page.read()
    soup = bs4.BeautifulSoup(html)
    iiii = soup.select('[data-level^="7."] a')
    for ii in iiii:
        htmllist1=ii.attrs['href']
        print htmllist1
    return iiii
print(get_video_page_urls().__len__())