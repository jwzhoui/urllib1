#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='10.156.128.8',
        port = 3306,
        user='root',
        passwd='openstack',
        db = 'citycloud',
        )
cur = conn.cursor()

#创建数据表
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
depts=cur.execute("select * from demo ")
ss=cur.fetchone()
print depts
print ss
cur.close()
conn.commit()
conn.close()

