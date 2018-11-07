from selenium import webdriver
from base64 import b64encode

proxy = {'host': 'http://16PGCOYA:238767@n10.t.16yun.cn', 'port': '6442', 'usr': '16YPROHH', 'pwd': '195778'}

fp = webdriver.FirefoxProfile()

fp.add_extension('closeproxy.xpi')
fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.http', proxy['host'])
fp.set_preference('network.proxy.http_port', int(proxy['port']))
# ... ssl, socks, ftp ...
fp.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')

credentials = '{usr}:{pwd}'.format(**proxy)
credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
fp.set_preference('extensions.closeproxyauth.authtoken', credentials)

driver = webdriver.Firefox(fp)