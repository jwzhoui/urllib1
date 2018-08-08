# -*- coding: UTF-8 -*-

from solrcloudpy.connection import SolrConnection
from solrcloudpy.parameters import SearchOptions

conn= SolrConnection(server=["192.168.200.128:8081", "192.168.200.128:8084", "192.168.200.128:8082", "192.168.200.128:8083"])
collection=conn.create_collection('citycloudProduct',num_shards=1,replication_factor=2)
docs = [{"id":"cclina", "min_price":"11111"}]
ww=conn['citycloudProduct'].add(docs)
conn['citycloudProduct'].commit()
se=SearchOptions()
se.commonparams.q("id:cclina").rows(10).fl("id,name")
response=conn['citycloudProduct'].search(se)
# for hit in response.result.response.docs:

        # print hit['id'],hit['text_url']
