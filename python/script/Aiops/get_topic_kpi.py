import requests
import json
import os
import logging
import logging.handlers
from openpyxl import Workbook
from openpyxl.styles import Font  
from datetime import datetime
import re


def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
    log_path = os.path.dirname(__file__)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + "/" + name + "_" + datetime.now().strftime("%Y%m%d") + '.log'
    print("日志保存在%s" % log_name)
    ###
    ch_handler = logging.StreamHandler()
    ch_handler.setLevel(log_level)
    ch_handler.setFormatter(formatter)
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight", interval=1,
                                                             encoding='utf-8', backupCount=count)
    time_handler.setLevel(log_level)
    time_handler.setFormatter(formatter)
    ###
    logger.setLevel(log_level)
    logger.addHandler(time_handler)
    logger.addHandler(ch_handler)
    return logger

def do_request(method, url, queryparm):
    querystring = {
        "startTime":"1716876646575",
        "endTime":"1716963046575",
        "updateRecent":"false",
        "queries":"",
        "chartType":"line",
        "desiredRollup":"",
        "returnFilteredOutStreams":"false",
        "returnImpliedStreams":"false"}
    querystring.update(queryparm)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "SESSION=MjFmOTA0ZmUtYjdmNi00Njg4LWE5MzAtN2YzMDYwNTJlNjk1",
        "content-type": "application/json"
    }
    res = requests.request(method, url, headers=headers, params=querystring)
    if res:
        return res.json()
    
# select total_kafka_bytes_received_rate_across_kafka_broker_topics 
# total_kafka_bytes_fetched_rate_across_kafka_broker_topics
# total_kafka_bytes_rejected_rate_across_kafka_broker_topics 
# total_kafka_messages_received_rate_across_kafka_broker_topics 
# total_kafka_rejected_message_batches_rate_across_kafka_broker_topics 
# total_kafka_fetch_request_failures_rate_across_kafka_broker_topics 
# total_kafka_bytes_fetched_rate_across_kafka_brokers 
def get_topic_max_byte(topic):
    querystring = {
        "queries":f'[{{\"tsquery\":\"SELECT total_kafka_bytes_received_rate_across_kafka_broker_topics WHERE entityName = \\\"kafka:{topic}\\\" AND category = KAFKA_TOPIC\",\"histogramCutPoints\":null,\"densityPlotNumSlices\":null,\"sliceIndexToContinueFrom\":null,\"pipelineType\":null}}]',
        "desiredRollup":"TEN_MINUTELY"}
    res = do_request("POST", url, querystring)
    max_bytes = 0
    if res:
        res = res[0]['timeSeries'][0]['data']
        for item in res:
            max_bytes=max(max_bytes, item['rollupStatistics']["max"])
    return int(max_bytes * 60)

def get_topic_mean_byte(topic):
    querystring = {
        "queries":f'[{{\"tsquery\":\"SELECT total_kafka_bytes_received_rate_across_kafka_broker_topics WHERE entityName = \\\"kafka:{topic}\\\" AND category = KAFKA_TOPIC\",\"histogramCutPoints\":null,\"densityPlotNumSlices\":null,\"sliceIndexToContinueFrom\":null,\"pipelineType\":null}}]',
        "desiredRollup":"DAILY"}
    res = do_request("POST", url, querystring)
    mean = 0
    if res:
        res = res[0]['timeSeries'][0]['data']
        if res:
            res = res[0]['rollupStatistics']
            mean = res["mean"]
    return int(mean * 60)
    
def get_topic_max_message(topic):
    querystring = {
        "queries":f'[{{\"tsquery\":\"SELECT total_kafka_messages_received_rate_across_kafka_broker_topics WHERE entityName = \\\"kafka:{topic}\\\" AND category = KAFKA_TOPIC\",\"histogramCutPoints\":null,\"densityPlotNumSlices\":null,\"sliceIndexToContinueFrom\":null,\"pipelineType\":null}}]',
        "desiredRollup":"TEN_MINUTELY"}
    res = do_request("POST", url, querystring)
    max_message = 0

    if res:
        res = res[0]['timeSeries'][0]['data']
        for item in res:
            max_message=max(max_message, item['rollupStatistics']["max"])
    return int(max_message * 60)
            
def get_topic_mean_message(topic):
    querystring = {
        "queries":f'[{{\"tsquery\":\"SELECT total_kafka_messages_received_rate_across_kafka_broker_topics WHERE entityName = \\\"kafka:{topic}\\\" AND category = KAFKA_TOPIC\",\"histogramCutPoints\":null,\"densityPlotNumSlices\":null,\"sliceIndexToContinueFrom\":null,\"pipelineType\":null}}]',
        "desiredRollup":"DAILY"}
    res = do_request("POST", url, querystring)
    mean = 0
    if res:
        res = res[0]['timeSeries'][0]['data']
        if res:
            res = res[0]['rollupStatistics']
            mean = res["mean"]
    return int(mean * 60)



if __name__ == "__main__":
    logger = init_logger(os.path.basename(__file__).strip('.py'))
    url = "http://10.251.4.18:8081/cmf/charts/timeSeries"
    topic_l = ["APP_BSMP.AC_TRACELOG_SOURCE", "APP_BSMP.VC_TRACELOG_SOURCE", "APP_BSMP_TRACELOG", "APP_CBC_TRACELOG", "APP_CBMS_TRACELOG_SOURCE", "APP_CRC_TRACELOG", "APP_CRC_TRACELOG_SOURCE", "APP_ECMP_TRACELOG_SOURCE", "APP_EIB.NEW_TRACELOG", "APP_EMBS.SEBS_TRACELOG_SOURCE", "APP_EMBS_TRACELOG", "APP_IFS.AFM_TRACELOG_SOURCE", "APP_IFS.BS_TRACELOG_SOURCE", "APP_IFS.FB_TRACELOG_SOURCE", "APP_IFS.QP_TRACELOG", "APP_IFS.SMCS_TRACELOG_SOURCE", "APP_IFS.UCAP_TRACELOG_SOURCE", "APP_IFS_TRACELOG", "APP_IPS.ECNY-SC_TRACELOG_SOURCE", "APP_IPS.ECNY_TRACELOG", "APP_OCS.OPS_TRACELOG_SOURCE", "APP_PDMP.EBSS_TRACELOG", "APP_PDMP.EFM_TRACELOG_SOURCE", "APP_PDMP.OC_TRACELOG_SOURCE", "APP_PDMP.OSI_TRACELOG_SOURCE", "APP_PDMP_TRACELOG", "APP_PDMP_TRACELOG_SOURCE", "APP_PMB_TRACELOG", "APP_PMB_TRACELOG_SOURCE", "APP_PRMS.IRMS_TRACELOG_SOURCE", "APP_PRMS_TRACELOG", "APP_PRMS_TRACELOG_SOURCE", "APP_RCMP.LMC_TRACELOG_SOURCE", "APP_RCMP.PLS_TRACELOG_SOURCE", "APP_RCMP.RSC_TRACELOG", "APP_RCMP.RSC_TRACELOG_SOURCE", "APP_RCMP_TRACELOG", "APP_RESB_TRACELOG_SOURCE", "APP_TXBK_TRACELOG", "APP_TXBK_TRACELOG_SOURCE", "APP_WMPC_TRACELOG_SOURCE"]
    res = []
    wb = Workbook()
    work_sheet = wb.active
    work_sheet.append(["topic", "每分钟最大bytes", "今天平均bytes每分钟", "每分钟最大消息数", "今天平均分钟消息数"])
    for i in range(1,6):
        work_sheet.cell(row=1,column=i).font = Font(name="Arial", size=14, color="FF000000", bold=True) 
    for topic in topic_l:
        data = {"name": topic}
        data["max_b"] = get_topic_max_byte(topic)
        data["mean_b"] = get_topic_mean_byte(topic)
        data["max_m"] = get_topic_max_message(topic)
        data["mean_m"] = get_topic_mean_message(topic)
        res.append(data)
        work_sheet.append([x for x in data.values()])
    res_file = os.path.join(os.path.dirname(__file__), "topic_Kpi.xlsx")
    wb.save(res_file)
    
    # TEN_MINUTELY
