import requests
import os, json
import logging
import logging.handlers
from datetime import datetime
#!/aiops/python/python-3.8.13/bin/python3.8

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
logger = init_logger(os.path.basename(__file__).strip('.py'))

def delete_es_index(index):
    url = "http://10.251.52.102:18080/cerebro/overview/delete_indices"

    payload = {
        "indices": "sys_oracle_alertunix_eoi_2024_04_25",
        "host": "http://10.207.64.26:29202",
        "username": "elastic",
        "password": "Aiops_2022"
    }
    headers = {
        "Cookie": "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzE3Mzk5MzI0ODIwLCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCIsXCJyZWZpbmVyXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjU1MTY5MDMyMTMzMDI3ODQsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJjWit4ekdpUVBSZWpISW1OZUlKK1FGV2t3Uk9PcTFEelVZZ0FuWmtycTN4dDhzZkMrOGgzK3hLbEpDMmdPb3VqYlZCdTNna29mVUFzYk1aZGpxdEFMNTRzaG5VdThMdkRGa2VSemhJb3VSZWowOGRvSTRsVE5Ud3FoQnF2c2dIeVFmNFY0VzM5UmMzMHkxeUxKVVVBNlRDbTNkN2JuMEw0MVpxQjhTWEJVNE09IiwicHJvZHVjdHMiOiJ7fSJ9.LsQ1M3z5Z73pOt75JO-65zhYPsYXhqTLKY5HeDKcWnuti73pm7iaqD_7xPqIXdxOYuyiMmfqCd-0Isu9b4xqSQ",
        "content-type": "application/json"
    }
    try:
        res = requests.request("POST", url, json=payload, headers=headers).json()
        if res.get("status") == 200:
            logger.error(f"删除索引{index}成功")
            return True
        logger.error(f"删除索引{index}失败")
        return False
    except Exception as e:
        logger.exception(e)
        logger.error(f"删除索引{index}失败")

def calc_es_index():
    for index in mon_index_list:
        for item in all_data:
            if index in item.get("name"):
                size_res[index] = size_res.get(index, 0) + item.get("size_in_bytes")

def filter(index):
    if not index:
        return False
    
    if "_eoi_2023_" not in index:
        return False
    
    if "net_nmm_almlog_source" in index:
        return False
    
    if "itm_linux_securelog_source" in index:
        return False

    if "itm_linux_dmesglog_source" in index:
        return False

    if "itm_linux_messageslog_source" in index:
        return False

    if "itm_san_syslog_source" in index:
        return False

    if "itm_net_syslog" in index:
        return False

    return True

def calc_es_index():
    for index in mon_index_list:
        for item in all_data:
            if index in item.get("name"):
                size_res[index] = size_res.get(index, 0) + item.get("size_in_bytes")

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "es_index.json"), "r", encoding='utf-8') as f:
        all_data = json.load(f)

    mon_index_list = ["iops_itoa_jaxlog", 'app_promethues.transfer_log', 'iops_refiner_alert_source_count', 'itm_nginx_errorlog_source', 'itm_nginx_accesslog_source', 'itm_redis_redislog_source', 'itm_redis_sentinellog_source', 'iops_itoa_uqplus_log', 'itm_aiops_applog_source', 'itm_kafka_serverlog_source', 'itm_kafka_statechangelog_source', 'itm_kafka_controllerlog_source', 'itm_tomcat_catalinalog_source', 'itm_tomcat_accesslog_source', 'itm_zk_serverlog_source', 'itm_bes_iastoolslog_source', 'itm_bes_serverlog_source', 'app_txbk_applog_source', 'app_csi_applog_source', 'app_eib_applog_source', 'app_pib_applog_source', 'app_pmb_applog_source', 'app_pmb.golf_applog_source', 'itm_windows_syseventlog_source', 'itm_windows_seceventlog_source', 'itm_windows_appeventlog_source', 'app_rlcs_applog_source', 'app_msb_applog_source', 'app_cbib_applog_source', 'app_esb_applog_source', 'itm_rabbitmq_log_source', 'app_wmbp_applog_source', 'app_ips_applog_source', 'itm_httpd_accesslog_source', 'itm_httpd_errorlog_source', 'app_otp.snd_applog_source', 'app_embs_applog_source', 'app_bce_applog_source', 'app_bbp_applog_source', 'app_cbbm_applog_source', 'app_sms_applog_source', 'app_pdmp.fps_applog_source', 'app_prms.irms_applog_source', 'app_picp_applog_source', 'app_tfpv_applog_source', 'app_uim_applog_source', 'app_crm_applog_source', 'app_bsft_applog_source', 'app_cpt_applog_source', 'app_edb.dbes_applog_source', 'app_blim_applog_source', 'app_rcmp.pls_applog_source', 'app_pdmp.efm_applog_source', 'app_rcmp.lmc_applog_source', 'app_rcmp.rsc_applog_source', 'app_nucp.upop_applog_source', 'app_nucp.aop_applog_source', 'app_nucp_applog_source', 'app_atmp_applog_source', 'itm_cbs_celllog_source', 'app_cdbp_applog_source', 'app_epay_applog_source', 'itm_cbs_log_source', 'itm_cfs_log_source', 'itm_csp_log_source', 'itm_dcgw_log_source', 'itm_es_log_source', 'itm_hdfs_log_source', 'itm_imagestage_log_source', 'itm_metedata_log_source', 'itm_natgw_log_source', 'itm_ocloud_log_source', 'itm_overlay_log_source', 'itm_snap_log_source', 'itm_sxgw_log_source', 'itm_tcloud_log_source', 'itm_vpc_log_source', 'itm_vpcdns_log_source', 'itm_vpcgw_log_source', 'itm_xgw_log_source', 'itm_tdsql_log_source', 'itm_tgw_log_source', 'itm_tke_log_source', 'itm_underlay_log_source', 'itm_zk_log_source', 'itm_upsql_log_source', 'itm_redis_log_source', 'app_resb_applog_source', 'app_dsr_translog_source', 'itm_erm_stagingdlog_source', 'net_syslog_h3c_switch', 's.app.jp1.joblog', 'net-pro', 's.aiops.refiner.recovery.event', 's.itm.iops.id.almlog.source.tmp', 's.net.alert.filter.log', 's.net.alarm.filter.out', 's.aiops.refiner.event.output', 's.itsm.log', "s.app.cnv.applog"]
    size_res = {}
    calc_es_index()
    for key,value in size_res.items():
        size = value/1024/1024/1024
        logger.info(f"{key}的张江和石泉索引大小是{.2fsize}G") 

    # for item in all_data:
    #     name = item.get("name", "")
    #     if filter(name):
    #         delete_es_index(name)
