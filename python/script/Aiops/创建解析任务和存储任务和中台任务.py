#!/opt/EntegorAgent/python3/bin/python3
#encoding:utf-8
import math
import os, sys, time
import json
import requests
import logging
import logging.handlers
#!/aiops/python/python-3.8.13/bin/python3.8

def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
    log_path = os.path.dirname(__file__)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + os.sep + 'logs' + os.sep + name + '.log'
    print("日志保存在%s" % log_name)
    ###
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight", interval=1, encoding='utf-8', backupCount=count)
    time_handler.setLevel(log_level)
    time_handler.setFormatter(formatter)
    con_handler = logging.StreamHandler()
    con_handler.setLevel(log_level)
    con_handler.setFormatter(formatter)
    ###
    logger.setLevel(log_level)
    logger.addHandler(con_handler)
    logger.addHandler(time_handler)
    return logger


def do_request(method, url, headers, payload):
    try:
        headers.update({"Cookie": cookie})
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.error(f"reason{res.reason}")
        logger.exception(e)
    return False


def create_storage(conf_dict):
    payload={
        "dataSetName": conf_dict["data_set_name"],
        "dataSetAlias": conf_dict["storage_task_name"],
        "sourceType": "esstore",
        "inDataSetId": conf_dict["anylsis_task_id"],
        "inDataSetIdValue": [
            "数据解析",
            conf_dict["anylsis_task_id"]
            ],
        "remark": "",
        "mappingAppIds": [
            #183109539291136
            ],
        "categoryId": None,
        "categoryList": [],
        "host": "",
        "hostType": "dynamic",
        "hostType": "dynamic",
        "serviceId": "",
        "serviceName": "",
        "topologyId": None,
        "store": [
            {
            "centerId": conf_dict["centerId"],
            "centerName": conf_dict["centerName"],
            "storageId": conf_dict["storageId"],
            "timestamp": "@parsingTime",
            "cycleType": 0,
            "timeInterval": None,
            "dayData": 10,
            "numPartitions": resource_conf["number_of_shards"],
            "isDefaultAddress": True,
            "storageTime": "",
            "jaxCluster": conf_dict["jaxCluster"],
            "groupId": conf_dict.get("store_groupid"),
            "offset": resource_conf["offset_mode"],
            "instanceNum": resource_conf["stor_parall_num"],
            "maxPollSize": 5000,
            "repeatCheck": 0,
            "taskManagerMemory": resource_conf["stor_task_manager_memory"],
            "yarnSlots": resource_conf["yarnslots"],
            "checkPointInterval": 0,
            "esTemplate": "{\n \"order\": \"200\",\n \"index_patterns\": [\n \"" + conf_dict["data_set_name"] + "_*\"\n ],\n \"settings\": {\n \"index\": {\n \"codec\": \"best_compression\",\n \"refresh_interval\": \"10s\",\n \"number_of_shards\": \"" + str(resource_conf["number_of_shards"]) + "\",\n \"number_of_replicas\": \"1\",\n \"translog\": {\n \"sync_interval\": \"60s\",\n \"durability\": \"async\"\n },\n \"merge\": {\n \"scheduler\": {\n \"max_thread_count\": \"1\"\n },\n \"policy\": {\n \"max_merged_segment\": \"100m\"\n }\n },\n \"unassigned\": {\n \"node_left\": {\n \"delayed_timeout\": \"15m\"\n }\n }\n }\n },\n \"mappings\": {\n \"dynamic\": true,\n \"dynamic_templates\": [\n {\n \"message_field\": {\n \"path_match\": \"@message\",\n \"mapping\": {\n \"norms\": false,\n \"type\": \"text\"\n },\n \"match_mapping_type\": \"string\"\n }\n },\n {\n \"string_fields\": {\n \"mapping\": {\n \"type\": \"keyword\"\n },\n \"match_mapping_type\": \"string\",\n \"match\": \"*\"\n }\n }\n ],\n \"properties\": {\n \"@timestamp\": {\n \"type\": \"date\"\n }\n }\n },\n \"aliases\": {}\n}"
            }
        ]
    }
    headers = {
    "Content-Type": "application/json"
    }
    url = f"{host}/logAnalysis/api/itoa/dataset/storageOutPut"
    res = do_request("POST", url, headers, payload)
    if res.get("retCode") == "0000":
        logger.info(f"创建{conf['anly_in_topic']}存储任务成功：{res.get('retMsg')}")
    else:
        logger.error(f"创建{conf['anly_in_topic']}存储任务成功：{res.get('retMsg')}")

def create_analysis(conf_dict):
    payload={
        "inputChannel": "others",
        "inputStorageId": conf_dict.get("inputStorageId"),
        "inputTopic": conf_dict.get("anly_in_topic"),
        "outputChannel": "local",
        "outputStorageId": None,
        "outTopicName": conf_dict.get("anly_out_topic"),
        "dataSetName": conf_dict.get("anlysis_task_name"),
        "sourceType": "analysis",
        "dayData": 10,
        "numPartitions": resource_conf["anly_partitions"], # 分区数
        "remark": "",
        "groupId": "",
        "advanceConfig": [
            {
            "groupId": conf_dict.get("anly_groupid"),
            "numReplications": resource_conf["topic_replication_factor"],
            "maxMessageSize": 1,
            "maxPullMessageSize": 500,
            "instanceNum": resource_conf["anly_parall_num"], # 并发数
            "offset": resource_conf["offset_mode"],
            "commitInterval": 10,
            "taskManagerMemory": resource_conf["anly_task_manager_memory"], # 内存
            "yarnSlots": resource_conf["yarnslots"], # yarnslot数
            "partitionType": "ROUND_ROBIN",
            "partitionType": "ROUND_ROBIN",
            "checkPointInterval": 0,
            "centerId": conf_dict["centerId"],
            "centerName": conf_dict["centerName"],
            "jaxCluster": conf_dict["jaxCluster"],
            "inDataSetIds": []
            }
        ],
        "inDataSetId": [],
        "inDataSetIdValue": [],
        "categoryId": None,
        "categoryList": [],
        "host": "",
        "hostType": "dynamic",
        "serviceId": "",
        "serviceName": "",
        "topologyId": None,
        "centerId": conf_dict["centerId"],
        "filter": {
            "filterGroup": {
                "filtersJson": [
                {
                    "condition": "",
                    "_showCondition": False,
                    "data": [
                    {
                        "field": "@timestamp",
                        "fieldValue": "${timeStamp}",
                        "fieldType": "String"
                    }
                    ],
                    "enable": 1,
                    "ruleName": "Add",
                    "_showRule": True
                },
                {
                    "condition": "",
                    "_showCondition": False,
                    "data": [
                    {
                        "field": "@timestamp",
                        "format": "UNIX_MS",
                        "timezone": "Asia/Shanghai",
                        "locale": ""
                    }
                    ],
                    "enable": 1,
                    "ruleName": "Date",
                    "_showRule": True
                },
                {
                    "condition": "",
                    "_showCondition": False,
                    "data": [
                    {
                        "result": "@rownumber",
                        "target": "",
                        "type": "DATE",
                        "fieldInfo": "",
                        "express": "(${@timestamp})/500",
                        "format": "ms"
                    }
                    ],
                    "enable": 1,
                    "ruleName": "Arithmetic",
                    "_showRule": True
                },
                {
                    "condition": "",
                    "_showCondition": False,
                    "data": [
                    {
                        "result": "@message",
                        "target": "",
                        "type": "STRING",
                        "fieldInfo": "",
                        "express": "${message}"
                    }
                    ],
                    "enable": 1,
                    "ruleName": "Arithmetic",
                    "_showRule": True
                }
                ],
                "sampleDataLists": [
                {
                    "data": {},
                    "_editTitle": False,
                    "isCheck": 1,
                    "title": "样本1"
                }
                ],
                "customizeScript": [],
                "_fieldsList": []
            }
    
        }
    }
    headers = {
        "Content-Type": "application/json"
        }
    url = f"{host}/logAnalysis/api/itoa/dataset/stream"
    res = do_request("POST", url, headers, payload)
    if res.get("retCode") == "0000":
        data_set_id = res.get("entity", {}).get("dataSetId")
        logger.info(f"创建{conf['anly_in_topic']}解析任务成功：{res.get('retMsg')}, task_id:{data_set_id}")
        conf_dict.update({"anylsis_task_id": data_set_id})
    else:
        logger.error(f"创建{conf['anly_in_topic']}解析任务执行失败：{res.get('retMsg')}")

def create_jax(conf_dict):
    payload = {
    "pipelineName": conf_dict["jax_task_name"],
    "pipelineType": "streaming",
    "pipelineConfig": {
    "jobs": [
    {
    "jobId": conf_dict["jax_kafka_in_job_id"], # KafkaByteSourceJob171592622504733080
    "jobName": "com.eoi.jax.flink.job.source.KafkaByteSourceJob",
    "jobConfig": {
    "offsetMode": "group",
    "kafkaConsumerProperties":{"auto.offset.reset":resource_conf["auto.offset.reset"]},
    "topics": [
        conf_dict["jax_input_topic"]
        #"APP_PDMP_TRACELOG_ETL"
    ],
    "commitOffsetOnCheckPoint": True,
    "rebalancePartition": True,
    "groupId": conf_dict["jax_group_id"], #"APP_PDMP_TRACELOG_ETL222",
    "bootstrapServers": conf_dict["bootstrapServers"],
    "byteArrayFieldName": "bytes",
    "autoCreateTopic": False
    },
    "jobOpts": {}
    },
    {
    "jobId": conf_dict["jax_decoder_job_id"],#"YaoLogDecoderJob171592630342152741",
    "jobName": "com.eoi.jax.bosc.flink.job.YaoLogDecoderJob",
    "jobConfig": {},
    "jobOpts": {}
    },
    {
    "jobId": conf_dict["jax_kafka_out_job_id"],#"KafkaSinkJob171592633328590053",
    "jobName": "com.eoi.jax.flink.job.sink.KafkaSinkJob",
    "jobConfig": {
        "autoCreateTopic": True,
        "autoCreateTopicPartitions": resource_conf["jax_partitions"],
        "autoCreateTopicReplicationFactor": resource_conf["topic_replication_factor"],
        "topic": conf_dict["jax_output_topic"], #"APP_PDMP_TRACELOG_ETL_3333",
        "bootstrapServers": conf_dict["bootstrapServers"],
        "semantic": "AT_LEAST_ONCE",
        "logFailuresOnly": True,
        "writeTimestampToKafka": False,
        "kafkaPartitionType": "ROUND_ROBIN"
    },
    "jobOpts": {}
    }
    ],
    "edges": [
    {
    "edgeId": "edge171592633751911604",
    "from": conf_dict["jax_decoder_job_id"], #"YaoLogDecoderJob171592630342152741",
    "fromSlot": 0,
    "to": conf_dict["jax_kafka_out_job_id"], #"KafkaSinkJob171592633328590053",
    "toSlot": 0,
    "mockId": None,
    "enableMock": None
    },
    {
    "edgeId": "edge171592634110732240",
    "from": conf_dict["jax_kafka_in_job_id"], #"KafkaByteSourceJob171592622504733080",
    "fromSlot": 0,
    "to": conf_dict["jax_decoder_job_id"], #"YaoLogDecoderJob171592630342152741",
    "toSlot": 0,
    "mockId": None,
    "enableMock": None
    }
    ],
    "opts": {
        "parallelism": resource_conf["jax_parallelism"], 
        "yarnTaskManagerMemory": resource_conf["jax_yarnTaskManagerMemory"]
        }
    },
    "pipeDescription": None,
    "clusterName": conf_dict["clusterName"],
    "pipelineUi": {
    conf_dict["jax_kafka_in_job_id"]: {
    "display": "Kafka数据源接入_1.9",
    "description": "Kafka Source 返回`Map<String,Object>`1. kafka message的value数据为byte数组类型，通过参数byteArrayFieldName指定输出字段名（默认为bytes）\n2. kafka的元数据输出到参数metaFieldName指定字段名（默认为meta）",
    "x": 336,
    "y": 27,
    "hasDoc": True,
    "docUrl": "/api/v1/job/com.eoi.jax.flink.job.source.KafkaByteSourceJob/document"
    },
    conf_dict["jax_decoder_job_id"]: {
    "display": "解码器(瑶光)",
    "description": "解析瑶光日志，并输出到指定字段，如果不指定输出字段则默认输出到@message字段，\n输出slot 0 为decode成功数据，输出slot 1 为decode失败数据（错误原因添加在error_msg字段） ",
    "x": 334,
    "y": 96,
    "hasDoc": True,
    "docUrl": "/api/v1/job/com.eoi.jax.bosc.flink.job.YaoLogDecoderJob/document"
    },
    conf_dict["jax_kafka_out_job_id"]: {
    "display": "输出到Kafka_1.9",
    "description": "使用FlinkKafkaProducer,无需指定版本号, 由Flink自适应.",
    "x": 329,
    "y": 170,
    "hasDoc": True,
    "docUrl": "/api/v1/job/com.eoi.jax.flink.job.sink.KafkaSinkJob/document"
    }
    }
    }
    headers = {
    "Content-Type": "application/json"
    }
    url = f"{host}/jax/api/v1/pipeline/{conf_dict['jax_task_name']}/stage"
    res = do_request("POST", url, headers, payload)
    if res.get("retCode") == "0000":
        logger.info(f"创建{conf['jax_task_name']}中台任务成功：{res.get('retMsg')}")
    else:
        logger.error(f"创建{conf['jax_task_name']}中台任务执行失败：{res.get('retMsg')}")

def gen_conf(topic, env=None):
    # 原始应用日志：APP_$PASO_APPLOG_SOURCE

    # 分割符处理后应用日志：APP_$PASO_APPLOG_ETL

    # 入ES应用日志：APP_$PASO_DLMT_APPLOG_ETL
    # APP_ECMP_TRACELOG_SOURCE

    # 中台任务输入topic 原始topic名 APP_{p}_TRACELOG_SOURCE_{e}
    # 解析任务输入topic、中台任务输出topic 去掉source APP_{p}_TRACELOG_{e}
    # 解析任务输出topic、存储任务输入topic source换成ETL APP_{p}_TRACELOG_ETL_{e}
    if topic != topic.upper():
        logger.error(f"topic:{topic}不是全大写")
    id_conf = {
        "zj": {
            "bootstrapServers":[
                "10.239.2.76:9092","10.239.2.77:9092","10.239.2.78:9092","10.239.2.79:9092","10.239.2.80:9092"],
            "clusterName": "SQYarn",
            "inputStorageId": 754273169113088, # 张江kafka地址 
            "centerId": 754275092074496, # 张江数据中心 
            "centerName": "张江数据中心",
            "jaxCluster": "ZJYarn",
            "storageId": 754274834120704,# 存储数据中心
        },
        "sq": {
           "bootstrapServers":[
                "10.207.64.27:9092","10.207.64.28:9092","10.207.64.29:9092"],
            "clusterName": "SQYarn",
            "inputStorageId": 756369794883584, # 石泉kafka地址 
            "centerId": 764284838682624, # 石泉数据中心 
            "centerName": "石泉数据中心",
            "jaxCluster": "SQYarn",
            "storageId": 122005221953536,# 存储数据中心
        },
        "dev": {
            "bootstrapServers":[
                "10.240.245.31:9092",
                "10.240.245.32:9092",
                "10.240.245.33:9092"],
            "clusterName": "Yarn",
            "inputStorageId": 182839312752640, # 张江kafka地址
            "centerId": 183106926206976,
            "centerName": "数据中心",
            "jaxCluster": "Yarn",
            "storageId": 182841604730880,
        }
    }
    conf = {}
    conf.update(id_conf[env])
    prefix = str(int(time.time() * 100000000))

    # KafkaByteSourceJob171592622504733080
    conf["jax_kafka_in_job_id"] = f"KafkaByteSourceJob{prefix}"
    # 中台解析算子 #"YaoLogDecoderJob171592630342152741",
    conf["jax_decoder_job_id"] = f"YaoLogDecoderJob{prefix}"
    conf["jax_kafka_out_job_id"] = f"KafkaSinkJob{prefix}" #"KafkaSinkJob171592633328590053",

    # jax_topic名_sq/zj，topic名【除前面的itm/app/等，以及后面的source/etl】。比如nginx这个，就是jax_nginx_errorlog_zj
    # conf["jax_task_name"] = f"jax_{topic.replace('APP_', '').replace('ITM_', '').replace('_SOURCE', '').replace('_ETL', '').replace('.','-')}{'_' + env if not env == 'dev' else ''}"
    # 修改jax任务名，好搜索20240716
    conf["jax_task_name"] = f"jax_{topic.replace('.','-')}{'_' + env if not env == 'dev' else ''}"
    conf["jax_input_topic"] = topic # 原始topic名 APP_{p}_TRACELOG_SOURCE_{e}
    conf["jax_group_id"] = f"{topic}_jax"

    conf["anly_groupid"] = f"{topic}_anly"
    conf["store_groupid"] = f"{topic}_stor"

    if env == "dev":
        conf["jax_output_topic"] = topic.replace("_SOURCE", "")

        conf["anly_in_topic"] = [topic.replace("_SOURCE", "")]
        conf["anly_out_topic"] = topic.replace("SOURCE", "ETL")
        conf["anlysis_task_name"] = f"解析-{topic}"
        conf["storage_task_name"] = f"存储-{topic}"
        conf["data_set_name"] = topic.replace("SOURCE", "ETL").lower()# 数据集名称 子paso是点
    else:
        conf["jax_output_topic"] = topic.replace("SOURCE", "ETL")

        conf["anly_in_topic"] = [topic.replace("SOURCE", "ETL")]
        anly_out_topic = topic.replace("SOURCE", "ETL").split("_")
        anly_out_topic.insert(-2, "DLMT")
        conf["anly_out_topic"] = "_".join(anly_out_topic)

        conf["anlysis_task_name"] = f"解析-{'张江' if env.lower() == 'zj' else '石泉'}-{topic}"
        conf["storage_task_name"] = f"存储-{'张江' if env.lower() == 'zj' else '石泉'}-{topic}"
        conf["data_set_name"] = f"{conf['anly_out_topic'].lower()}_{env.lower()}"
    return conf


if __name__ == "__main__":
    logger = init_logger(os.path.basename(__file__).strip('.py'))
    env = "sq"
    host = {
        "sq": "http://10.251.52.102:18080",
        "zj": "http://10.251.52.102:18080",
        "dev":"http://10.240.246.138:8080"
        }.get(env)
    cookie = "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzIxMTA4NTEwNDIwLCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCIsXCJyZWZpbmVyXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjU2Mzg0NDU4MDcwNDM1ODQsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJjWit4ekdpUVBSZWpISW1OZUlKK1FGV2t3Uk9PcTFEelVZZ0FuWmtycTN4dDhzZkMrOGgzK3hLbEpDMmdPb3VqYlZCdTNna29mVUFzYk1aZGpxdEFMNTRzaG5VdThMdkRGa2VSemhJb3VSZWowOGRvSTRsVE5Ud3FoQnF2c2dIeVFmNFY0VzM5UmMzMHkxeUxKVVVBNlRDbTNkN2JuMEw0MVpxQjhTWEJVNE09IiwicHJvZHVjdHMiOiJ7fSJ9.L3AJDfe6k-wkwrVPPqKe_18Zkp2slpf9B7vvOd5zoXcQ1_NSqyYbsOAxnABxzeeQI7bN7je0rqDZDzWuya3pDw"
    resource_conf = {
        "yarnslots":1,
        "offset_mode": "earliest", # 解析任务存储任务
        "auto.offset.reset": "earliest", # jax任务
        "topic_replication_factor":3, # 副本数量

        "anly_task_manager_memory":512,
        "anly_parall_num":10, # 并行度
        "anly_partitions":20, # kafka分区

        "stor_task_manager_memory":512,
        "stor_parall_num":20, # 并行度
        "number_of_shards":20, # es索引分片

        "jax_parallelism":1,
        "jax_yarnTaskManagerMemory": 1024,
        "jax_partitions": 1, # jax输入topic分区数
    }

    paso = ["CB","CBC", "PDMP.ECMP", "CMO.POF", "IST"]
    env1 = ["PI1", "PI2", "UAT1", "UAT2", "UAT3", "UAT4", "PL1", "PL2", "SIT1", "SIT2", "SIT3", "KFLT1", "KFLT2"]
    env2 = ["PI1", "PI2", "SFYL1", "UAT1", "UAT2", "UAT3", "UAT4", "SIT1", "SIT2"]
    topic_d = {
    "CB": env1,
    "ECMP": env1,
    "CMO.POF": env1,
    "IST": env1,
    "CBC": env2
    }
    # 测试
    # APP_ECMP_TRACELOG_SOURCE APP_MSB.ALP_TRACELOG_SOURCE 
    # APP_OCS.OPS_APPLOG_SOURCE APP_OCS.OPS_TRACELOG_SOURCE
    # APP_ESB_DIRECT_APPLOG_SOURCE
    # for i in ["sq", "zj"]:
    for i in ["sq"]:
        conf=gen_conf("APP_ESB_APPLOG_SOURCE", i)

        create_jax(conf)
        create_analysis(conf)
        create_storage(conf)
    exit()

    # APP_CBC_TRANSLOG_SOURCE_PI1
    # APP_CBC_TRACELOG_SOURCE_PI1
    # APP_CBC_APPLOG_SOURCE_PI1
    # APP_CBC_BATCHLOG_SOURCE_PI1
    for paso in topic_d:
        logger.info(f"创建{paso}的")
        for type in ["APPLOG", "TRACELOG"]:
            for env in topic_d[paso]:
                topic = f"APP_{paso}_{type}_SOURCE_{env}"
                logger.info(topic)
                # conf = gen_conf(topic)
                # logging.info(conf)
                # create_analysis(conf)
                # create_storage(conf)
