# -*- coding: UTF-8 -*-
import base64
import urllib
import bs4
import json
from solrcloudpy.connection import SolrConnection
from solrcloudpy.parameters import SearchOptions





'''
添加
'''
try:
    conn = SolrConnection(
        server=["192.168.200.128:8081", "192.168.200.128:8084", "192.168.200.128:8082", "192.168.200.128:8083"])
    collection=conn.create_collection('citycloudProduct',num_shards=1,replication_factor=2)
    iii={"id":"cc", "name":"恭喜发财"}
    docs = [iii]
    ww=conn['citycloudProduct'].add(docs)
    i=conn['citycloudProduct'].commit()
    print  i

    se=SearchOptions()
    se.commonparams.q("id:cclina").rows(10).fl("id,name")
    response=conn['citycloudProduct'].search(se)
    for hit in response.result.response.docs:

        print hit['id'],hit['name']
except Exception as e:
    print 'solr服务器链接错误或选取solrhome有误. error: %s' % e.message