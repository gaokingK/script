### Resources
- [代码仓](http://isource.huawei.com/TaiShan-Solution/Kunpeng_Automation_test/tree/master)
- [执行机](10.186.108.156)
- [命令](http://3ms.huawei.com/hi/group/2795335/wiki_5789686.html?for_statistic_from=all_group_wiki)

### 新任务
- [ ] OVS自动化开发是干什么，OVS是什么意思？
- [ ] openstack是什么？
    OpenStack 是当今最具影响力的云计算管理工具通过命令或者基于 Web 的可视化控制面板来管理 IaaS 云端的资源池(服务器、存储和网络)。
- [ ] GTR 是什么东西？
- [ ] CIDA 是什么东西？
    是一个自动化测试平台
- [ ] 自动化用例是什么
- [ ] Avocado？
    - 是一个自动化测试框架
- [ ] BMC
- [ ] UVP
- [ ] 为什么掉这么多层， 封包？
- [ ] 步骤里面没说的东西，为什么要做，是不是有些通用的前置操作

### 看文档
1. [GTR_Python脚本开发从零开始](http://3ms.huawei.com/hi/group/2795335/wiki_5704596.html?for_statistic_from=all_group_wiki)
    - [ ] 安装gtr_python 环境
    - [ ] 测试套是什么？
2. [自动化测试代码Merge操作规范](http://3ms.huawei.com/hi/group/2795335/wiki_5900526.html?for_statistic_from=all_group_wiki)
    - [x] 触发门禁，build 页签是什么
3. [自动化用例/工厂常见问题及原因分析](http://3ms.huawei.com/hi/group/2795335/wiki_5750852.html?for_statistic_from=all_group_wiki)
    - [ ] 只看了一点
4. [切换2+1模式TICC指南 ](http://3ms.huawei.com/hi/group/2795335/wiki_5918440.html?for_statistic_from=all_group_wiki)
    - [ ] 什么是2+1 模式？ TICC 又是什么意思？
    - [ ] 只看了一点
5. [自动化代码规范与cleancode要求](http://3ms.huawei.com/hi/group/2795335/wiki_5826122.html?for_statistic_from=all_group_wiki)
    - [ ] 只看了一点

### 有没有业务介绍的资料，或者原理类
- 地址 ：\\10.174.60.200\测试框架
- cnt_V2R5是所有用例的合集，uts_dev_master是原始的原子
    - [ ] cnt_V2R5 是什么意思？ uts_dev_master又是什么意思？

1. 大家找原始用例的时候用git工具的find命令，比如找这个用例 find . -name etp_user_hwc_vpn_001
### 看cnt_V2R5
- [x] .rst文件格式

### 看IFE软卸载测试报告

### 看GTR PYTHON 简介
- 版本为1.7.7
- [ ] GIT python 单机版怎么配合IDE进行开发，调试。。。
- [ ] 测试用例、测试套、在哪里？
- [ ] 工厂版服务是什么？
- [ ] gtr config 选项不能使用？

### unittest
### 复用代码
- 对端创建虚拟机 组网 ping evs2.0_ife_fun_018
- 加载acl模块 acl ovs-appctl dpif-dpdk/component load acl
- 置捕获窗口时长为5分钟  ovs-vsctl set Open_vSwitch . other_config:flowlog_interval=5
- 打开iptables ovs-appctl iptables/on
- .使能tap1端口flowlog功能（ALL，ACCEPT，REJECT） ovs-vsctl set interface %s options:flow_log=on" % self.port[0]
### 看evs2.0_ife_fun_018 修改前与修改后
- [ ] 流程的变化是怎么推知的？
- [ ] 两端都配CT 
- [ ] 把相应的原子操作给挑出来 
### 迁移
- `self.atom(fun=self.driver.network_kvm.clear_plc_dpdk_env, result=exit_code.PASS_ACK)`
- `self.net.clear_net()`

- `self.atom(_func=self.driver.network_common.restart_service, _args='openvswitch', _result=exit_code.PASS_ACK)`

### 相关
- OpenFlow是一种新型的网络协议，它是控制器和交换机之间的标准协议。

### 命令
- mz使用eth0 发送广播流`mz eth0 -A 10.0.0.1 -B 10.0.0.2 ff:ff:ff:ff:ff:ff`
- 使用特定的设备发起 ping `ping -i dev_name`
- 网段不同，会自动选择同网段的网卡进行通信的，不在一个网段，肯定不通。eth0能通，是因为，br-int跟虚拟机的ip，在同一个网段
- 删除测试网卡 `ip link del eth1.100`
- vm内部创建相同vlan的vlan子接口（1-4094随机)
    ```shell
    ip link add link eth0 name eth0.100 type vlan id 100
    ip addr add 192.168.100.10/24 brd 192.168.100.255 dev eth0.100
    ip link set dev eth0.100 up
    ```
- 网卡热插: virsh attach-device VM1 --file iface.xml
    ```xml
    <interface type='vhostuser'>
      <mac address='02:ca:fe:fa:2e:23'/>
      <source type='unix' path='/var/run/openvswitch/tap2' mode='client'>
        <reconnect enabled='yes' timeout='10'/>
      </source>
      <target dev='tap2'/>
      <model type='virtio'/>
      <driver name='vhost' queues='4' rx_queue_size='1024' tx_queue_size='1024'/>
      <address type='pci' domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
    </interface>
    ```
- 在192.168.1.2上添加192.168.1.2的互信 ssh-copy-id -i .ssh/id_rsa.pub root@192.168.1.3
- 重启网络 systemctl restart network (虚拟机内也能)
- 设置mtu
    ```shell
    ovs-vsctl set interface p0 mtu_request=9058
    ovs-vsctl set interface p1 mtu_request=9058
    ovs-vsctl set interface tap1 mtu_request=9058
    ovs-vsctl set interface tap2 mtu_request=9058
    ovs-vsctl set interface br-dpdk mtu_request=9058
    ovs-vsctl set interface br-int mtu_request=9058

    ovs-vsctl set interface br-ply1 mtu_request=9058
    ovs-vsctl set interface br-ply2 mtu_request=9058
    ovs-vsctl set interface p-ply1-int mtu_request=9058
    ovs-vsctl set interface p-ply2-int mtu_request=9058
    ```
- 查下mtu设置成功没 `ovs-appctl dpctl/show `
- 协议号 6 TCP，17 UDP 1 ICMP
- 删除执行流表 
    ```shell
    ovs-appctl dpctl/flush-conntrack netdev@ovs-netdev zone=3 "ct_nw_src=192.168.2.2,ct_nw_dst=192.168.2.3,ct_nw_proto=17,ct_tp_src=5201,ct_tp_dst=5202"
    ovs-appctl dpctl/flush-conntrack netdev@ovs-netdev zone=3 "ct_nw_src=192.168.2.2,ct_nw_dst=192.168.2.3,ct_nw_proto=17"
    ```
- 查看端口信息 `ovs-vsctl list interface tap1`
- 设置端口信息 `ovs-vsctl set interface tap1 mtu_request=1450`
- 设置vm前端网卡mtu值 ifconfig eth0 mtu 1400
- 服务器重启配置
    ```shell
    python /root/dpdk-devbind.py -s
    modprobe uio igb_uio
    modprobe igb_uio
    python dpdk-devbind.py --bind=igb_uio 0000:03:00.0
    python dpdk-devbind --bind=igb_uio 0000:03:00.0
    python dpdk-devbind --bind=igb_uio 0000:03:00.0
    python dpdk-devbind --bind=igb_uio 0000:03:00.0
    ```

- 如果yum安装失败 `mount -o loop /home/software/CentOS-7-aarch64-Everything-1810.iso /mnt/repo/` 
- 查看设置项 `ovs-vsctl list Open_Vswitch`
- 删除设置项 `ovs-vsctl remove Open_Vswitch . other_config [options]`
- 查看流表 ovs-ofctl dump-flows 网桥名称
    ```
    # cmd = 'ovs-vsctl add-bond br-int bond0 p0 p1 -- set Interface p0
    # type=dpdk options:dpdk-devargs=0000:03:00.0 '
    # '-- set Interface p1 type=dpdk options:dpdk-devargs=0000:04:00.0'
    ```
- 检查cpu亲和性 `ovs-appctl dpif-netdev/pmd-rxq-show`  
- 这次用来查看是否有tap1 的`ll /var/run/openvswitch `
- 进入虚拟机 `virsh console VM0 `
- 查看所有的虚拟机 `virsh list --all` 
- 删除VM10的虚拟机 `virsh undefine VM10 --nvram` 
- 也是删除镜像的？ `r`m -f /home/kvm/images/ `
- 删除镜像 `virsh vol-delete /home/kvm/images/10.img `
- 打印数据库内容概览`ovs-vsctl show ` 
- 加载、卸载、查询以及执行，当前vhostagent所支持的component。`ovs-appctl component list`
- 看物理网卡 `hinicadm info`
- `systemctl status openvswitch`
- `service openvswitch restart`
- 先组个网
    ```
    >>> from base.network import Net
    >>> net = Net()
    >>> net.set_vxlan(tap_num=1,sub=False)
    ```
- 配置env.py 
```
[root@localhost testcase]# hinicadm info
Card num:1
Hi1822 device Information:
     Card         PCIe Function
|----hinic0(ETH_25GE)
         |--------0000:06:00.0(NIC:enp6s0)
         |--------0000:07:00.0(NIC:enp7s0)
```
- 配置`vi /opt/xpf/ovs.ini`
- 查看配置项
```
[root@localhost testcase]# ovs-vsctl find Open_Vswitch
_uuid               : dd8db3d4-2fab-4f93-bfce-7b82011ad70b
bridges             : []
cur_cfg             : 464
datapath_types      : [netdev, system]
db_version          : "8.0.0"
dpdk_initialized    : true
dpdk_version        : "DPDK 19.11.0"
external_ids        : {hostname=localhost, rundir="/var/run/openvswitch", system-id="dd415808-c772-4cf                           1-9db3-dbfbdffe7d4d"}
iface_types         : [dpdk, dpdkr, dpdkvhostuser, dpdkvhostuserclient, erspan, geneve, gre, internal,                            "ip6erspan", "ip6gre", lisp, patch, stt, system, tap, vxlan]
manager_options     : []
next_cfg            : 464
other_config        : {dpdk-init="true", dpdk-lcore-mask="0x3", dpdk-pmd-driver="/lib64/librte_pmd_hin                           ic.so", dpdk-socket-mem="4096", pmd-cpu-mask="0x2"}
ovs_version         : "2.12.0"
ssl                 : []
statistics          : {}
system_type         : centos
system_version      : "7"
```
- 查看成功的配置项
```
[root@localhost testcase]# ovs-vsctl show
dd8db3d4-2fab-4f93-bfce-7b82011ad70b
    Bridge br-dpdk
        datapath_type: netdev
        Port br-dpdk
            Interface br-dpdk
                type: internal
        Port "bond0"
            Interface "bond0"
                type: dpdk
                options: {dpdk-devargs="0000:08:00.0", mode=lacp}
    Bridge "br-ply1"
        datapath_type: netdev
        Port "br-ply1"
            Interface "br-ply1"
                type: internal
        Port "p-int-ply1"
            Interface "p-int-ply1"
                type: patch
                options: {peer="p-ply1-int"}
        Port "tap1"
            Interface "tap1"
                type: dpdkvhostuser
                options: {max_queue_num="4", vm_id="1"}
    Bridge br-int
        datapath_type: netdev
        Port br-int
            Interface br-int
                type: internal
        Port "p-ply1-int"
            Interface "p-ply1-int"
                type: patch
                options: {peer="p-int-ply1"}
        Port "vxlan0"
            Interface "vxlan0"
                type: vxlan
                options: {local_ip="192.168.1.2", remote_ip="192.168.1.3"}
    ovs_version: "2.12.0"
[root@localhost testcase]# ovs-appctl component list
The available components are:
name                            dynamic   dependent
ovs-ct                          N         xpf_flow_agent(id:30)
xpf_flow_agent                  Y         No_dependent_component
ovs-netdev                      N         xpf_flow_agent(id:30)
xpf_ife_agent                   Y         No_dependent_component
list ok.
```




