
# encoding=utf-8
import base64

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

service_args = ['--proxy=%s' % 'http://16PGCOYA:238767@n10.t.16yun.cn:6442','--proxy-type=http','--load-images=no','--disk-cache=yes','--ignore-ssl-errors=true'
]

authentication_token = "Basic " + base64.b64encode(b'16YPROHH:195778')

capa = DesiredCapabilities.PHANTOMJS
capa['phantomjs.page.customHeaders.Proxy-Authorization'] = authentication_token

driver = webdriver.PhantomJS(desired_capabilities=capa, service_args=service_args)
driver.get('http://bj.58.com/chuzu/1/pn2/?key=北关东路')
print driver.page_source
driver.close()