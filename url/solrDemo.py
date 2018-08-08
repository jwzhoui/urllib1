import  solr



s = solr.SolrConnection('http://192.168.200.129:8080/solr/citycloud')

result = s.select("*:*")
ss = result['response']
list = ss['docs']
print result
for r in list:
     print r
     print r['id']


