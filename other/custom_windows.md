### 加入开机启动
Win+R打开“运行”
输入“shell:startup” 如果正在为当前用户配置启动行为
如果正在使用设备为所有用户配置启动行为，shell:common startup

按 Windows 徽标键 + R，键入“shell:startup”，然后选择“确定”。这将打开“启动”文件夹。

将该应用的快捷方式从文件位置复制并粘贴到“启动”文件夹中。

### powershell中设置环境变量
```cs
$env:KUBECONFIG="/.kube/devops-cmdbserv-v0.yaml" #注意引号

echo $env:MY_ENV_VAR 
# 设置用户级环境变量
[System.Environment]::SetEnvironmentVariable("MY_ENV_VAR", "my_value", "User")
# 设置系统级环境变量
[System.Environment]::SetEnvironmentVariable("KUBECONFIG", "C:\Users\d1806\.kube\devops-cmdbserv-v0.yaml", "Machine")
```

### git bash 路径转换
```cs
- Git Bash 自动将 Unix 风格的路径 /bin/bash 转换成了 Windows 风格的路径 D:/softwares/Git/usr/bin/bash 使用winpty 或者MSYS_NO_PATHCONV=1 
```cs
# 在 Git Bash 中设置环境变量 MSYS_NO_PATHCONV=1 可以禁止路径转换：
MSYS_NO_PATHCONV=1 kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash
# 临时禁用所有转换：
export MSYS_NO_PATHCONV=1
kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash

# winpty 是一个 Windows 特定的工具，帮助解决 Git Bash 和 Windows 环境之间的兼容性问题。
winpty kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash
```

### 一些git bash中的小工具
由于git bash使用unix风格的路径名称，所以尝尝造成一些程序错误。cygpath可以完成git bash 中的路径与windows系统的路径之间的转换。
```
$cygpath --dos /c/WINDOWS/system32
C:\WINDOWS\system32
```
### 添加到环境变量
除了直接添加到系统环境变量的方式，还有集中方式可以将bash添加到系统的环境变量之中

使用scoop的可以通过scoopshim 命令，如 scoop shim add gitbash $env:scoop\apps\git\current\bin\bash.exe
通过在在powershell profile 中添加alias或者function，如New-Alias gbash $env:scoop\apps\git\current\bin\bash.exe
