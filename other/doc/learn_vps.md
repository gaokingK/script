# 申请一个域名
- [从freenom上申请](https://zhuanlan.zhihu.com/p/115535965)
- 个人信息填的时候要和ip对应(使用china不行)
  - ip信息从[ipaddress](https://www.ipaddress.my/)上看
  - 地址和电话可以从旅游网站上找如(https://www.tripadvisor.cn/Restaurant_Review-g188589-d7285683-)
  - 不一致的话complete order 后会提示“某些原因此订单可能会失败"
- [freenom域名自动续期]https://github.com/luolongfei/freenom
# 域名解析
- CNAME地址： http://hello.youwebcloud.com
## rDNS(reverse DNS) 可逆DNS, 把ip地址解析到域名， http://ip 会跳到网站里
## 在freedom中设置DNS
- Services -> My Domains 
- Managements tools -> Nameservers (Use default nameservers (Freenom Nameservers) 选中)
- Manage Freenom DNS
  - Name: null; Type: A; TTL: 3600; Target: ip;
  - save Changes; 等待半个小时左右？
  - 设置好的话输入域名就会看到拒绝连接，而不是

# 部署
- 工具采用[八合一共存脚本+伪装站点](https://github.com/mack-a/v2ray-agent)
  - 选择xray-core
  - 安装完成后使用13（安装BBR、DD脚本）
    - 选择 BBR原版+FQ
    ```
    TCP加速 一键安装管理脚本 [v1.3.2.100] from blog.ylx.me 母鸡慎用
    0. 升级脚本
    9. 切换到不卸载内核版本        10. 切换到一键DD系统脚本
    1. 安装 BBR原版内核
    2. 安装 BBRplus版内核          5. 安装 BBRplus新版内核
    3. 安装 Lotserver(锐速)内核    6. 安装 xanmod版内核
    11. 使用BBR+FQ加速             12. 使用BBR+FQ_PIE加速
    13. 使用BBR+CAKE加速
    14. 使用BBR2+FQ加速            15. 使用BBR2+FQ_PIE加速
    16. 使用BBR2+CAKE加速
    17. 开启ECN                    18. 关闭ECN
    19. 使用BBRplus+FQ版加速
    20. 使用Lotserver(锐速)加速
    21. 系统配置优化               22. 应用johnrosen1的优化方案
    23. 禁用IPv6                   24. 开启IPv6
    25. 卸载全部加速               99. 退出脚本
    ———————————————————————————————————————————————————————————————
    系统信息: CentOS 7.9.2009 KVM x86_64 5.15.12
    当前状态: 已安装 BBR 加速内核 , BBR启动成功
    当前拥塞控制算法为: bbr 当前队列算法为: fq
    请输入数字 :
    ```
  - window 中使用的v2rayN 要用Torjan那个连接
- 帮助：
  - https://github.com/ylx2016/Linux-NetSpeed
  - https://www.v2ray-agent.com

# 管理服务
- cloudcone 上运行工具会乱码，使用xshell登入
- 安装完上面的八合一脚本后，install.sh会删除，vasma 即可打开服务
- 选择1xray-core

# v2ray、xray
- [区别](http://www.vjsun.com/656.html)
## 数据传输协议
- VLESS 是一种无状态的轻量级数据传输协议，被定义为下一代 V2ray 数据传输协议
- TLS 将是接下来三到五年内躲避封锁的主流方式
- V2ray 之前因性能不好而被一些人唾弃，VLESS 协议的出现，让 V2ray 的便利性和性能达到 trojan 的高度（使用 TLS 的情况下）。仅有 VLESS 还不够，套了一层 TLS，V2ray 的性能依然不如 SS、SSR。但随 VLESS 协议而来的另一个大惊喜：XTLS。（个人认为）这是划时代的概念和技术，将 V2ray 的性能提升到、甚至超越 SS/SSR 的水平。

# 其他
- [gooreplacer](https://github.com/jiacai2050/gooreplacer/)
  - 资源拦截替换, 把请求的某些资源重置到别的地方获取，这样资源就能加载了

### 手机共享vpn
- 打开终端输入route print
- 将路由表中的192.168.136.245填入设置->代理中的地址输入框中
```cs
网络目标        网络掩码          网关       接口   跃点数
0.0.0.0          0.0.0.0  192.168.136.245  192.168.136.213     55
```
- 保持v2rayN关闭，就可以使用vpn了，如果想要更新v2rayN中的一些内容，需要将V2rayN中的代理设置改为不改变系统代理