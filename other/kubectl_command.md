
export KUBECONFIG=~/.kube/devops-cmdbserv-v0.yaml


kubectl -n foundation get deployments | grep casea

kubectl -n foundation edit deployment <deployment-name>
或者 kubectl -n foundation apply -f deploy-manifest_dev.yaml

### 重启 
- 直接删除
- kubectl -n foundation get pod |grep casea
kubectl -n foundation delete pod pod_name 删除完成后pod会重新拉起来一个


### 进入单容器的pod里执行命令


```cs
$ kubectl.exe  -n foundation get pod|grep cmdb
devops-cmdbserv-v0-6bcf9db8f7-qgxvg                   2/2     Running            0          35m
devops-cmdbweb-v0-8949d84c9-75hhj                     2/2     Running            0          2d18h

d1806@DESKTOP-6L3FPSB MINGW64 ~
$ kubectl.exe  -n foundation get pods|grep cmdb
devops-cmdbserv-v0-6bcf9db8f7-qgxvg                   2/2     Running            0          35m
devops-cmdbweb-v0-8949d84c9-75hhj                     2/2     Running            0          2d18h

d1806@DESKTOP-6L3FPSB MINGW64 ~
$ kubectl.exe -n foundation exec -it devops-cmdbserv-v0-6bcf9db8f7-qgxvg -- "/bin/bash"
```
- Git Bash 自动将 Unix 风格的路径 /bin/bash 转换成了 Windows 风格的路径 D:/softwares/Git/usr/bin/bash 使用winpty 或者MSYS_NO_PATHCONV=1 
```cs
# 在 Git Bash 中设置环境变量 MSYS_NO_PATHCONV=1 可以禁止路径转换：
MSYS_NO_PATHCONV=1 kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash
# 临时禁用所有转换：
export MSYS_NO_PATHCONV=1
kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash
```

### 问题
- error: error loading config file "C:/Users/d1806/.kube/devops-cmdbserv-v0.yaml": no kind "Deployment" is registered for version "apps/v1" in scheme "k8s.io/client-go/tools/clientcmd/api/latest/latest.go:50"
export KUBECONFIG=~/.kube/devops-cmdbserv-v0.yaml 导入的文件格式不正确

-  winpty kubectl exec -it devops-cmdbserv-v0-78f6954fd6-r4sdh -n foundation -- /bin/bash 集群的配置信息没导入成功
E0331 15:27:34.443846   26324 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"
http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target
machine actively refused it."
  