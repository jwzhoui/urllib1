#coding=utf-8
import httplib
import json
import random
import time
import MySQLdb
from datetime import datetime
from datetime import timedelta
import requests


def get_cur():
    conn= MySQLdb.connect(
            # host='192.168.87.1',
            host='10.156.128.8',
            port = 3306,
            user='root',
            # passwd='root',
            passwd='openstack',
            db = 'citycloud',
            )
    cur = conn.cursor()
    return  conn ,cur
def get_kw():
    conn = MySQLdb.connect(
        # host='10.16.118.50',
        host='10.156.128.8',
        port=3306,
        user='root',
        passwd='openstack',
        db='keystone',
    )
    cur = conn.cursor()
    return conn, cur

def get_users_info():
    conn,cur=get_kw()
    # depts = cur.execute("SELECT lu.`name` name,u.type type,u.id user_id,u.email email,u.phone phone,u.source source from `user` u,local_user lu where u.id=lu.user_id ")
    #                                                                                                                                                                                               ren
    # depts = cur.execute("SELECT lu.`name` name,u.type type,u.id user_id,u.email email,u.phone phone,u.source source from `user` u,local_user lu where u.id=lu.user_id AND lu.`name` in ('geren')")
    depts = cur.execute("SELECT lu.`name` name,u.type type,u.id user_id,u.email email,u.phone phone,u.source source from `user` u,local_user lu where u.id=lu.user_id AND lu.`name` in ('geren','hzhb01')")
    users_info = cur.fetchmany(depts)
    # cur.close()
    # conn.commit()
    # conn.close()
    return users_info


def get_all_product():
        conn,cur = get_cur()
        depts=cur.execute("select id,name,region,partner,partner_name from product ")
        products=cur.fetchmany(depts)
        # cur.close()
        # conn.commit()
        # conn.close()
        return products



def get_num():
    ar=[1,1,1,3]
    num=random.randint(0, 3)
    return ar[num]


def update_order(order_id,user_info,date):
    # 修改订单数据  确认订单  状态 时间  创建人 拓展字段
    created_by=user_info[0]
    u={"type": user_info[1], "user_id": user_info[2],"email": user_info[3],"phone": user_info[4], "source": user_info[5]}
    extra=json.dumps(u)
    conn,cur = get_cur()
    # sql=" UPDATE `order` set `status` = '0',`created_at` = '%s',`created_by`='%s',`extra`='%s' where id='%s'" %date,created_by,extra,order_id
    sql=" UPDATE `order` set `status` = '0',`created_at` = '%s',`created_by`='%s',`extra`='%s' where id='%s'" %(date,created_by,extra,order_id)
    cur.execute(sql)
    # cur.execute(" update  %s  set   status=%s   where  id  =  %s" %('order','5',order_id))
    conn.commit()

def order_post(data):
        # 定义一个要提交的数据数组(字典)
        # 定义post的地址
        try:
            http_conn = httplib.HTTPConnection('localhost', '19000')
            # auth = base64.b64encode('cleartext admin' + ':' + 'cleartext openstack')
            # rz='cleartext admin'+ ':'+ 'cleartext openstack'
            url = '/orders/qq'
            headers = {'Content-Type': 'application/json; charset=UTF-8',
                        'X-Auth-Token':'c03eebe4712c4d75be3cf4da0fbba5a1',
                       # headers.put("Accept", "application/json");
                       # "Authorization": "Basic " + '87e940c7e6314f2bae4aaeb13a6d834d',
                       }
            datas=json.dumps(data)
            http_conn.request('POST', url,datas, headers=headers,)
            res = http_conn.getresponse()
            order_result = json.loads(res.read())
            order_id=order_result['result']
            #修改订单内数据  时间 创建人  状态
            if order_id ==None or order_id=='':
                return  None
            return  order_id
        except Exception as e:
            print e.message
            return

def get_all_product_infos():
        all_product_infos=[]
        # product_ids=get_all_product()
        product_ids=['65540037-befe-5f74-b3c8-eca55c407fd6','6f754c3d-415b-5748-abf5-1cb8609530a0','49267f82-b40a-5893-9bff-60445f9ff5d8']
        i = 0
        for product in product_ids:
                i=i+1
                # product_id=product[0]
                url = "http://localhost:19000/billing/rules/product?product_id="+product
                product_info=requests.get( url).json()['result']
                product_billing=product_info['product_billing']
                if len(product_billing)>0:
                        for product_billing_info in product_billing :
                                rules=product_billing_info['billingRule']
                                if len(rules)>0:
                                        for rule in rules:
                                                brps=rule['brps']
                                                if len(brps)>0:

                                                      all_product_infos.append({'product':product,'product_info':product_info})
                                                      if len(all_product_infos)>10:
                                                          return all_product_infos
                                                      break
                                break
                print  i
        return all_product_infos


def create_data(product,product_info):
    product_billing = product_info['product_billing']
    if len(product_billing) > 0:
        for product_billing_info in product_billing:
            rules = product_billing_info['billingRule']
            if len(rules) > 0:
                for rule in rules:
                    brps = rule['brps']
                    if len(brps) > 0:

                        brp=brps[random.randint(0, len(brps)-1)]
                        region = product[2]
                        billing_item_id = rule['billing_item_id']
                        name = product[1]
                        pay_mode = brp['cycle']
                        product_id = product
                        # product_id = product[0]
                        price = brp['price']
                        partner = product[3]
                        partner_name = product[4]
                        type = get_num()
                        spec = product_billing_info['spec']
                        data = {"availablezone": region,
                                "order_items": [
                                    {
                                        "billing_item_id": billing_item_id,
                                        "extra":
                                            {
                                                "deleted": "false"
                                            }
                                        ,
                                        "name": name,
                                        "pay_mode": pay_mode,
                                        "price": price,
                                        "product_id": product_id,
                                        "product_type": "2",
                                        "partner": partner,
                                        "partner_name": partner_name,
                                        "count": 1,
                                        "spec" : spec
                                    }
                                ],
                                "price": price,
                                "type": type
                                }
                        return data
def create_order(product, product_info):
    print  0


def get_date():
    #方法: shijian
    a = "2016-12-01 01:40:00"
    #将其转换为时间数组
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    #起始時間转换为时间戳:
    s = int(time.mktime(timeArray))
    #系統當前時間時間錯
    # e=int((time.mktime(time.localtime())))
    b = "2016-12-30 01:40:00"
    # 将其转换为时间数组
    timeArray = time.strptime(b, "%Y-%m-%d %H:%M:%S")
    # 起始時間转换为时间戳:
    e = int(time.mktime(timeArray))

    c=random.randint(s, e)
    time_local = time.localtime(c)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return date


'''

    def project_member_filter(self, **kwargs):
        return ProjectMember.objects.filter(**kwargs)
    #
    #
    # def get_project_member_user_id(self, *project_ids):
    #     cursor = connection.cursor()
    #
    #     cursor.execute(
    #         "SELECT distinct  pm.user_id  FROM project_member pm WHERE pm.project_id in %s and  ISNULL(pm.user_group_id);",
    #         [project_ids]
    #     )
    #     result = cursor.fetchone()
    #     return result
    #
    #
    # def get_project_member_user_group_id(self, *project_ids):
    #     cursor = connection.cursor()
    #
    #     cursor.execute(
    #         "SELECT distinct  pm.user_group_id  FROM project_member pm WHERE pm.project_id in %s and not ISNULL(pm.user_group_id);",
    #         [project_ids]
    #     )
    #     result = cursor.fetchone()
    #     return result

'''

def pay_order(order_id, pay_time):
    # 定义一个要提交的数据数组(字典)
    # 定义post的地址
    try:
        http_conn = httplib.HTTPConnection('localhost', '19000')
        # auth = base64.b64encode('cleartext admin' + ':' + 'cleartext openstack')
        # rz='cleartext admin'+ ':'+ 'cleartext openstack'
        url = '/orders/'+order_id
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'X-Auth-Token': 'c03eebe4712c4d75be3cf4da0fbba5a1',
                   # "Authorization": "Basic " + '87e940c7e6314f2bae4aaeb13a6d834d',
                   }
        datas = json.dumps({})
        http_conn.request('POST', url, body=datas, headers=headers, )
        res = http_conn.getresponse()
        result = res.status
        #修改訂單支付時間
        conn, cur = get_cur()
        sql = " UPDATE `order` set `paid_at` = '%s'where id='%s'" % (
            pay_time,order_id)
        cur.execute(sql)
        #獲取收支表id
        sql = "select er.id from `order` o," \
              " order_items oi,expenses_receipts_detail erd,expenses_receipts er where " \
              "erd.order_item=oi.id and o.id=oi.order_id and er.id=erd.expenses_receipts_id and o.id='%s'" % (
            order_id)
        depts=cur.execute(sql)

        er_ids=cur.fetchmany(depts)
        er_id=None
        for ss in er_ids:
            er_id=ss[0]
        #修改收支表　paid_at時間
        sql = " UPDATE `expenses_receipts` set `paid_at` = '%s' where id='%s'" % (
            pay_time, er_id)
        cur.execute(sql)
        sql = " UPDATE `expenses_receipts_detail` set `paid_at` = '%s' where expenses_receipts_id='%s'" % (
            pay_time, er_id)
        cur.execute(sql)

        conn.commit()
        return result
    except Exception as e:
        print e.message
        return


def approve_order(order_id, approve_time):
    conn, cur = get_cur()
    sql_oi = "select oi.id from `order` o," \
             " order_items oi where " \
             " o.id=oi.order_id  and o.id='%s'" % (
                 order_id)
    depts = cur.execute(sql_oi)

    oi_ids = cur.fetchmany(depts)
    oi_id = None
    for ss in oi_ids:
        oi_id = ss[0]

    # 修改訂單結束時間

    sql = " UPDATE `order` set `end_at` = '%s'where id='%s'" % (
        approve_time, order_id)
    cur.execute(sql)
    conn.commit()

    http_conn = httplib.HTTPConnection('localhost', '19000')
    url = '/orders/' + oi_id +'/action/'
    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'X-Auth-Token': 'c03eebe4712c4d75be3cf4da0fbba5a1',
               # "Authorization": "Basic " + 'c03eebe4712c4d75be3cf4da0fbba5a1',
               }
    datas = json.dumps({ "approveOrder" : {
      "notes" : {
         "productParameters" : [
            {
               "label" : "用户名",
               "name" : "name",
               "value" : "admin"
            },
            {
               "label" : "url",
               "name" : "url",
               "value" : "www.baidu.com"
            }
         ]
      }
   }})
    http_conn.request('POST', url, datas, headers=headers, )
    res = http_conn.getresponse()



def main_():

    users_info=get_users_info()
    all_product_infos = get_all_product_infos()

    for pi in all_product_infos:
        print  pi['product'][0]
    u=[0,0,0,1]
    lenn=len(all_product_infos)
    print  '有效产品数==' + lenn.__str__()
    #geshu
    for i in range(0,2):
    # for i in range(0,1400):
        product_infos_product =  all_product_infos[random.randint(0, len(all_product_infos)-1)]
        product_info = product_infos_product['product_info']
        product = product_infos_product['product']
        data=create_data(product, product_info)
        # 生成订单
        order_id = order_post(data)
        if order_id == None:
            continue
        # print 'order_id==' + order_id
        # 修改订单数据  确认订单  状态 时间  创建人 拓展字段
        date = get_date()
        # user_info=users_info[0]
        user_info=users_info[u[random.randint(0, len(u)-1)]]

        update_order(order_id,user_info,date)
        #zf
        date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        aH = timedelta(hours=1)
        pay_time = date_time + aH
        pay_order(order_id,pay_time)
        #處理
        approve_time = date_time + aH*2
        approve_order(order_id,approve_time)
        print i + 1, user_info[0],  order_id,approve_time
    #模拟每天定时任务

main_()






