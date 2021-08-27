#!/usr/bin/python3

import subprocess

p = subprocess.Popen("su\n",shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
p.stdin.write(bytes("huawei123\n" ,encoding="utf-8"))
# stdout, stderr = p.communicate("huawei123", 10)
# print(stderr)
stdout, stderr = p.communicate("ls -l", 10)
print(stderr.decode("utf-8"), stdout.decode("utf-8"))
