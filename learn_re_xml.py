#!/usr/bin/python3
from lxml import html


def get_bound(path, text):
    with open(path, 'r', encoding='utf-8') as f:
        xml_info=f.read()
    element_source = html.etree.fromstring(xml_info.encode("utf-8"))

    text = generate_xpath(text)
    #els = element_source.xpath(text, namespaces={"re": "http://exslt.org/regular-expressions"})
    eles = element_source.xpath(text)
    for ele in eles:
        print("目标的bound是{}".format(ele.get("bounds")))
        print("目标的index是{}".format(ele.get("index")))

def generate_xpath(resource_id):
    #xpath = u"//*[@text=\"{}\"]".format(text)
    # 获取resouce-id的第二个子节点
    #xpath = u"//*[@resource-id=\"{}\"]/node[2]".format(resource_id)

    #xpath = "//*[@text=\"{}\"]/../following-sibling::node[1]".format(text)
    xpath = "//*[@text=\"{}\"]/../preceding-sibling::node[1]/descendant::node[last()]".format(text)

    return xpath


if __name__ == "__main__":
    path = "/home/huawei/Desktop/window_dump.xml"
    text ="精彩评论"
    get_bound(path, text)
    #resource_id = "com.hexin.plat.android:id/ll_content"
    #get_bound(path, resource_id)

