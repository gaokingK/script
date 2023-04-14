### re.sub(r"(?<=\()(\S+)(?=\))", r"\1 IB", event_description) 
- 还可已这样替换
```
a="disk backplane 2 temperature detection point"
re.sub(r"(?<=backplane )\d(?= temper)", "-", a, 1)
或者直接 re.sub(r"(?<=backplane )\d(?= temper)", "backplane - temper", a, 1)
```
### (?<=(mAsserted\(.*\n.*\n.*)) wait_time=20\)