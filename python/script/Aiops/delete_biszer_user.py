import os,json
import logging
import logging.handlers     
import requests


def init_logger(name, count=10):
    logger = logging.getLogger(__file__)
    log_level = logging.DEBUG
    formatter = logging.Formatter("%(message)s")
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

filename = f"{os.path.basename(__file__).strip('.py')}"
logger = init_logger(name=filename)

def do_request(method, url, header=None, payload=None):
    headers = {"Authorization":Authorization}
    if header:
        headers.update(header)
    try:
        if payload:
            res = requests.request(method, url=url, headers=headers, json=payload)
        else:
            res = requests.request(method, url=url, headers=headers)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False


def delete_user(username):
    url=f"http://10.251.4.18:8083/api/system/user/username/{username}"
    method = "DELETE"
    res = do_request(method, url)
    if res.get("code") == 200:
        logger.info(f"删除用户{username}成功")
    else:
        logger.error(f"删除用户{username}失败，msg:{res.get('msg')}")

def add_user(user_info):
    url=f"http://10.251.4.18:8083/api/system/user/register"
    method = "POST"
    payload = {
        "username": user_info.get("username").lower(),
        "full_name": user_info.get("username_zh"),
        "phone_number": "",
        "email": "",
        "description": "",
        "password": "Aipt!@34",
        "services": {
            "include_all": False,
            "include": [],
            "instances": []
        },
        "roles": [
            "60652550107d7c9c2021d4ea" if user_info.get("role") == 1 else "5f16a535107d7c3d15b86ff9"
        ],
        "status": "enable"
    }

    res = do_request(method, url, payload=payload)
    if res.get("code") == 200:
        logger.info(f"新建用户{user_info.get('username')}成功")
    else:
        logger.error(f"新建用户{user_info.get('username')}失败，msg:{res.get('msg')}")

if __name__ == "__main__":
    Authorization = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJmdWxsX25hbWUiOiJzdXBlcmFkbWluIiwiZXhwIjoxNzIxMTI0ODMyLCJ1c2VybmFtZSI6ImFpb3BzIiwicm9sZXMiOltdfQ.M5tvJcsF5PhE8TkkvbEGU-MHgoMoEbA5HTioRM3MkO9iEdfZY-KKK6We07f3GKaf_9EpmTZYqu90_DoK5huCvg"
    # delete_user_l = {'tongx', 'chendy', 'cuilq', 'zhuw', 'yuanm', 'yaoyf', 'wuqy', 'tangyy', 'wangjr', 'lull', 'jiangkx', 'mayx', 'zhangxu', 'netquery', 'xtquery', 'daiwt', 'guql', 'zhangyy', 'fangdq', 'shaozhoury', 'lily', 'pengwl', 'panjun', 'wuhx', 'baochj', 'yyai', 'liwh', 'hujie', 'liuy', 'sgbquery', 'lichf', 'fandh', 'chenxj', 'xiali', 'huangjm', 'xtadmin', 'jingych', 'zhaoshuai'}
    # for user in delete_user_l:
    #     delete_user(user)
    # exit()
    
    # role0_name = ['CS8488', 'CS6557', 'CS6551', 'CS6545', 'CS5457', 'CS7049', 'CS6958', 'CS8436', 'CS8098']
    # role0_name_zh = ['胡瑜', '汪义', '张云松', '凌志', '张文甫', '王媛媛', '王银成', '鲍硕', '张如中']
    # for name,name_zh in zip(role0_name, role0_name_zh):
    #     user_info = {"username": name, "username_zh":name_zh, "role":0}
    #     add_user(user_info)
    # exit()
    # role1_name = ['301178', '301190', '301211', '302286', '303061', '301845', '303074', '303939', '304106', '304349', '304766', '305364', '302935', '304076', '305411', '305434', '306454', '306456', '306451', '306457', 'W00059', 'W00063', 'W00124', '304088', '306448', '306418', '305062', '300765', '310258', '319833', '300320', '300333', '300342', '319907', '301855', '303077', '303457', '303488', '303490', '303777', '303938', '304109', '304040', '305333', '306186', '306452', '306453']
    # role1_name_zh = ['邵周若宇', '王颉蓉', '郑子熠', '潘骏', '赵帅', '童俊超', '朱雯', '包晨杰', '高世宇', '彭望龙', '江康熙', '韩健伟', '徐淼', '李超峰', '樊丁皓', '景奕辰', '方丹青', '沈小愉', '李蓉受', '周屹彬', '韩怀柱', '梁鸿波', '姚一飞', '许致立', '王硕邦', '宁寰', '潘明杰', '王明杰', '王成', '邱旻骏', '孙明昊', '周敏超', '贾天婧', '倪捷', '黄亮', '张旭', '肖坤', '王立', '朱俊杰', '欧阳晖', '龙汉良', '冯亦磊', '沈健', '孙帅', '王恩泽', '万琪', '王晨懿']
#     role1_name = ['300673', '313146', '319573', '315367', '319699', '300329', '301252', '302549', '319910', '303489', '304066', '304103', '305389', '306458', '306803', '305354', '306455', '303929', '303497', '303953']
#     role1_name_zh = ['金斯', '白翔', '卫廉', '王靓', '余飞', '高丰韡', '王明辉', '李涛', '徐昱昊', '卞荣坤', '戎奕豪', '肖雁冰', '张天天', '张蓉', '陈凡', '史金易', 
# '杨中金', '胡红青', '金杨', '崔立群']
    role1_name = ['305891', '303469', '302368', '303081', '303055', '304084', '302851']
    role1_name_zh = ['陈晓剑', '宁静艳', '郑建丽', '蔡根根', '邱迪佩', '夏煜彬', '李佳媛']
    for name,name_zh in zip(role1_name, role1_name_zh):
        user_info = {"username": name, "username_zh":name_zh, "role":1}
        add_user(user_info)
