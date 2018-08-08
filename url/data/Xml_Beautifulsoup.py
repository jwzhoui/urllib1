
# -*- coding: utf-8 -*-
import re
import urllib

import requests
import bs4



xml='<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg><appid><![CDATA[wxc1eea2c03e1b0ea4]]></appid><mch_id><![CDATA[1483045472]]></mch_id><device_info><![CDATA[WEB]]></device_info><nonce_str><![CDATA[msiOuMhXRtKERmms]]></nonce_str><sign><![CDATA[487C999683ED15B4DFBD871BF51A7E04]]></sign><result_code><![CDATA[SUCCESS]]></result_code><prepay_id><![CDATA[wx20170818155250c693f8699c0592169596]]></prepay_id><trade_type><![CDATA[NATIVE]]></trade_type><code_url><![CDATA[weixin://wxpay/bizpayurl?pr=5BbkeUo]]></code_url></xml>'


def trans_xml_to_dict(xml):
    """
       将微信支付交互返回的 XML 格式数据转化为 Python Dict 对象

       :param xml: 原始 XML 格式数据
       :return: dict 对象
       """

    soup = bs4.BeautifulSoup(xml, features='xml')
    xml = soup.find('xml')
    if not xml:
        return {}

    # 将 XML 数据转化为 Dict
    data = dict([(item.name, item.text) for item in xml.find_all()])
    return data



ss=trans_xml_to_dict(xml)


