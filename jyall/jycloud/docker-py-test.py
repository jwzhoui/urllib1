# encoding: utf8
import docker
client = docker.Client(base_url='unix:///var/run/docker.sock')
s = client.stats('f720aedf9330da5483c99111ccce4a32eb57fdec1b7d741b026a6c117cc31d45')
print s
# for component,version in client.version().iteritems():
#     print component,version