# -*- coding: utf-8 -*-
import pymysql
import os
import logging
import logging.handlers


def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
    log_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + os.sep + 'logs' + os.sep + name + '.log'
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

logger = init_logger(os.path.basename(__file__).split(".py")[0])
# 打开数据库连接
db = pymysql.connect(host='10.126.156.158',
                     user='cmdb_rw',
                     password='cmdb@dev',
                     database='cmdb',
                     charset='utf8mb4',
                     port=3307,
                     cursorclass=pymysql.cursors.DictCursor )
def transfer_resource_uids(names, table_a, table_b, name_column='name', uid_column='resource_uid'):
    """从表A查询resource_uid并插入到表B"""
    cursor = db.cursor()
    
    try:
        # 构建IN查询的占位符
        placeholders = ','.join(['%s'] * len(names))
        
        # 查询表A中匹配名字的resource_uid
        select_sql = f"SELECT {uid_column} FROM {table_a} WHERE {name_column} IN ({placeholders})"
        cursor.execute(select_sql, names)
        
        results = cursor.fetchall()
        
        # 提取resource_uid列表
        resource_uids = [row[uid_column] for row in results]
        print(f"找到 {len(resource_uids)} 个resource_uid: {resource_uids}")
        
        # 插入到表B
        insert_sql = f"INSERT INTO {table_b} ({uid_column}) VALUES (%s)"
        cursor.executemany(insert_sql, [(uid,) for uid in resource_uids])
        
        db.commit()
        print(f"成功插入 {cursor.rowcount} 条记录到表B")
        
    except Exception as e:
        db.rollback()
        print(f"操作失败: {e}")
    finally:
        cursor.close()

def update_one_project_tags(db_cursor, project_name, table_a, table_b, name_column='project_name', uid_column='resource_uid', is_prod=True, filter_column=None, filter_v=None):
    try:
        tag_id = 27 if is_prod else 28
        select_sql = f"SELECT {uid_column} FROM {table_a} WHERE {name_column} = %s and d_version='latest' and is_deleted=0"
        if filter_column and filter_v:
            select_sql += f" and {filter_column} = '{filter_v}'"
        db_cursor.execute(select_sql, (project_name,))
            
        results = db_cursor.fetchall()
        if not results:
            logger.error(f"未找到项目{project_name}")
            return project_name
        if len(results) > 1:
            logger.error(f"项目{project_name}找到多条记录")
            return project_name
    
        resource_uid = results[0][uid_column]
        insert_sql = f"INSERT INTO {table_b} (tag_id, resource_type, {uid_column}) VALUES (%s, 'project', %s)"
        db_cursor.execute(insert_sql, (tag_id, resource_uid))
        db.commit()
        
        logger.info(f"成功为项目{project_name}插入标签记录")
        
    except Exception as e:
        logger.error(f"更新项目{project_name}标签失败: {e}")
        raise


# 使用示例
if __name__ == "__main__":
    dev_project_names = ["FND-TEST-Ninja", "Wukong-HK", "TOS-TEST-ICMS", "WuKong-TEST-CDNOSS", "apisix_chaos_tke宿主机",  "apisix_chaos_ack宿主机", "FND-TEST-混沌环境", "TOS-TEST-Retentionmall", "TOS-TEST-Global_Boss", "TOC-TEST-Campaign", "WuKong-TEST-PT", "TOS-TEST-RgmbossDt", "TOE-TEST-Chatbot", "TOC-TEST-OMNI", "TOC-TEST-Menu2", "INFRA-TEST-Devops", "TOE-TEST-MSO", "TOC-TEST-Cos_Order", "TOS-TEST-Dify", "TOS-TEST-AI", "INFRA-TEST-MaxKB", "TOS-TEST-Training公网代理", "INFRA-TEST-TCR", "INFRA-TEST-JiraProxy", "WuKong-TEST-Victoria", "PT_ACK_BFF", "PT_ACK_ISTIO", "TOC-TEST-MASM", "TOC-TEST-Delta", "WuKong-TEST-HKAccessSite", "FND-TEST-TRAINING", "DCOE-TEST-大数据", "TOC-TEST-OMMDIY", "TOE-TEST-Hackathon", "devops_test_fake_tke宿主机", "devops_test_fake_rke宿主机", "sit_tke宿主机", "uat_tke宿主机", "dev_tke宿主机", "uat_ack宿主机", "sit_ack宿主机", "dev_ack宿主机", "TOB-TEST-Hackathon", "dev_rke宿主机", "TOC-DEV-中银通VPN", "INFRA-TEST-InfraLLM", "TOC-TEST-冷热分离", "TOS-TEST-Burgerx", "TOC-TEST-CNN", "TOC-TEST-会员画像", "WuKong-TEST-devops", "TOC-TEST-DPP2", "WuKong-TEST-DRcluster", "FND-TEST-混沌工程", "INFRA-TEST-AES_Client", "INFRA-TEST-360_AES", "FND-TEST-混沌环境", "TOC-TEST-菜单改版", "TOC-TEST-OpenApi", "INFRA-TEST-PAGP", "TOE-TEST-SCPL", "tc-test-testServer-01", "TOE-TEST-NEPS", "TOE-TEST-PlaceCenter", "People_Center", "TOC-TEST-Tidb", "TOE-TEST-PYT代理SAP", "TOB-TEST-RDRM", "TOC-TEST-APISIX", "TOS-TEST-RGM_BOSS", "TOC-PROD-COE_Redis", "INFRA-TEST-Network", "INFRA-TEST-AI攻防", "TOE-TEST-Chatbot", "TOE-TEST-Hackathon", "TOE-TEST-EXT_BOSS", "INFRA-TEST-SRE", "TOC-TEST-Payment", "TOC-TEST-PaaSStore", "TOC-TEST-PCM", "TOE-TEST-知识中心", "TOC-TEST-Coupon", "INFRA-TEST-大中台", "TOE-TEST-BizGateway", "TOE-TEST-Etraining", "TOS-TEST-麦麦e起说", "TOC-TEST-LEGO", "TOS-TEST-AdminPortal", "TOB-TEST-GitlabApp", "TOE-TEST-AITrain", "TOE-TEST-Legal电子签", "TOE-TEST-eMall", "TOE-TEST-CPM", "TOS-TEST-Nova", "TOE-TEST-E_Tax_Platform", "TOE-TEST-外网代理", "TOS-TEST-Dfs", "TOS-TEST-压测发压机", "TOB-TEST_PYT代理SAP", "TOC-PROD-BCP_TIDB", "TOB-TEST-STINV", "TOS-TEST-Recruitment", "TOE-TEST-移动端Mechina", "TOE-TEST-Ninja", "TOS-TEST-ERetention", "TOE-TEST-HR_Service_Portal", "TOS-TEST-BBEP", "TOS-TEST-MAP", "TOC-TEST-NEWAPP_FY", "TOC-TEST-BCP_TIDB", "INFRA-TEST-默安巡哨", "WuKong-TEST-COS", "TOC-TEST-MDMS", "TOE-TEST-跨行资金池", "TOC-TEST-K8S_ELK", "TOC-TEST-ELK", "INFRA-TEST-Network", "TOC-TEST-DouyinEC", "INFRA-TEST-NetworkMonitor", "TOE-TEST-AIGC", "INFRA-TEST-Network", "DOCE-TEST-大数据", "INFRA-TEST-SDWAN", "WuKong-TEST-ECS", "TOC-TEST-CNY压测", "INFRA-TEST-DorisVictoria测试", "TEST_CNY压测", "TOC-TEST-SmartLocker", "TOE-TEST-IOT", "ali_uat_ack宿主机", "ali_pt_ack宿主机", "ali_dev_ack宿主机", "TEST_Hackathon", "TEST_Coupon", "TEST_NOVA", "TEST_默安巡哨系统", "TEST_ACK_BFF_PERF", "TEST_EXT_BOSS", "TEST_BCP_mongo", "TEST_e-retention", "TEST_猫窝压测", "TEST_BCP方案验证", "tidb_test", "TEST_BCP_TIDB", "TEST_Wukong", "TEST_ACK_BFF_FUNC", "apisix_test_tke宿主机", "TEST_GitlabApp", "TEST_PYT代理SAP", "TEST_People_Center", "TEST_AI攻防", "APISIX_生产", "TEST_Hi400", "TEST_Wukong", "cloudpos", "TEST_AI训练", "TEST_cloudpos", "智能用户增长", "TEST_知识中心", "TEST_全电发票", "阿里云第三方市场", "阿里云短信", "pt_ack宿主机", "TEST_餐厅非Windows设备远程管理平台", "日志审计", "ToC_CLB", "apisix_test_ack宿主机", "apisix_test_tke宿主机", "Payment_IDC迁移项目", "HR Service Portal", "APISIX_TEST", "uat-ack宿主机631比例均摊", "uat-ack宿主机(631比例均摊)", "sit-ack宿主机(631比例均摊)", "FCT_财务中台", "备案域名留档", "TEST_BBeProduction", "Legal_2B电子签", "支付网关", "HedanJumpServer腾讯云转发", "绿盟态势感知", "餐道传输", "OPEN_API", "RGM_BOSS_TEST", "COE_redis", "COE_mysql", "BFF_PT_TKE", "SIEM_proxy", "网络ping测试", "企业微信", "Legal_2B电子签_TEST", "泛微工作平台", "eMall_TEST", "dev2_tke宿主机", "Pandora_test", "CPS_PRO_TEST", "cnsok_TEST", "stage_tke宿主机", "PT_TKE_ISTIO", "NEWAPP_FY_test", "Tob测试环境外网代理", "TEST_TKE_BFF", "sit_tke宿主机_631比例均摊", "foundation_tke宿主机", "E_Tax_Platform_TEST", "API_7_POC_TEST", "社群企微顾客标签", "SAAB", "rts_nova", "PT_TKE_COE", "Chatbot_test", "压测发压机", "uat_tke宿主机_631比例均摊", "uat_rke宿主机", "test_tke宿主机", "PT_TKE_BFF", "infra_esalert", "Headoffice工位_会议系统_腾讯云", "dev_tke宿主机_631比例均摊", "Crew人员幸福指数调研问卷", "devops_tke宿主机", "SRE_TEST", "RMS_TEST", "支付网关开发测试", "store_test", "供应链中台_TEST", "TEST_hrms_recruitment", "PCM_test", "TEST_ninja_pandora", "HR中台", "Etraining_TEST", "企微反向代理", "DFS_数字化食品安全_TEST", "LEGO_test", "HR_ESS_TEST", "HR_Service_Portal_TEST", "AdminPortal_test", "CRM_腾讯云", "eTraining_麦麦e起说_test", "devops", "大中台Infra测试", "sit_ack宿主机_631比例均摊", "监控机器_生产", "hedan阿里云堡垒机代理_生产", "CMDB转发机器_生产", "ADB转发机器_生产", "网络监控_测试", "uat_ack宿主机_631比例均摊", "网络ping测试", "测试k8s_ELK", "开发测试ELK", "AB测试"]
    
    all_dev_faild = ['FND-TEST-混沌环境', 'TOC-TEST-Tidb', 'TEST_AI训练', '绿盟态势感知', 'TOS-TEST-MAP', 'INFRA-TEST-SRE', 'TEST_BBeProduction', 'TOS-TEST-BBEP', '网络ping测试', 'INFRA-TEST-Network', 'TOE-TEST-Hackathon', 'TOE-TEST-IOT', 'TOC-TEST-CNN', 'TOE-TEST-E_Tax_Platform', 'TOE-TEST-Chatbot', '日志审计', 'uat_rke宿主机', 'apisix_test_tke宿主机', 'dev_rke宿主机', 'HedanJumpServer腾讯云转发', 'devops', 'TEST_Wukong']
    # 腾讯云大中台  
    dev_faild1 = ['FND-TEST-混沌环境', 'TOC-TEST-Tidb', "TEST_AI训练", "绿盟态势感知", "TOS-TEST-MAP", "INFRA-TEST-SRE", "TEST_BBeProduction", 
    "TOS-TEST-BBEP", "网络ping测试", "INFRA-TEST-Network", "TOE-TEST-Hackathon", "TOE-TEST-IOT", "TOC-TEST-CNN", "TOE-TEST-E_Tax_Platform", "TOE-TEST-Chatbot", "日志审计", "uat_rke宿主机", "apisix_test_tke宿主机", "dev_rke宿主机", "HedanJumpServer腾讯云转发", "devops", "TEST_Wukong"]
    # 腾讯云大数据 
    dev_faild2 = ["网络ping测试", "INFRA-TEST-Network", "TOE-TEST-Hackathon", "apisix_test_tke宿主机"]
    # 阿里云小程序 
    dev_faild3 = ["FND-TEST-混沌环境", "INFRA-TEST-Network", "TOE-TEST-Chatbot", "TEST_Wukong"]
    dev_project_names = list(set(dev_project_names))

    
    prod_project = ["INFRA-PROD-BAS", "TOE-PROD-PMT_OuterNet", "K3", "NetworkWatcherRG", "HAVICenter", "HAVI-K3", "HAVI-ER", "CTC-Azure项目暂存", "TOE-PROD-SRM堡垒机", "INFRA-PROD-eCapex", "AOAI", "hu-ai", "TOE-PROD-AOAIPOC", "TOE-PROD-麦当劳招聘公众号", "user-audit", "TOE-PROD-HeadOffice", "TOE-PROD-eCapex", "Portal", "INFRA-PROD-WSUS", "TOE-PROD-MDM", "PMT", "INFRA-PROD-赛门铁克", "ICP", "FND-PROD-Gomax", "TOE-PROD-进销存系统", "TOE-PROD-EPS", "TOE-PROD-CEM", "TOC-PROD-官网", "STINV-PT", "SC-CENTER", "INFRA-PROD-Network", "TOS-PROD-排班系统", "TOE-PROD-新考勤系统", "TOE-PROD-招聘移动开发", "TOE-PROD-SAP", "TOE-PROD-IOT", "TOE-PROD-HR_eContract", "TOE-PROD-EMSB", "TOE-PROD-eLegalReport", "TOE-PROD-eCion", "TOE-PROD-CLMS", "TOE-PROD-CCMS", "INFRA-PROD-Monitor", "TOS-PROD-Nabit", "TOC-PROD-MappingTool", "INFRA-PROD-ER专线", "DCOE-PROD-BCG", "TOE-PROD-WIP", "TOE-PROD-HFM", "MCD_Test", "TOS-PROD-LSM", "TOE-PROD-O365", "TOE-PROD-IDP", "INFRA-PROD-Zabbix", "TOC-PROD-微信公众号中控服务", "TOE-PROD-慈善基金会", "TOC-PROD-麦麦同学会", "Mcd-Azure项目暂存", "INFRA-PROD-Fortigate", "", "", "SOL", "SRM", "AWS-CTC-Default", "TOE-PROD-ROP", "TOE-PROD-SAPFLUME", "TOE-PROD-JDA", "AWS-EDH-Default", "", "", "INFRA-PROD-ASOC", "TOS-PROD-ICMS", "INFRA-PROD-Zabbix", "INFRA-PROD-Zabbix", "WuKong-PROD-GitLabRunner", "TOE-PROD-Esourcing", "DCOE-PROD-CDP", "TOC-PROD-CCC", "TOS-PROD-RgmbossDt", "TOC-PROD-CCC", "INFRA-PROD-TSec", "INFRA-PROD-DMP", "TOS-PROD-eTraining", "TOC-PROD-Campaign", "TOS-PROD-Retentionmall", "TOS-PROD-Delta", "WuKong-PROD-AurumGlobal", "TOC-PROD-OMNI", "TOC-PROD-SWC", "TOC-PROD-Menu2", "TOC-PROD-Cos_Order", "TOE-PROD-MSO", "TOE-PROD-SCCC_MirrorRepository", "INFRA-PROD-MDM_EMM", "TOE-PROD-Proxy", "INFRA-PROD-AI_Gateway", "TOS-PROD-AI", "TOE-PROD-Image", "DCOE-PROD-DAAS", "WuKong-PROD-OBOCP", "z_prod_rke宿主机", "TOE-PROD-AIGC", "TOS-PROD-Nabit", "cn_wukong_ack_dr01宿主机", "PROD_ACK_PORTAL", "PROD_ACK_大数据", "z_prod_ack宿主机", "INFRA-PROD-BAS", "INFRA-PROD-BAS", "PROD_ACK_BFF", "PROD_ACK_ISTIO", "TOC-PROD-MASM", "TOC-PROD-Delta", "DCOE-PROD-DTS", "TOC-PROD-年末战报", "z_prod_tke宿主机", "INFRA-PROD-MerakiApi", "DCOE-PROD-埋点同步", "TOS-PROD-DTv2", "TOC-PROD-中银通VPN", "DCOE-PROD-TKE_TID", "DCOE-PROD-Nob_Plus", "DCOE-PROD-中银通VPN", "DCOE-PROD-BigDataCrawler", "DCOE-PROD-第三方接口", "DCOE-PROD-Nob_Plus", "DCOE-PROD-IMP", "DCOE-PROD-DMP", "DCOE-PROD-NoBRealtime", "DCOE-PROD-基础服务", "ali_trainning_ack宿主机", "DCOE-PROD-AI中台", "ali-prod-ack宿主机", "TOC-PROD-官网", "ali_prod_ack宿主机", "TOC-PROD-OpenApi", "WuKong-PROD-MDM_Pad准入", "TOC-PROD-BCP_OMC", "阿里云号码百科", "TOB-PROD-Nob_Plus", "FND-PROD-API治理", "TOC-PROD-会员画像", "TOE-PROD-CCMSG", "TOS-PROD-Burgerx", "TOC-PROD-CNN", "TOB-PROD-中银通VPN", "INFRA-PROD-KYBP", "INFRA-PROD-SmartOA", "INFRA-PROD-DCCloud", "WuKong-PROD-MDM_EMM", "TOC-PROD-Tidb_Oms", "TOC-PROD-Tidb_Mbr", "TOC-PROD-Tidb_Payment", "TOC-PROD-Tidb_Coupon", "INFRA-PROD-RavenMonitor", "INFRA-PROD-RavenMonitor", "INFRA-PROD-RavenMonitor", "INFRA-PROD-RavenMonitor", "DCOE-PROD-冷数据备份", "WuKong-PROD-COS", "WuKong-PROD-DRcluster", "TOE-PROD-STINV_COS", "TOC-PROD-AI", "TOS-PROD-CCCTool", "Wukong-PROD-Download", "WuKong-PROD-Rancher", "TOE-PROD-SCPL", "TOE-PROD-NEPS", "TOE-PROD-PlaceCenter", "TOC-PROD-E_BOOK", "TOS-PROD-RDRM", "TOE-PROD-企业微信", "TOC-PROD-Tidb_Pnt", "TOC-PROD-Tidb", "TOE-PROD-PYT代理SAP", "FND-PROD-GoMax", "TOE-PROD-OCR", "TOE-PROD-FCT_财务中台", "TOC-PROD-Magpie", "TOB-PROD-TKE_TID", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-BillingItemDetail", "TOC-PROD-Invoice", "INFRA-PROD-LogAudit", "TOE-PROD-EXT_BOSS", "TOS-PROD-RGM_BOSS", "TOC-PROD-COE_Mysql", "TOC-PROD-Open_Platform", "TOC-PROD-SAAB", "TOC-PROD-中台OPS", "INFRA-PROD-域名留档", "TOC-PROD-Payment", "TOC-PROD-CLB", "INFRA-PROD-SIEM_Proxy", "TOB_PROD_RDRM", "INFRA-PROD-PingMesh", "INFRA-PROD-SecurityToken", "TOE-PROD-BizGateway", "INFRA-PROD-MVP", "INFRA-PROD-TC堡垒机_FW", "TOE-PROD-Chatbot", "INFRA-PROD-EsAlert", "INFRA-PROD-Thanos", "TOE-PROD-知识中心", "TOB-PROD_GoMax", "INFRA-PROD-Devops", "TOC-PROD-Coupon", "TOC-PROD-PaaSStore", "TOS-PROD-麦麦e起说", "TOC-PROD-LEGO", "TOC-PROD-TKE_PORTAL", "TOS-PROD-BBEP", "TOE-PROD-WorkflowEcology", "TOE-PROD-DMS", "TOE-PROD-OKR", "TOS-PROD-Dfs", "TOE-PROD-E_Tax_Platform", "FND-PROD-Pandora", "TOB-PROD_PYT代理SAP", "TOE-PROD-Legal电子签", "TOE-PROD-Hi400", "TOE-PROD-CPM", "TOS-PROD-Nova", "TOE-PROD-eMall", "TOC-PROD-社群顾客_Tag", "TOE-PROD-FCT_Recon_Center", "TOE-PROD-员工满意度", "TOE-PROD-Head会议系统", "TOS-PROD-CNSOK", "TOC-PROD-MDMS", "TOB-PROD-STINV", "TOS-PROD-Recruitment", "TOS-PROD-DPM", "TOE-PROD-移动端Mechina", "TOE-PROD-Ninja", "TOE-PROD-HR_Service_Portal", "TOE-PROD-eTraining", "TOS-PROD-ERetention", "TOC-PROD-餐道传输", "TOC-PROD-OpenApi", "TOS-PROD-MAP", "TOC-PROD-ShortUrl", "TOC-PROD-IMP", "FND-PROD-GITLAB", "TOC-PROD-BCP", "TOC-PROD-WOAPP", "TOC-PROD-非码Nginx", "TOS-PROD-智能取餐柜", "TOS-PROD-CrystalShield", "TOC-PROD-ICC_CT_服务包", "TOB-PROD-第三方接口", "TOB-PROD-NoBRealtime", "TOE-PROD-TES", "TOS-PROD-RGM_Community", "TOS-PROD-能耗管家", "TOB-PROD-基础服务", "INFRA-PROD-LogAudit", "INFRA-PORD-SecurityLog", "DCOE-PROD-Pricing_Tiger", "INFRA-PROD-DataProxyOld", "TOB-PROD-BigDataCrawler", "INFRA-PROD-Devops", "TOB-PROD-DAAS", "INFRA-PROD-DataProxyNew", "INFRA-PROD-TC堡垒机_FW", "INFRA-PROD-欧阳堡垒机", "INFRA-PROD-MonitorApi", "INFRA-PROD-PingMesh", "TOE-PROD-Wecom", "INFRA-PROD-基础服务", "DCOE-PROD-RgmNob", "TOB-PROD-ROMS", "INFRA-PROD-Kong", "DCOE-PROD-神策埋点", "INFRA-PROD-齐志堡垒机", "TOE-PROD-EPS", "INFRA-PROD-LogAudit", "INFRA-PORD-SecurityLog", "TOC-PROD-Eachhub", "INFRA-PROD-TC堡垒机_FW", "INFRA-PROD-Hedan_FW", "TOC-PROD-TmallEC", "TOC-PROD-DouyinMP", "TOC-PROD-DouyinEC", "TOB-PROD-PMTPLUS", "INFRA-PROD-LogAudit", "INFRA-PROD-AckLog", "INFRA-PORD-SecurityLog", "INFRA-PROD-LogAudit", "INFRA-PROD-TC堡垒机_FW", "TOC-PORD-现在支付", "INFRA-PROD-Rancher", "INFRA-PROD-Security", "INFRA-PROD-备案LB", "INFRA-PROD-CMDB_FW", "DCOE-PROD-ADB_FW", "INFRA-PROD-Ali堡垒机_FW", "INFRA-PROD-NetworkMonitor", "INFRA-PROD-PingMesh", "TOB-PROD-Nob_Plus", "TOC-PROD-SmartLocker", "TOE-PROD-IOT", "TOC-PROD-AlipayCoupon", "TOB-PROD-DMP", "PROD_Coupon", "PROD_EXT_BOSS", "PROD_e-retention", "PROD_BCP_TIDB", "tidb_pro", "PROD_GoMax", "PROD_PYT代理SAP", "PROD_People_Center", "PROD_企微安全令牌", "PROD_BCP_mongo", "apisix_prod_tke宿主机", "apisix_prod_ack宿主机", "PROD_Hi400", "PROD_知识中心", "TOB-PROD-腾讯会议", "腾讯云WebService API", "腾讯云DNS", "INFRA-PROD-HW_SDWAN", "PROD_pingmesh", "PROD_pingmesh", "PROD_餐厅非Windows设备远程管理平台", "日志审计", "安全日志对接", "PROD_TKE_COE", "PROD_BBeProduction", "RGM_BOSS_PROD", "open_platform_prod", "E_Tax_Platform_PROD", "PROD_TKE_PORTAL", "PROD_RKE宿主机", "CPS_PRO_PROD", "mvp_prod", "FCT_Recon_Center_PROD", "eMall_PROD", "Chatbot_prod", "stage_rke宿主机", "PROD_TKE_大数据", "PROD_TKE_ISTIO", "PROD_TKE_BFF", "PROD_Infra_thanos", "RMS_PROD", "store_prod", "PROD_hrms_recruitment", "供应链中台_PROD", "OKR_PROD", "Legal_2B电子签_PROD", "Etraining_PROD", "DFS_数字化食品安全_PROD", "DPM_PROD", "LEGO_prod", "HR_ESS_PROD", "HR_Service_Portal_PROD", "PROD_ninja_pandora", "cnsok_PROD", "eTraining_麦麦e起说_prod", "PROD_ACK宿主机", "HedanJumpServer", "IoT_Utility", "Infra基础服务", "ROMSPRO", "Crystal_Shield"]


    all_prod_failed_project = ['INFRA-PROD-BAS', 'INFRA-PROD-WSUS', 'FND-PROD-Gomax', 'TOE-PROD-EPS', 'TOC-PROD-官网', 'TOE-PROD-SAP', 'TOE-PROD-IOT', 'INFRA-PROD-Monitor', 'TOS-PROD-Nabit', 'INFRA-PROD-Zabbix', 'INFRA-PROD-Zabbix', 'INFRA-PROD-Zabbix', 'DCOE-PROD-CDP', 'TOC-PROD-CCC', 'TOC-PROD-CCC', 'TOC-PROD-SWC', 'z_prod_rke宿主机', 'TOS-PROD-Nabit', 'INFRA-PROD-BAS', 'INFRA-PROD-BAS', 'DCOE-PROD-埋点同步', 'DCOE-PROD-Nob_Plus', 'DCOE-PROD-Nob_Plus', 'DCOE-PROD-IMP', 'DCOE-PROD-DMP', 'DCOE-PROD-AI中台', 'TOC-PROD-官网', 'TOC-PROD-OpenApi', 'TOB-PROD-Nob_Plus', 'TOC-PROD-会员画像', 'TOC-PROD-CNN', 'INFRA-PROD-KYBP', 'INFRA-PROD-SmartOA', 'INFRA-PROD-DCCloud', 'TOC-PROD-Tidb_Oms', 'TOC-PROD-Tidb_Mbr', 'TOC-PROD-Tidb_Payment', 'TOC-PROD-Tidb_Coupon', 'INFRA-PROD-RavenMonitor', 'INFRA-PROD-RavenMonitor', 'INFRA-PROD-RavenMonitor', 'INFRA-PROD-RavenMonitor', 'TOC-PROD-Tidb_Pnt', 'TOC-PROD-Tidb', 'TOE-PROD-PYT代理SAP', 'TOE-PROD-OCR', 'INFRA-PROD-BillingItemDetail', 'INFRA-PROD-BillingItemDetail', 'INFRA-PROD-BillingItemDetail', 'INFRA-PROD-BillingItemDetail', 'INFRA-PROD-BillingItemDetail', 'INFRA-PROD-LogAudit', 'INFRA-PROD-PingMesh', 'TOE-PROD-BizGateway', 'INFRA-PROD-TC堡垒机_FW', 'INFRA-PROD-Devops', 'TOS-PROD-BBEP', 'TOE-PROD-WorkflowEcology', 'TOE-PROD-DMS', 'TOE-PROD-OKR', 'TOE-PROD-E_Tax_Platform', 'TOE-PROD-Legal电子签', 'TOE-PROD-Hi400', 'TOE-PROD-Head会议系统', 'TOE-PROD-eTraining', 'TOC-PROD-OpenApi', 'TOS-PROD-能耗管家', 'INFRA-PROD-LogAudit', 'INFRA-PORD-SecurityLog', 'INFRA-PROD-Devops', 'INFRA-PROD-TC堡垒机_FW', 'INFRA-PROD-PingMesh', 'TOE-PROD-Wecom', 'TOE-PROD-EPS', 'INFRA-PROD-LogAudit', 'INFRA-PORD-SecurityLog', 'INFRA-PROD-TC堡垒机_FW', 'INFRA-PROD-LogAudit', 'INFRA-PORD-SecurityLog', 'INFRA-PROD-LogAudit', 'INFRA-PROD-TC堡垒机_FW', 'INFRA-PROD-Security', 'INFRA-PROD-PingMesh', 'TOB-PROD-Nob_Plus', 'TOE-PROD-IOT', 'PROD_pingmesh', 'PROD_pingmesh', '日志审计', '安全日志对接', 'PROD_RKE宿主机', 'stage_rke宿主机']

    # 腾讯云大中台
    prod_failed0 = ["FND-PROD-GoMax"]
    prod_failed1 = ["INFRA-PROD-BAS", "FND-PROD-GoMax", "TOE-PROD-IOT", "INFRA-PROD-Zabbix", "TOC-PROD-CCC", "TOC-PROD-SWC", "z_prod_rke宿主机", "DCOE-PROD-Nob_Plus", "TOC-PROD-会员画像", "TOC-PROD-CNN", "INFRA-PROD-KYBP", "INFRA-PROD-SmartOA", "INFRA-PROD-DCCloud", "TOC-PROD-Tidb_Oms", "TOC-PROD-Tidb_Mbr", "TOC-PROD-Tidb_Payment", "TOC-PROD-Tidb_Coupon", "INFRA-PROD-RavenMonitor", "TOC-PROD-Tidb_Pnt", "TOC-PROD-Tidb", "TOE-PROD-PYT代理SAP", "TOE-PROD-OCR", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-LogAudit", "INFRA-PROD-PingMesh", "TOE-PROD-BizGateway", "INFRA-PROD-TC堡垒机_FW", "INFRA-PROD-Devops", "TOS-PROD-BBEP", "TOE-PROD-WorkflowEcology", "TOE-PROD-DMS", "TOE-PROD-OKR", "TOE-PROD-E_Tax_Platform", "TOE-PROD-Legal电子签", "TOE-PROD-Hi400", "TOE-PROD-Head会议系统", "TOE-PROD-eTraining", "TOB-PROD-Nob_Plus", "TOE-PROD-IOT", "PROD_pingmesh", "PROD_RKE宿主机", "stage_rke宿主机"]

    # Mcd-Azure
    prod_failed2 = ["TOE-PROD-SAP", "TOE-PROD-IOT", "INFRA-PROD-Monitor", "TOS-PROD-Nabit", "INFRA-PROD-Zabbix", "INFRA-PROD-BAS", "TOS-PROD-Nabit", "TOC-PROD-官网", "TOE-PROD-EPS", "TOE-PROD-IOT"]
    # 腾讯云大数据  
    # 没有 INFRA-PROD-Monitor
    prod_failed3 = ["TOE-PROD-EPS", "TOC-PROD-官网", "INFRA-PROD-Monitor", "TOS-PROD-Nabit", "DCOE-PROD-CDP", "TOS-PROD-Nabit", "DCOE-PROD-埋点同步", "DCOE-PROD-Nob_Plus", "DCOE-PROD-IMP", "DCOE-PROD-DMP", "TOC-PROD-官网", "TOB-PROD-Nob_Plus", "INFRA-PROD-RavenMonitor", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-LogAudit", "INFRA-PROD-PingMesh", "INFRA-PROD-TC堡垒机_FW", "INFRA-PROD-Devops", "TOS-PROD-能耗管家", "INFRA-PORD-SecurityLog", "TOE-PROD-Wecom", "TOE-PROD-EPS", "INFRA-PORD-SecurityLog", "TOB-PROD-Nob_Plus", "PROD_pingmesh"]

    # 腾讯云小程序
    # 没有 INFRA-PROD-Monitor
    prod_failed4 = ["INFRA-PROD-RavenMonitor", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-LogAudit", "INFRA-PROD-TC堡垒机_FW"]

    # 腾讯云现在支付
    prod_failed5 = ["INFRA-PROD-RavenMonitor", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-LogAudit", "INFRA-PROD-TC堡垒机_FW", "INFRA-PORD-SecurityLog", "INFRA-PORD-SecurityLog", "日志审计", "安全日志对接"]
    # 阿里云小程序
    prod_failed6 = ["INFRA-PROD-BAS", "INFRA-PROD-Zabbix", "TOC-PROD-CCC", "INFRA-PROD-BAS", "DCOE-PROD-AI中台", "TOC-PROD-OpenApi", "INFRA-PROD-BillingItemDetail", "INFRA-PROD-LogAudit", "INFRA-PROD-PingMesh", "INFRA-PROD-Security"]


    project_names = list(set([""]))
    db_cursor = db.cursor()
    fail_project = []
    for name in project_names:
        res = update_one_project_tags(db_cursor, name, "project", "resource_tag", is_prod=True)
        # res = update_one_project_tags(db_cursor, name, "project", "resource_tag", is_prod=True, filter_column='cloud_account', filter_v='阿里云小程序')
        if res:
            fail_project.append(res)
    logger.info(f"失败项目: {fail_project}, 共有{len(fail_project)}个")

    db.close()
