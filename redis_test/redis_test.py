#coding:utf-8
#!/
from datetime import datetime

from rediscluster import StrictRedisCluster
import sys




SS = {
    "index:ispublic:true": [
        "beehive/粮库系统基础服务",
        "beehive/粮库计划管理服务",
        "beehive/粮库合同管理服务",
        "beehive/粮库出入库通知单服务",
        "beehive/粮库业务进度查询服务",
        "beehive/粮库客户管理服务",
        "beehive/智能安防服务",
        "beehive/远程监管基础服务",
        "beehive/远程视频监控服务",
        "beehive/远程粮情监测服务",
        "beehive/远程仓储作业服务",
        "beehive/远程储粮信息服务",
        "beehive/仓储业务管理服务",
        "beehive/仓储业务质量服务",
        "beehive/仓储业务数量服务",
        "beehive/仓储业务费用服务",
        "beehive/工作流服务",
        "beehive/粮情查询追溯服务",
        "beehive/粮库出入库服务",
        "beehive/智能仓房管理服务",
        "beehive/填报引擎服务",
        "beehive/填报模板定义服务",
        "beehive/填报数据上报服务",
        "beehive/国内市场监测服务",
        "beehive/应急保障管理服务",
        "beehive/应急预案管理服务",
        "beehive/粮油加工统计服务",
        "beehive/粮油加工业技术改造服务",
        "beehive/粮食流通基础设施投资统计服务",
        "beehive/仓储管理服务",
        "beehive/全国粮食监督检查服务",
        "beehive/粮油标准质量管理服务",
        "beehive/放心粮油工程信息服务",
        "beehive/局内公文服务",
        "beehive/工作动态服务",
        "beehive/信息报送服务",
        "beehive/综合管理服务",
        "beehive/调控管理服务",
        "beehive/监督检查服务",
        "beehive/财务管理服务",
        "beehive/流通发展服务",
        "beehive/查询分析服务",
        "beehive/数据查询管理",
        "beehive/政务协同系统设置服务",
        "beehive/政务协同用户管理服务",
        "beehive/粮油生产分析服务",
        "beehive/供需平衡分析服务",
        "beehive/市场形势分析服务",
        "beehive/省级储备分析服务",
        "beehive/应急保障分析服务",
        "beehive/项目投资分析服务",
        "beehive/仓储设施分析服务",
        "beehive/加工业转化分析服务",
        "beehive/国有粮食企业分析服务",
        "beehive/经济运行分析服务",
        "beehive/行业主体分析服务",
        "beehive/粮食收购分析服务",
        "beehive/省级储备粮分析服务",
        "beehive/市县级储备粮分析服务",
        "beehive/应急管理分析服务",
        "beehive/流通统计分析服务",
        "beehive/市场监测分析服务",
        "beehive/交易分析服务",
        "beehive/库存检查分析服务",
        "beehive/行政执法分析服务",
        "beehive/专业人才分析服务",
        "beehive/体系建设分析服务",
        "beehive/诚信档案分析服务",
        "beehive/投资项目分析服务",
        "beehive/仓储设施统计分析服务",
        "beehive/粮食加工统计分析服务",
        "beehive/粮油质量分析服务",
        "beehive/仓储单位备案分析服务",
        "beehive/安全生产分析服务",
        "beehive/Gis服务",
        "beehive/报表查询分析服务",
        "beehive/采集数据源服务",
        "beehive/元数据管理服务",
        "beehive/数据标签服务",
        "beehive/采集定义服务",
        "beehive/采集数据清洗服务",
        "beehive/采集任务服务",
        "beehive/采集监控服务",
        "beehive/物联网数据采集服务",
        "beehive/大数据存储引擎服务",
        "beehive/大数据计算引擎服务",
        "beehive/大数据处理引擎服务",
        "beehive/数据目录管理服务",
        "beehive/数据安全管理服务",
        "beehive/数据日志管理服务",
        "beehive/OLAP分析服务",
        "beehive/海量数据分析服务",
        "beehive/实时交互查询服务",
        "beehive/大数据可视化引擎服务",
        "beehive/数据共享服务",
        "beehive/数据交换服务",
        "beehive/数据访问流程服务",
        "beehive/MySql服务",
        "beehive/oracle服务",
        "beehive/redis服务",
        "beehive/NongoDB服务",
        "beehive/postgresql服务",
        "beehive/Neo4J服务",
        "beehive/influxdb服务",
        "beehive/空间与项目管理",
        "beehive/项目生命周期管理",
        "beehive/流水线持续发布管理",
        "beehive/代码与构件库管理",
        "beehive/云服务器管理",
        "beehive/容器管理",
        "beehive/应用管理",
        "beehive/产品管理",
        "beehive/订单管理",
        "beehive/计费管理",
        "beehive/服务监控",
        "beehive/告警模板设置",
        "beehive/运维管理",
        "beehive/Java开发服务",
        "beehive/PHP开发服务",
        "beehive/Go开发服务",
        "beehive/Ruby开发服务",
        "beehive/Python开发服务",
        "beehive/Node.js开发服务"
    ]
}
# REDIS={
#     'host':'10.16.117.24',
#     'port':6379,
#     'password':123456,
#     'max_connections':8,
#     'db':1
# }
REDIS={
    'host':'127.0.0.1',
    'port':6379,
    'password':123456,
    'max_connections':8,
    'db':1
}
def redis_cluster():
    redis_nodes =  [ {'host': '10.156.129.7', 'port': 8001},
                    {'host': '10.156.129.8', 'port': 8002},
                    {'host': '10.156.129.9', 'port': 8003},
                   ]
    try:
        kwargs={'password':'123456'}
        redisconn = StrictRedisCluster(max_connections=8,host='10.156.129.9',port='8003',**kwargs)
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)
    redisconn.set('name','admin')
    redisconn.set('age',18)
    print "name is: ", redisconn.get('name')
    print "age  is: ", redisconn.get('age')

    when = u'2017-11-06T04:04:37.256701Z'

    # 把字符串转成datetime
    # when_datetime= datetime.strptime(when, "%Y-%m-%d-%H")
    # redisconn.expireat('name',when)


# redis_cluster()