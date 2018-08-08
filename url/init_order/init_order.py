#coding=utf-8
import MySQLdb
import urllib2
import urllib

conn= MySQLdb.connect(
        host='192.168.87.1',
        port = 3306,
        user='root',
        passwd='root',
        db = 'citycloud',
        )
cur = conn.cursor()


depts=cur.execute("select * from product ")
ss=cur.fetchmany(depts)
print depts
print ss
cur.close()
conn.commit()
conn.close()


# 定义一个要提交的数据数组(字典)
data = {}
data['username'] = 'zgx030030'
data['password'] = '123456'

# 定义post的地址
url = 'http://www.test.com/post/'
post_data = urllib.urlencode(data)

# 提交，发送数据
req = urllib2.urlopen(url, post_data)

# 获取提交后返回的信息
content = req.read()
