# 概念
- 域名类型
A 将域名指向一个 IPv4 地址，如 106.55.75.123。 A记录归属地是埃文科技的付费接口，为了防止盗刷，每个用户有查询限制，请节省使用。

AAAA 将域名指向一个 IPv6 地址，如 2402:4e00:1013:e500:0:9671:f018:4947。同一个主机名可以同时解析到 IPv4(A记录)地址 和 IPv6(AAAA 记录)地址上，当只有IPv4 地址的用户会解析到 IPv4 地址，一般情况下有 IPv6 地址的用户会优先解析到 IPv6 地址。

CNAME 将域名指向另一个域名地址，与其保持相同解析，如 static.ipw.cn 别名到 static.ipw.cn.cdn.dnsv1.com

MX 用于邮件服务器，一般由邮件注册商提供，如 mxbiz1.qq.com。如果邮箱格式为 test@ipw.cn 则输入 ipw.cn 查询。如果邮箱格式为 test@mail.ipw.cn则输入mail.ipw.cn查询。推荐2个免费的企业邮箱：腾讯企业邮、网易免费企业邮。

TXT 附加文本信息，常用于域名所有权验证，如在申请 HTTPS 证书时需要增加记录、

PTR IP 的反向解析记录，例如 159.75.190.197 反解析到 ipw.cn，一般用于提升自建域名邮件服务器的可信度，可提单找云服务商添加。

NS 域名的 DNS 服务器地址，例如 ns3.dnsv2.com，推荐 DNSPod.

网站开启IPv6检测 网站开启IPv6检测 | SSL证书在线检查
# 申请一个域名
- [从freenom上申请](https://zhuanlan.zhihu.com/p/115535965)
- 个人信息填的时候要和ip对应(使用china不行)
  - ip信息从[ipaddress](https://www.ipaddress.my/)上看
  - 地址和电话可以从旅游网站上找如(https://www.tripadvisor.cn/Restaurant_Review-g188589-d7285683-)
  - 不一致的话complete order 后会提示“某些原因此订单可能会失败"
- [freenom域名自动续期]https://github.com/luolongfei/freenom
# 域名解析
- CNAME地址： http://hello.youwebcloud.com
- 查看域名是否设置到ip上面可以使用 ping gaoking.top 来看是不是解析到了ip里
# 域名
- 服务商 https://my.noip.com/dynamic-dns 
- 域名 gaoking.zapto.org
# 帮助网站
- 这个比较好
- ping 检测 https://ping.chinaz.com/185.77.225.53
- dns解析 https://www.boce.com/dns/www.gaoking.top
- https://tools.ipip.net/newping.php
- https://www.itdog.cn/
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
  - https://www.v2fly.org/config/dns.html#dnsobject
  - 安装教程https://www.v2ray-agent.com/archives/1680104902581
- 参看core的版本`vasma 16->1>会显示版本`
# 使用
- win V2rayN:
  - 下载:https://kgithub.com/2dust/v2rayN
  - 配置：
    - https://v2rayn.org/
    - 代理方式选择“自动配置系统代理”， 路由方式选择“绕过大陆”。
    - 路由配置：https://amoment.site/p/%E6%96%B0%E7%89%88v2rayn%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%90%86%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AEpac/
    - 如果使用域名改变direct，配置是`domain:erebor.douban.com `而不是`erebor.douban.com` 写在规则里面有example的那个direct规则列表中就行，不用新建了
- 输入 vasma 查看账号

# 管理服务
- cloudcone 上运行工具会乱码，使用xshell登入
- 安装完上面的八合一脚本后，install.sh会删除，vasma 即可打开服务
- 选择1xray-core

# 问题
### io: read/write on closed pipe
- 先看下域名是否失效
- 再看下时区是不是不一样，如果不一样就改下服务器的时区
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
- sms-activate.org 网站注册一个虚拟号
  - link：https://juejin.cn/post/7199657558834692157
# 一些代理
- git: https://juejin.cn/post/7210744398640595005
  - 


# openAI
- organization：org-KJCQAA8sLPd0vagGsygofPcL
- 254774511744 +254 (774) 51 17 44 
- API key: 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

# windows 开代理后one note和micrsoft  Store 连不上网络的问题 0x80131500
- Microsoft Store等软件绕过V2ray全局代理 https://zhuanlan.zhihu.com/p/413730301
```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1609473798-1231923017-684268153-4268514328-882773646-2760585773-1760938157
# restore
CheckNetIsolation.exe loopbackexempt -d -p=S-1-15-2-1609473798-1231923017-684268153-4268514328-882773646-2760585773-1760938157
```
- 然后还是没有用，把网络适配器删掉了，然后重新配置，打开代理又好了，真奇怪

- 后面通过设置v2ray解决，设置-解除UWP应用回环代理设置 然后在新窗口中勾选全部的点击保存就可以了 每次重启后都要重新设置的

