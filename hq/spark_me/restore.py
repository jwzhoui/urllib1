# coding:utf-8
import os
import sys

import time
import datetime

def rsync_log_tj_php(start_day,nu):
    d1 = datetime.datetime.strptime(start_day, '%Y-%m-%d')
    for i in range(nu):
        delta = datetime.timedelta(days=i)
        n_days = d1 + delta
        day = n_days.strftime('%Y-%m-%d')
        rsync = 'rsync -avz haoqiao@172.16.24.176:/data/logs_2b/logs_check/log-tj-%s.php /data/duanyr/spark/offline_log/'%day
        print rsync
        # os.system(rsync)
        # time.sleep(20)
        spark = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit --master spark://172.16.22.55:7077  \
    --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
    --jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class web_list_page_stat.StatWebListPage  \
    /home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebListPage.jar StatWebListUserClick %s >> /data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/log/search_stat/StatWebListUserClick.log'%day
        # os.system(spark)
        print spark

def rsync_log(start_day,nu):
    d1 = datetime.datetime.strptime(start_day, '%Y-%m-%d')
    for i in range(nu):
        delta = datetime.timedelta(days=i)
        n_days = d1 + delta
        day = n_days.strftime('%Y-%m-%d')
        rsync = 'rsync -avz haoqiao@172.16.20.93:/data/online/hq-hotel-price/log/info.log.%s /data/duanyr/spark/offline_log/' % day
        print rsync
        # v = os.system(rsync)


def exe_d():
    d1 = datetime.datetime.strptime('2018-10-23', '%Y-%m-%d')
    for i in range(6):
        delta = datetime.timedelta(days=i)
        n_days = d1 + delta
        day = n_days.strftime('%Y-%m-%d')
        statSupplierRecall = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
--master spark://172.16.22.55:7077  --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
--jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class b_detail_page_stat.StatWebDetailPage  \
/home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebDetailPage_jw2.jar  StatSupplierRecall %s ' % day


        statSupplierRecallOnImpatienceRequest = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
--master spark://172.16.22.55:7077  --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
--jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class b_detail_page_stat.StatWebDetailPage  \
/home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebDetailPage_jw2.jar  statSupplierRecallOnImpatienceRequest %s ' % day



        print statSupplierRecall
        v = os.system(statSupplierRecall)
        print statSupplierRecallOnImpatienceRequest
        v = os.system(statSupplierRecallOnImpatienceRequest)


def exe_w():
    d1 = datetime.datetime.strptime('2018-10-29', '%Y-%m-%d')
    for i in range(5):
        delta = datetime.timedelta(days=i)
        n_days = d1 + delta
        day = n_days.strftime('%Y-%m-%d')
        statSupplierRecall = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
--master spark://172.16.22.55:7077  --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
--jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class b_detail_page_stat.StatWebDetailPage  \
/home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebDetailPage_jww.jar  StatSupplierRecall %s ' % day

        statSupplierRecallOnImpatienceRequest = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
--master spark://172.16.22.55:7077  --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
--jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class b_detail_page_stat.StatWebDetailPage  \
/home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebDetailPage_jww.jar  statSupplierRecallOnImpatienceRequest %s ' % day

        print statSupplierRecall
        v = os.system(statSupplierRecall)
        print statSupplierRecallOnImpatienceRequest
        v = os.system(statSupplierRecallOnImpatienceRequest)



# while True:
#     b = time.time()
#     print b
#     #      1541196000
#     if b > 1541196000:
#         exe_d()
#         exe_w()
#         print 2
#         sys.exit(0)
#     else:
#         time.sleep(3600)
#         print 1
#

def exe_d():
    d1 = datetime.datetime.strptime('2018-11-02', '%Y-%m-%d')
    for i in range(4):
        delta = datetime.timedelta(days=i)
        n_days = d1 + delta
        day = n_days.strftime('%Y-%m-%d')
        statSupplierRecallOnImpatienceRequest = '/data/duanyr/spark/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
--master spark://172.16.22.55:7077  --conf spark.port.maxRetries=100  --executor-cores 2 --total-executor-cores 8 --executor-memory 2G \
--jars /home/duanyingrong/jars/mysql_connector_jars/mysql-connector-java-5.1.45-bin.jar,/home/duanyingrong/jars/jedis_jars/jedis-2.9.0.jar,/home/duanyingrong/jars/json_lib_jars/json-lib-2.4-jdk15.jar,/home/duanyingrong/jars/json_lib_jars/commons-beanutils-1.8.0.jar,/home/duanyingrong/jars/json_lib_jars/commons-collections-3.2.1.jar,/home/duanyingrong/jars/json_lib_jars/commons-lang-2.4.jar,/home/duanyingrong/jars/json_lib_jars/commons-logging-1.0.4.jar,/home/duanyingrong/jars/json_lib_jars/ezmorph-1.0.6.jar,/home/duanyingrong/jars/json_lib_jars/json-20070829.jar  --class b_detail_page_stat.StatWebDetailPage  \
/home/duanyingrong/spark/spark-2.2.0-bin-hadoop2.7/duan_test/java_jars/StatFromWebDetailPage_d1.jar  StatSupplierRecallOnImpatienceRequest %s' % day

        print statSupplierRecallOnImpatienceRequest
        # v = os.system(statSupplierRecallOnImpatienceRequest)


exe_d()















