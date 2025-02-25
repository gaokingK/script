import itchat
import os
import re

def find_friends(all_phone):
# 登录微信
    itchat.auto_login()

    # 手机号列表，用于搜索微信好友
    phone_list = all_phone

    # 循环搜索好友
    for phone in phone_list:
        friends = itchat.search_friends(phone=phone)
        for friend in friends:
            # 保存好友头像到文件夹
            img = itchat.get_head_img(userName=friend['UserName'])
            img_path = os.path.join('头像文件夹', f"{friend['NickName']}.jpg")
            with open(img_path, 'wb') as f:
                f.write(img)

    # 退出微信登录
    itchat.logout()

def get_phone_list():
    all_phone = []
    with open(r"C:\Users\CN-jinweijiangOD\Downloads\Telegram Desktop\朱丽君_总数_39945_第1部分.txt", encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
           res = re.search(r"(?<!\d)\d{11}(?!\d)", line)
           if res:
               all_phone.append(res[0])
    return all_phone

if __name__ == "__main__":
    # all_phone = get_phone_list()
    # all_phone = set(all_phone)
    all_phone = ["13189993668"]
    find_friends(all_phone)
               
