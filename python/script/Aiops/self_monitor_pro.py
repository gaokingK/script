#!/usr/bin/env python
# -*- coding:utf-8 -*-
#中台：告警辨析+日志精析
#es：日志：张江+石泉
import sys
reload(sys)
sys.path.insert(0,'/opt/sharplook/scripts/pro_self_monitor/site-packages/')
sys.setdefaultencoding('utf-8')
import re
import os
import json
import pymysql
import commands
import requests 
from datetime import datetime
def get_cookies(url,user,passwd):
    try:
        data = {
            "enableLDAP": False,
            "password": passwd,
            "userName": user
        }
        headers = {"content-type": "application/json"}
        res = requests.post(url=url, json=data, headers=headers)
    except Exception as e:
        print("登录sso失败，{}".format(e))
        exit(1)
    else:
        return res.cookies
def monitor_collect():
    """获取每次要检查的采集任务ID,查询带APPLOG的任务,按序每次查询6个"""
    sql = "select dataSetId from collectCenter where topicName like '%APP%' group by dataSetId,topicName order by dataSetId;"
    cursor.execute(sql)
    dataSetId_list = cursor.fetchall()
    #if collect_index == "":
    if os.path.isfile("index.txt"):
      file = open("index.txt", "r")
      collect_index = int(file.read())
      file.close
    else:
      collect_index = 0
    next_index = collect_index + 1
    max_index = len(dataSetId_list)/6 + 1
    if next_index >= max_index:
       next_index = 0
    file = open("index.txt", "w")
    file.write(str(next_index))
    file.close
    itoaflow = [1,2,3,4,5,6]
    i = 0
    j = 6 * collect_index
    while i < 6:
      if j < len(dataSetId_list):
        itoaflow[i] = dataSetId_list[j][0]
      i+=1
      j+=1
    """检查采集任务中的agent是否采集数据"""
    payload = {
        "dbType": "ElasticSearch",
        "query": "search source=zjiopses:mave_monitor* ,sqiopses:mave_monitor*  (`process_name`^='itoa-flow') (`process_name`='itoa-flow-"+str(itoaflow[0])+"' OR `process_name`='itoa-flow-"+str(itoaflow[1])+"' OR `process_name`='itoa-flow-"+str(itoaflow[2])+"' OR `process_name`='itoa-flow-"+str(itoaflow[3])+"' OR `process_name`='itoa-flow-"+str(itoaflow[4])+"' OR `process_name`='itoa-flow-"+str(itoaflow[5])+"')  @timestamp >= 'now-2h' |stats max(`send_lines`) as max_lines,min(`send_lines`) as min_lines by `ip`  (size=60000), `process_name` (size=60000) | eval `div`=`max_lines`-`min_lines` | table `ip`,`process_name`,`div`",
        "format": "std"
    }
    headers = {"content-type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers).json()
    res = response.get('aggs',{}).get('aggs')
    # 遍历每一条记录
    for each in res:
        # 获取IP
        ip = each.get("ip")
        # 获取process_name
        process_name = each.get("process_name")
        # 根据process_name得到采集任务ID
        dataSetId = int(process_name.split('-')[-1])
        # 根据采集任务ID查询数据库，获取采集任务名称
        sql = "select dataSetName from datasetCollect where dataSetId={}".format(dataSetId)
        cursor.execute(sql)
        each["dataSetName"] = cursor.fetchone()[0]
        # 根据采集任务ID查询数据库，获取索引名称
        index_name = get_index_name(dataSetId)
        # 查询索引中，agent ip是否存在
        index_ip = 1 if get_index_ip(index_name, ip) else 0
        # print ip,each["dataSetName"],index_name,index_ip
        each["index"] = index_name
        each["index_ip"] = index_ip
        each["data_type"] = "collect"
        f.write(json.dumps(each, ensure_ascii=False, encoding='utf-8') + '\n')

def get_index_ip(index_name, ip):
    """获取索引是否存在该IP"""
    SPL = "index={}* @timestamp >= 'now-1d/d' @ip='{}'".format(index_name,ip)
    payload = {
        "dbType": "ElasticSearch",
        "query": SPL,
        "format": "std"
    }
    headers = {"content-type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers).json()
    res = response.get('events',{}).get('total')
    return res
    
    
def get_index_name(task_id):
    """获取索引名称"""

    # 通过采集任务ID获取解析任务ID
    sql = "select streamid from streamCenter where inDataSetId={}".format(task_id)
    cursor.execute(sql)
    stream_info = cursor.fetchone()
    if stream_info:
        stream_id = stream_info[0]
        # 通过解析任务ID获取存储任务索引名称
        sql2 = "select dataSetName from streamingDataSet where inDataSetId={}".format(stream_id)
        cursor.execute(sql2)
        data = cursor.fetchone()
        index_name = data[0] if data else None
    else:
        # 通过采集任务ID获取存储任务索引名称
        sql2 = "select dataSetName from streamingDataSet where inDataSetId={}".format(task_id)
        cursor.execute(sql2)
        data = cursor.fetchone()
        index_name = data[0] if data else None

    return index_name
    
def monitor_index_config():
    """检查索引配置是否合理"""
    #sql = "select dataSetName,dataSetAlias,json_extract(advanceConfig,'$.store[0].esTemplate') from streamingDataSet"
    # 遍历数据库，获取所有的存储任务名称、索引、存储配置
    sql = "select dataSetName,dataSetAlias,json_extract(advanceConfig,'$.store') from streamingDataSet"
    cursor.execute(sql)
    data = cursor.fetchall()
    #data = cursor.fetchone()
    print(data)
    for each in data:
        try:
            dataSetName,dataSetAlias,store = each
            # 遍历存储配置
            for each2 in json.loads(store):
                centerID = each2.get("centerId")
                #shards_num = int(json.loads(each2.get("esTemplate")).get("settings",{}).get("index",{}).get("number_of_shards"))
                if centerID == 754275092074496:
                    execute_shell = sh_curl_shell.format(dataSetName)
                    index_info = commands.getoutput(execute_shell)
                    index_size =  index_info.split()[-1]
                    shards_num = int(index_info.split()[-6])
                    if index_size[-2:] == 'kb':
                        one_shard_size = int(float(index_size[:-2])) / shards_num
                        suggestion_shards_num = int(float(index_size[:-2])) / 35
                    elif index_size[-2:] == 'tb':
                        one_shard_size = int(float(index_size[:-2])) * 1024 / shards_num
                        suggestion_shards_num = int(float(index_size[:-2])) * 1024 / 35
                    else:
                        one_shard_size = 0
                        suggestion_shards_num = 1
                    data = {
                        "data_type": "index_conf",
                        "indexName": dataSetName,
                        "taskName": dataSetAlias,
                        "one_shard_size": one_shard_size,
                        "shardNum": shards_num,
                        "sugShardNum": suggestion_shards_num,
                        "center": '张江数据中心'
                    }
                if centerID == 764284838682624:
                    execute_shell = sh_curl_shell.format(dataSetName)
                    index_info = commands.getoutput(execute_shell)
                    index_size =  index_info.split()[-1]
                    shards_num = int(index_info.split()[-6])
                    if index_size[-2:] == 'kb':
                        one_shard_size = int(float(index_size[:-2])) / shards_num
                        suggestion_shards_num = int(float(index_size[:-2])) / 35
                    elif index_size[-2:] == 'tb':
                        one_shard_size = int(float(index_size[:-2])) * 1024 / shards_num
                        suggestion_shards_num = int(float(index_size[:-2])) * 1024 / 35
                    else:
                        one_shard_size = 0
                        suggestion_shards_num = 1
                    data = {
                        "data_type": "index_conf",
                        "indexName": dataSetName,
                        "taskName": dataSetAlias,
                        "one_shard_size": one_shard_size,
                        "shardNum": shards_num,
                        "sugShardNum": suggestion_shards_num,
                        "center": '石泉数据中心'
                    }
                f.write(json.dumps(data, ensure_ascii=False, encoding='utf-8') + '\n')
        except:
            continue
           
def agent_monitor():
    sql = "select agent_id, ip, server_ip, connection, now() as now, from_unixtime(floor(lasthb_time/1000)) as last, floor(unix_timestamp(now()) - lasthb_time/1000) as sub  from tbl_agent where connection=2"
    cell_cursor.execute(sql)
    data = cell_cursor.fetchall()
    for each in data:
        agent_id,ip,server_ip,connection,now,last,sub = each
        data = {
            "agent_id": agent_id,
            "ip": ip,
            "server_ip": server_ip,
            "connection": connection,
            "now": str(now),
            "last": str(last),
            "sub": str(sub),
            "data_type": "agentMonitor"
        }
        f.write(json.dumps(data, ensure_ascii=False, encoding='utf-8') + '\n')

def get_pipeline_info(jaxUrl, pipelineInfoFile, pipelineType, cookies, pipelineStatus, recoveryRetry):
    """
    请求jax获取Pipline列表,并返回运行异常的pipeline信息
    :param pipelineType: str or list,pipeline类型,单个为str,多个为数组，不传参默认为所有类型
    :return: list,运行异常的所有pipeline信息
    """
    params = {"type": pipelineType}
    res = requests.get(jaxUrl, params=params, cookies=cookies).json()
    entity = res.get("entity", "")
    if entity:
        # 遍历所有pipeline
        for pipeline in entity:
            try:
                # 获取pipeline字段数据
                pipelineName = pipeline.get("pipelineName")
                # 根据pipelineName生成appName
                appName = app_name(pipelineName)
                taskName = pipeline.get("pipeDescription")
                # 组装pipelne运行数据
                dataInfo = {
                    "pipelineName": pipelineName,
                    "appName": appName,
                    "taskName": taskName,
                    "pipelineStatus": pipeline.get("pipelineStatus"),
                    "internalStatus": pipeline.get("internalStatus"),
                    "data_type": "pipelineMonitor"
                }
                # pipeline运行数据写入文件
                f.write(json.dumps(dataInfo, ensure_ascii=False, encoding='utf-8') + '\n')
                if pipeline.get("pipelineStatus") in pipelineStatus:
                    recoveryInfo = {
                        "appName": appName,
                        "pipelineName": pipelineName,
                        "pipelineStatus": pipeline.get("pipelineStatus"),
                        "taskName": taskName,
                        "internalStatus": pipeline.get("internalStatus"),
                        "data_type": "pipelineRecovery"
                    }
                    pipelineStart = start_pipeline(pipelineName, recoveryRetry, 0)
                    if pipelineStart == 1:
                        print("作业{}自愈失败，请检查！！！".format(pipelineName, taskName))
                        recoveryInfo.update({
                            "msg": "{}{}任务异常，自愈失败，请检查！！！".format(appName, pipelineName),
                            "recovery": "failed"
                        })
                    else:
                        print("作业{}自愈成功。".format(pipelineName, taskName))
                        recoveryInfo.update({
                            "msg": "{}{}任务异常，已自愈启动。".format(appName, pipelineName),
                            "recovery": "success"
                        })
                    # 自愈记录写入文件
                    f.write(json.dumps(recoveryInfo, ensure_ascii=False, encoding='utf-8') + '\n')
            except Exception as e:
                print("[get_pipeline_info]{}。".format(e))
                continue

def start_pipeline(pipelineName, recoveryRetry, initNum):
    """
    启动pipeline
    :param pipelineName: str,pipeline名称
    :param recoveryRetry: int,恢复pipeline运行的重试次数
    :param initNum: int,pipeline恢复次数的初始值,默认为0,不要修改
    :return: int,pipeline是否启动成功,0:成功,1,失败
    """
    try:
        # 重试次数-1
        recoveryRetry -= 1
        initNum += 1
        # 拼接pipeline url
        url = jaxUrl + pipelineName + '/start'
        # 请求并返回
        result = requests.put(url,cookies=cookies).json()
        entity = result.get("entity")
        # 返回数据存在,且pipelineName相同，则启动成功
        if entity and entity.get('pipelineName') == pipelineName:
            print("作业{}第{}次启动成功.".format(pipelineName, initNum))
            pipelineStart = 0
        else:
            print("作业{}第{}次启动失败,{}.".format(pipelineName, initNum, result))
            pipelineStart = 1
    except Exception as e:
        #print("[start_pipeline]作业{}第{}次启动失败,{}.".format(pipelineName, initNum, e))
        pipelineStart = 1
    finally:
        # 如果创建失败且重试次数不为0，则递归执行，直到重试次数为0
        if pipelineStart == 1 and recoveryRetry > 0:
            start_pipeline(pipelineName, recoveryRetry, initNum)
        return pipelineStart
        

def app_name(pipelineName):
    """
    根据pipelineNam生成appName
    :param pipelineName: str,pipelineName
    :return: str,appName
    """
    try:
        if pipelineName.startswith("eoi_itoa"):
            appName = "日志精析"
        elif pipelineName.startswith("Refiner"):
            appName = "告警辨析"
        elif pipelineName.startswith("sensor"):
            appName = "指标解析"
        elif pipelineName.startswith("insper"):
            appName = "日志速析"
        else:
            appName = "其它"
    except Exception as e:
        print("[app_name]生成appName异常,{}。".format(e))
    else:
        return appName


def kafka_group_lag_zj():
    response = requests.get('http://10.239.84.77:18000/v3/kafka/local/consumer')
    consumers = json.loads(response.content).get('consumers')
    if consumers:
        for echo in consumers:
            try:
                response = requests.get('http://10.239.84.77:18000/v3/kafka/local/consumer/{}/lag'.format(echo))
                msg = response.content
                group = json.loads(response.content).get('status').get('group')
                lag = json.loads(response.content).get('status').get('totallag')
                group_status = json.loads(response.content).get('status').get('status')
                partition_count = json.loads(response.content).get('status').get('partition_count')

                #连接中台mysql数据库，关联数据
                db = pymysql.connect(host='10.239.207.19',port=3311,user='znyw',password='Hello123#',db='jax',charset='utf8')
                cursor = db.cursor()
                sql_topic_select = "select * from (select replace(json_extract(pipeline_config,'$.jobs[0].jobConfig.\"group.id\"'),'\"','') as groupId,json_extract(pipeline_config,'$.jobs[0].jobConfig.topics') as source_topics,pipeline_status,pipe_description from tb_pipeline) a where a.groupId='"+ group +"'"
                cursor.execute(sql_topic_select)
                data = cursor.fetchall()

                for each in data:
                   each_list=list(each)
                   final_data = {
                       "groupId":each_list[0],
                       "source_topic":each_list[1],
                       "pipline_status":each_list[2],
                       "pipline_name":each_list[3],
                       "lag":lag,
                       "group_status":group_status,
                       "partition_count":partition_count,
                       "data_type":"kafkaLagMonitor"
                   }
                   #print{json.dumps(final_data, ensure_ascii=False, encoding='utf-8')}
                   f.write(json.dumps(final_data, ensure_ascii=False, encoding='utf-8') + '\n')
                cursor.close()
                db.close()

            except:
                continue


def kafka_group_lag_sq():
    response = requests.get('http://10.239.84.77:18001/v3/kafka/local/consumer')
    consumers = json.loads(response.content).get('consumers')
    if consumers:
        for echo in consumers:
            try:
                response = requests.get('http://10.239.84.77:18001/v3/kafka/local/consumer/{}/lag'.format(echo))
                msg = response.content
                group = json.loads(response.content).get('status').get('group')
                lag = json.loads(response.content).get('status').get('totallag')
                group_status = json.loads(response.content).get('status').get('status')
                partition_count = json.loads(response.content).get('status').get('partition_count')

                #连接中台mysql数据库，关联数据
                db = pymysql.connect(host='10.239.207.19',port=3311,user='znyw',password='Hello123#',db='jax',charset='utf8')
                cursor = db.cursor()
                sql_topic_select = "select * from (select replace(json_extract(pipeline_config,'$.jobs[0].jobConfig.\"group.id\"'),'\"','') as groupId,json_extract(pipeline_config,'$.jobs[0].jobConfig.topics') as source_topics,pipeline_status,pipe_description from tb_pipeline) a where a.groupId='"+ group +"'"
                cursor.execute(sql_topic_select)
                data = cursor.fetchall()

                for each in data:
                   each_list=list(each)
                   final_data = {
                       "groupId":each_list[0],
                       "source_topic":each_list[1],
                       "pipline_status":each_list[2],
                       "pipline_name":each_list[3],
                       "lag":lag,
                       "group_status":group_status,
                       "partition_count":partition_count,
                       "data_type":"kafkaLagMonitor"
                   }
                   #print{json.dumps(final_data, ensure_ascii=False, encoding='utf-8')}
                   f.write(json.dumps(final_data, ensure_ascii=False, encoding='utf-8') + '\n')
                cursor.close()
                db.close()

            except:
                continue

        
    
if __name__=='__main__':
    # 获取登录cookies
    sso_url_itoa = "http://10.239.84.74:8080/authentication/api/login"
    sso_url_refiner = "http://10.239.84.98:8080/authentication/api/login"
    user = "admin"
    passwd = "rMLXJPKS7zGJXbNGYAGRYzevukBSaPD1oYnqrRIlvDlWk7IxJbEZf/Xi4XtSiEYG35VYMHqkPAcaPaw31OLEYEQgwoyUB2XSOXzwQvemghlDP5aXFCswTM5E/yNKgrXYU2yYxrEi0MS54LfZWwp7kgiIdFkmHod75Z3zoSbJjsE="
    cookies_itoa = get_cookies(sso_url_itoa,user,passwd)
    cookies_refiner = get_cookies(sso_url_refiner,user,passwd)
    
    f = open("result.txt", "a")
    cell_db = pymysql.connect(host='10.239.207.19',port=3311,user='znyw',password='Hello123#',database='cell')
    cell_cursor = cell_db.cursor()
    
    pymysql_db = pymysql.connect(host='10.239.207.19',port=3311,user='znyw',password='Hello123#',database='itoa')
    cursor = pymysql_db.cursor()
    url = "http://10.239.84.76:9910/rest/query/_q"
    # curl shell
    sh_curl_shell = "curl -u elastic:Aiops_2022 http://10.239.64.13:29201/_cat/indices?index={}*|sort|tail -1"

    # 需要监控的类型,streaming,batch等
    pipelineType = "streaming"
    # 需要监控的状态,RUNNING,FAILED,STOPPED,START_FAILED等
    pipelineStatus = ["START_FAILED","FAILED","WAITING_START"]
    # 恢复失败作业重试次数
    recoveryRetry = 3
    # jax url
    jaxUrl_itoa = "http://10.239.84.74:8080/jax/api/v1/pipeline/" # 日志
    jaxUrl_refiner = "http://10.239.84.98:8080/jax/api/v1/pipeline/" #  告警
    
    # 采集检查
    monitor_collect()
    # 索引分片配置检查
    monitor_index_config()
    # agent采集状态检查
    agent_monitor()
    # pipeline信息
    get_pipeline_info(jaxUrl_itoa, f, pipelineType, cookies_itoa, pipelineStatus, recoveryRetry)
    get_pipeline_info(jaxUrl_refiner, f, pipelineType , cookies_refiner, pipelineStatus, recoveryRetry)
    #kafka监控,张江及石泉中心
    kafka_group_lag_zj()
    kafka_group_lag_sq()

    cursor.close()
    pymysql_db.close()
    f.close()
