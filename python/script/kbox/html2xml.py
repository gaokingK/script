import os.path
import re
import sys
from html.parser import HTMLParser
from typing import List

"""
link:https://www.cnblogs.com/liuhaidon/p/12060184.html
"""
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []  # 定义data数组用来存储html中的数据
        self.links = []

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data===>', data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


def parse_by_re(path="/home/huawei/Desktop/html2xml/index.html"):
    with open(path, "r+") as f:
        content = f.read()
        # res = re.findall(r"href[\S ]*>([a-zA-Z]+\.[a-zA-Z.]+)(?#package).*?"
        #                  r"(\d+)(?#tests).*?(\d+)(?#failures).*?"
        #                  r"(\d+)(?#ignored).*?([\d.]+)(?#duration).*?([\d%]+)(?#success rate)", content, re.S)
        res = re.findall(r"tests.*?counter\">(\d+)(?#tests)"
                         r".*?failures.*?counter\">(\d+)(?#failures)"
                         r".*?ignored.*?counter\">(\d+)(?#ignored)"
                         r".*?duration.*?counter\">([\d.]+)(?#duration)"
                         r".*?successRate.*?percent\">([\d%]+)(?#success rate)", content, re.S)
        return res


def gen_xml_file(content: List, path=None):
    with open(path, "w+") as f:
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        for item in content:
            # name = item[0]
            # time = item[4]
            # tests = item[1]
            # errors = int((100 - int(item[5].split('%')[0])) / 100 * int(tests))
            # failures = item[2]
            # skipped = item[3] # ignored
            time = item[3]
            tests = item[0]
            errors = int((100 - int(item[4].split('%')[0])) / 100 * int(tests))
            failures = item[1]
            skipped = item[2]
            f.write(f'<testsuites name="kassiantphonetest" time="{time}" tests="{tests}" errors="{errors}" skipped="{skipped}" failures="{failures}"/>\n')

        # f.write("</node>")


if __name__ == "__main__":
    # html_code = '''<html>
    #         <head>这是头标签</head>
    #         <body>
    #             <!-- test html parser -->
    #             <p>Some <a href=\"#\">html</a> HTML&nbsp;&#1234; Ӓtutorial...<br>END</p>
    #         </body></html>'''
    # parser = MyHTMLParser()
    # parser.feed(html_code)
    # parser.close()
    # print(parser.data)
    # print(parser.links)
    html_file = sys.argv[1]
    xml_file = os.path.join(os.path.dirname(os.path.abspath(html_file)), "mvent.xml")
    print(xml_file)
    data = parse_by_re(path=html_file)
    gen_xml_file(data, path=xml_file)
