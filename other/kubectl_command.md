
export KUBECONFIG=~/dev-rke-config


kubectl -n foundation get deployments | grep casea

kubectl -n foundation edit deployment <deployment-name>
或者 kubectl -n foundation apply -f deploy-manifest_dev.yaml

### 重启 
- 直接删除
- kubectl -n foundation get pod |grep casea
kubectl -n foundation delete pod pod_name 删除完成后pod会重新拉起来一个