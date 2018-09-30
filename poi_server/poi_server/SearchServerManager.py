# coding: utf-8
import requests
import traceback

import settings
from public.logger import simple_log
import time
logger = simple_log()


class SearchServerManager(object):
    # String strReqUrl,HashMap<String, String> reqParamsMap,String strReqPath
    def handle_sear_server_request(self, str_req_url,str_req_path,req_params_map={}):
        """
        向搜索服务发送请求
        :param str_req_url:
        :param req_params_map:
        :param str_req_path:
        :return:
        """
        try:
            search_server_ip = settings.SEARCH_SERVER_IP
            search_server_port = settings.SEARCH_SERVER_PORT
            str_url = 'http://%s:%s%s?channel=poi'%(search_server_ip,search_server_port,str_req_path)
            if str_req_url:
                str_url+='&%s'%str_req_url
            else:
                for key,value in req_params_map.iteritems():
                    str_req_url+='&%s=%s'%(key,value)
            response = requests.request('GET', str_req_url, timeout=20000)
            status = response.status_code
            if status == 200:
                return  response.text
            else:
                logger.error('request url get error code:%s url:%d'%(status,str_req_url));
        except:
            logger.error(traceback.format_exc())


































