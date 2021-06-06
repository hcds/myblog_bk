#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime

from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordInfoRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest

# 阿里云 Access Key ID
access_key_id = ""
# 阿里云 Access Key Secret
access_key_secret = ""
# 阿里云 一级域名
rc_domain = ''
# 返回内容格式
rc_format = 'json'

"""
获取域名的解析信息
"""
def check_records(dns_domain):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(dns_domain)
    request.set_accept_format(rc_format)
    result = clt.do_action_with_exception(request)
    result = json.JSONDecoder().decode(result.decode('utf-8'))
    return result

"""
根据域名解析记录ID查询上一次的IP记录
"""
def get_old_ip(record_id):
    clt = client.AcsClient(access_key_id,access_key_secret,'cn-hangzhou')
    request = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
    request.set_RecordId(record_id)
    request.set_accept_format(rc_format)
    result = clt.do_action_with_exception(request)
    result = json.JSONDecoder().decode(result.decode('utf-8'))
    result = result['Value']
    return result

"""
更新阿里云域名解析记录信息
"""
def update_dns(dns_rr, dns_type, dns_value, dns_record_id, dns_ttl, dns_format):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RR(dns_rr)
    request.set_Type(dns_type)
    request.set_Value(dns_value)
    request.set_RecordId(dns_record_id)
    request.set_TTL(dns_ttl)
    request.set_accept_format(dns_format)
    result = clt.do_action_with_exception(request)
    return result

"""
通过 ip.cn 获取当前主机的外网IP
"""
def get_my_publick_ip():
    url = urllib.request.urlopen("https://jsonip.com")
    text = url.read()  
    get_ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    ip = get_ip_pattern.findall(text.decode('utf-8'))
    print("ip: ", ip[0])
    return ip[0]

def write_to_file(new_ip):
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    write_log = open('aliyun_ddns.txt', 'a')
    write_log.write(time_now + ' ' + str(new_ip) + '\n')
    return

if __name__ == '__main__':
    # # 之前的解析记录
    old_ip = ""
    record_id = ""
    dns_records = check_records(rc_domain)
    for record in dns_records["DomainRecords"]["Record"]:
        if record["Type"] == 'A':
            record_id = record["RecordId"]
            print("aidashuai.top recordID is {}".format(record_id))
            if record_id != "":
                old_ip = get_old_ip(record_id)
                # 获取主机当前的IP
                now_ip = get_my_publick_ip()
                print("now host ip is {}, dns ip is {}".format(now_ip, old_ip))
                if old_ip == now_ip:
                    print("The specified value of parameter Value is the same as old")
                else:
                    rc_rr = record["RR"]       # 解析记录
                    rc_type = record["Type"]   # 记录类型, DDNS填写A记录
                    rc_value = now_ip           # 新的解析记录值
                    rc_record_id = record_id    # 记录ID
                    rc_ttl = '600'              # 解析记录有效生存时间TTL,单位:秒

                    print(update_dns(rc_rr, rc_type, rc_value, rc_record_id, rc_ttl, rc_format))

                    write_to_file(now_ip)
