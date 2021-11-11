#!/usr/bin/python3
"""
# 解析xml文件 python 中用lxml
link: https://www.w3school.com.cn/xpath/xpath_axes.asp
#### 轴怎么用
- `preceding-sibling::` 要加两个冒号
#### 一些语句
- `//*[@text=\"aaa\"]` 获取属性名为text其值为aaa的所有节点集合 A
- `A/node[1]` 获取A的子元素的所有node元素中的第一个
- `A//node[@text!='']` 获取A的后代中的所有node元素且text!=空的
- `A/../preceding-sibling::node[1]/descendant::node[last()]` A 的父节点/所有同级节点
- `A//node[last()]不能获取所有后代的最后一个`
"""
from lxml import html


def get_bound(path, text):
    with open(path, 'r', encoding='utf-8') as f:
        xml_info = f.read()
    element_source = html.etree.fromstring(xml_info.encode("utf-8"))

    text = generate_xpath(text)
    # els = element_source.xpath(text, namespaces={"re": "http://exslt.org/regular-expressions"})
    eles = element_source.xpath(text)
    for ele in eles:
        print("目标的bound是{}".format(ele.get("bounds")))
        print("目标的index是{}".format(ele.get("index")))
        print("目标的text是{}".format(ele.get("text")))


def generate_xpath(resource_id):
    # xpath = u"//*[@text=\"{}\"]".format(text)
    # 获取resouce-id的第二个子节点
    # xpath = u"//*[@resource-id=\"{}\"]/node[2]".format(resource_id)

    xpath = "//*[@text=\"{}\"]/./following::node[1]".format(text)
    # xpath = "//*[@text=\"{}\"]/../preceding-sibling::node[1]/descendant::node[last()]".format(text)

    return xpath


if __name__ == "__main__":
    path = "/home/huawei/Desktop/window_dump.xml"
    # text = "精彩评论"
    text = "comment-reply"
    get_bound(path, text)
    # resource_id = "com.hexin.plat.android:id/ll_content"
    # get_bound(path, resource_id)
