#coding:utf-8
import urllib2
import sys
import re
import base64
from urlparse import urlparse
import httplib
import json
import urllib

# auth_url = HW_AUTH_ENDPOINT+HW_AUTH_URI
def get_token():
    url = 'https://ecs.cn-north-1.myhuaweicloud.com/v1/e79484c699864e76957fdb6687a806b0/cloudservers/flavors'
    # datagen = json.loads('')
    headers2 = {'Content-Type':'application/json;charset=utf8','X-Auth-Token':'MIIGxgYJKoZIhvcNAQcCoIIGtzCCBrMCAQExDTALBglghkgBZQMEAgEwggUUBgkqhkiG9w0BBwGgggUFBIIFAXsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMTgtMDUtMDVUMDg6MzE6MTAuODUwMDAwWiIsIm1ldGhvZHMiOlsiYXNzdW1lX3JvbGUiXSwiY2F0YWxvZyI6W10sInJvbGVzIjpbeyJuYW1lIjoicmVhZG9ubHkiLCJpZCI6IjBlZjhjNjA2OWZkMDQ1ZDI5ZmFmYzQ4ZWNjYzU0ZWZmIn0seyJuYW1lIjoidGVfYWRtaW4iLCJpZCI6IjdiZjk0NDU5OTdhMTQ0Njk5OTU1MGFhZWE1MWM5OTEyIn0seyJuYW1lIjoib3BfZ2F0ZWRfZmVuZ2x1YW4wMTI0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbGlqaW5waW5nNjIyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfbGVnYWN5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc2hhbmhlMDEyNCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JvdGFvMDEyNCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2RlamludGVzdDAwMiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX3Jlc3RyaWN0ZWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF90ZXN0MSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX3VudmVyaWZpZWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF8wNjIwdGVzdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2RlamludGVzdDAwMSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX0xXWSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Rlc3QwMSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3FhejAwMSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3FhejAwMiIsImlkIjoiMCJ9XSwicHJvamVjdCI6eyJkb21haW4iOnsibmFtZSI6Imp3emhvdWkiLCJpZCI6IjdjN2ZlMzZkZTE4NzQ3ZTJhMGI1MGFhMjcxYmJlMzBjIn0sIm5hbWUiOiJjbi1ub3J0aC0xIiwiaWQiOiJlNzk0ODRjNjk5ODY0ZTc2OTU3ZmRiNjY4N2E4MDZiMCJ9LCJpc3N1ZWRfYXQiOiIyMDE4LTA1LTA0VDA4OjMxOjEwLjg1MDAwMFoiLCJ1c2VyIjp7ImRvbWFpbiI6eyJuYW1lIjoiand6aG91aSIsImlkIjoiN2M3ZmUzNmRlMTg3NDdlMmEwYjUwYWEyNzFiYmUzMGMifSwibmFtZSI6Imp3emhvdWkvand6aG91aS1ydWFudG9uZ2Nsb3VkIiwiaWQiOiJmMmZhMzkxMThlNDI0ZWI3ODFkYjEyOWRmYjQ3MGRkYiJ9LCJhc3N1bWVkX2J5Ijp7InVzZXIiOnsiZG9tYWluIjp7Im5hbWUiOiJydWFudG9uZ2Nsb3VkIiwiaWQiOiIxZTcwMTRkOWQ0NmU0OTQ3YTEwNzE3ZGRiMTI4YmQ4MiJ9LCJuYW1lIjoicnVhbnRvbmdjbG91ZCIsImlkIjoiMmQxNjRlNzRmODVkNDIwODhmMjhmNDE0YzAwYjU2YzIifX19fTGCAYUwggGBAgEBMFwwVzELMAkGA1UEBhMCVVMxDjAMBgNVBAgMBVVuc2V0MQ4wDAYDVQQHDAVVbnNldDEOMAwGA1UECgwFVW5zZXQxGDAWBgNVBAMMD3d3dy5leGFtcGxlLmNvbQIBATALBglghkgBZQMEAgEwDQYJKoZIhvcNAQEBBQAEggEAap11Lfz1as3OetDJEhl+b16XXvHWG7OFNyHjjOkM-oB0GU965d02Q+bQaEUMl2uVBgwifpBtI4BYXh1H0JHam4pCEJ5Pb-JiIGppnF06lJ3Cz-77iUIfmmKz7tlGRwg+N5GxGVzXdYj5MeCEYVpasDjc6Dixwz0CuGw+AmE080C-ijreE+Ol+qHW94KoO-I+mXRXUOQ2W29mJvTuzMf3CJkZqZNbU7z+qsyotW81Z-DMY-wNuKcv8etXaM-Bu1CYYp+szPZn0FElEUMn280FAN8QJgqzkU3JjZNdaBBMpccNt62zQtQHIIBarz7J8ROFisnmrhZA9NXjTkz8ZOhk3g=='}
    request = urllib2.Request(url, '', headers2)
    # request.get_method = lambda: 'PUT'
    ss = urllib2.urlopen(request)
    r_read = ss.read()
    s_read = json.loads(r_read)
    return s_read

get_token()