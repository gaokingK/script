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
    log_name = log_path + "\\" + name + '.log'
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
            "centerId": 183106926206976,
            "centerName": "数据中心",
            "storageId": 182841604730880,
            "timestamp": "@collectiontime",
            "cycleType": 0,
            "timeInterval": None,
            "dayData": 10,
            "numPartitions": 1,
            "isDefaultAddress": True,
            "storageTime": "",
            "jaxCluster": "Yarn",
            "groupId": None,
            "offset": "earliest",
            "instanceNum": 1,
            "maxPollSize": 5000,
            "repeatCheck": 1,
            "taskManagerMemory": 512,
            "yarnSlots": 1,
            "checkPointInterval": 0,
            "esTemplate": "{\n \"order\": \"200\",\n \"index_patterns\": [\n \"" + conf_dict["data_set_name"] + "_*\"\n ],\n \"settings\": {\n \"index\": {\n \"codec\": \"best_compression\",\n \"refresh_interval\": \"10s\",\n \"number_of_shards\": \"1\",\n \"number_of_replicas\": \"1\",\n \"translog\": {\n \"sync_interval\": \"60s\",\n \"durability\": \"async\"\n },\n \"merge\": {\n \"scheduler\": {\n \"max_thread_count\": \"1\"\n },\n \"policy\": {\n \"max_merged_segment\": \"100m\"\n }\n },\n \"unassigned\": {\n \"node_left\": {\n \"delayed_timeout\": \"15m\"\n }\n }\n }\n },\n \"mappings\": {\n \"dynamic\": true,\n \"dynamic_templates\": [\n {\n \"message_field\": {\n \"path_match\": \"@message\",\n \"mapping\": {\n \"norms\": false,\n \"type\": \"text\"\n },\n \"match_mapping_type\": \"string\"\n }\n },\n {\n \"string_fields\": {\n \"mapping\": {\n \"type\": \"keyword\"\n },\n \"match_mapping_type\": \"string\",\n \"match\": \"*\"\n }\n }\n ],\n \"properties\": {\n \"@timestamp\": {\n \"type\": \"date\"\n }\n }\n },\n \"aliases\": {}\n}"
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
        "inputStorageId": 182839312752640,
        "inputTopic": conf_dict.get("anly_in_topic"),
        "outputChannel": "local",
        "outputStorageId": None,
        "outTopicName": conf_dict.get("anly_out_topic"),
        "dataSetName": conf_dict.get("anlysis_task_name"),
        "sourceType": "analysis",
        "dayData": 10,
        "numPartitions": 3, # 分区数
        "remark": "",
        "groupId": "",
        "advanceConfig": [
            {
            "groupId": "",
            "numReplications": 2,
            "maxMessageSize": 1,
            "maxPullMessageSize": 500,
            "instanceNum": 3, # 并发数
            "offset": "earliest",
            "commitInterval": 10,
            "taskManagerMemory": 1536, # 内存
            "yarnSlots": 1, # yarnslot数
            "partitionType": "ROUND_ROBIN",
            "partitionType": "ROUND_ROBIN",
            "checkPointInterval": 0,
            "centerId": 183106926206976,
            "centerName": "数据中心",
            "jaxCluster": "Yarn",
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
        "centerId": 183106926206976,
        "filter": {
        "filterGroup": {
        "filtersJson": [
            {
                "condition": "",
                "_showCondition": False,
                "data": [
                    {
                    "field": "timeStamp",
                    "format": "yyyy-MM-dd HH:mm:ss",
                    "timezone": "Asia/Shanghai",
                    "locale": ""
                    },
                    {
                    "field": "timeStamp",
                    "format": "UNIX_MS",
                    "timezone": "Asia/Shanghai",
                    "locale": ""
                    }
                ],
                "enable": 1,
                "ruleName": "Date",
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
    "topics": [
    conf_dict["jax_input_topic"]
    #"APP_PDMP_TRACELOG_ETL"
    ],
    "commitOffsetOnCheckPoint": True,
    "rebalancePartition": True,
    "groupId": conf_dict["jax_group_id"], #"APP_PDMP_TRACELOG_ETL222",
    "bootstrapServers": [
    "10.240.245.31:9092",
    "10.240.245.32:9092",
    "10.240.245.33:9092"
    ],
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
    "autoCreateTopicPartitions": 3,
    "autoCreateTopicReplicationFactor": 2,
    "topic": conf_dict["jax_output_topic"], #"APP_PDMP_TRACELOG_ETL_3333",
    "bootstrapServers": [
    "10.240.245.31:9092",
    "10.240.245.32:9092"
    ],
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
    "opts": {}
    },
    "pipeDescription": None,
    "clusterName": None,
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

def gen_conf(topic):
    # 中台任务输入topic 原始topic名 APP_{p}_TRACELOG_SOURCE_{e}
    # 解析任务输入topic、中台任务输出topic 去掉source APP_{p}_TRACELOG_{e}
    # 解析任务输出topic、存储任务输入topic source换成ETL APP_{p}_TRACELOG_ETL_{e}
    if topic != topic.upper():
        logger.error(f"topic:{topic}不是全大写")

    conf = {}
    prefix = str(int(time.time() * 100000000))


    # jax_topic名_sq/zj，topic名【除前面的itm/app/等，以及后面的source/etl】。比如nginx这个，就是jax_nginx_errorlog_zj
    conf["jax_task_name"] = f"jax_{topic.replace('APP_', '').replace('ITM_', '').replace('_SOURCE', '').replace('_ETL', '')}"
    conf["jax_input_topic"] = topic # 原始topic名 APP_{p}_TRACELOG_SOURCE_{e}
    conf["jax_output_topic"] = topic.replace("_SOURCE", "")
    conf["jax_group_id"] = f"{topic}_jax"

    # KafkaByteSourceJob171592622504733080
    conf["jax_kafka_in_job_id"] = f"KafkaByteSourceJob{prefix}"
    # 中台解析算子 #"YaoLogDecoderJob171592630342152741",
    conf["jax_decoder_job_id"] = f"YaoLogDecoderJob{prefix}"
    conf["jax_kafka_out_job_id"] = f"KafkaSinkJob{prefix}" #"KafkaSinkJob171592633328590053",

    conf["anly_in_topic"] = [topic.replace("_SOURCE", "")]
    conf["anly_out_topic"] = topic.replace("SOURCE", "ETL")
    conf["anlysis_task_name"] = f"解析-{topic}"
    conf["storage_task_name"] = f"存储-{topic}"
    conf["data_set_name"] = topic.replace("SOURCE", "ETL").lower()# 数据集名称 子paso是点
    return conf


if __name__ == "__main__":
    logger = init_logger(os.path.basename(__file__).strip('.py'))
    host = "http://10.240.246.138:8080"
    cookie = ""

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
    # conf=gen_conf("APP_test_TRACELOG_SOURCE_test")
    # create_jax(conf)
    # create_analysis(conf)
    # create_storage(conf)
    # exit()

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
