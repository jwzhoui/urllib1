# encoding=utf-8

from selenium import webdriver


obj = webdriver.PhantomJS()  # 加载网址
obj.get('http://bj.58.com/chuzu/1/pn2/?key=北关东路')  # 打开网址
print obj.page_source  # 截图保存
obj.quit()  # 关闭浏览器。当出现异常时记得在任务浏览器中关闭PhantomJS，因为会有多个PhantomJS在运行状态，影响电脑性能