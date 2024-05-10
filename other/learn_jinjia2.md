## doc
- 官方文档 ：https://docs.jinkan.org/docs/jinja2/templates.html#filters
## 转义
- link：https://www.w3cschool.cn/yshfid/ysaoqozt.html
## 过滤器
- `{% if "host" in exporters.mysqld and exporters.mysqld.host|length %}`
- {% if tag is defined and tag|length %}

## 操作符
- + 把两个对象加到一起。通常对象是素质，但是如果两者是字符串或列表，你可以用这 种方式来衔接它
## 注释方式
```
{# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}
```
