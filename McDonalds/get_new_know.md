### CommonRequest
- 是阿里云官方推出的、泛用型的OpenAPI调用接口，您可以使用CommonRequest，实现任意OpenAPI接口的调用
- https://developer.aliyun.com/article/512398

### WAF
- Web应用防火墙（Web Application Firewall，简称WAF）
- 能够帮助您的网站防御OWASP TOP10常见Web攻击和恶意CC攻击流量，避免网站遭到入侵导致数据泄露，全面保障您网站的安全性和可用性。您可以参考本文中的接入配置和防护策略最佳实践，在各类场景中使用WAF更好地保护您的网站。

### CNAME
- https://blog.csdn.net/DD_orz/article/details/100034049
- 通常来讲域名会解析出来一个ip，这种对应关系成为A记录；从域名到ipV4的对应关系成为A记录，此外域名还能解析出来一个域名，解析出来的域名就称为CNAME；CNAME通常用在CDN上面


### ACS
- 为了降低 K8s 的使用和运维复杂度，解决资源和容器割裂的问题，我们设计了容器计算服务 ACS

### 负载均衡
- 一文带你了解SLB、F5、Nginx负载均衡：https://blog.csdn.net/Jiao1225/article/details/122733116

### 四层负载均衡和七层负载均衡
- 4层（TCP协议）和7层（HTTP和HTTPS协议）的负载均衡服务。
- 判断是否要负载均衡的标准不同
    - 四层的负载均衡，就是通过发布三层的IP地址（VIP），然后加四层的端口号，来决定哪些流量需要做负载均衡；然后对需要处理的流量进行 NAT 处理，转发至后台服务器，并记录下这个 TCP 或者 UDP 的流量是由哪台服务器处理的，后续这个连接的所有流量都同样转发到同一台服务器处理。
    - 七层的负载均衡，就是在四层的基础上，再考虑应用层的特征。
    - 例如，同一个 Web 服务器的负载均衡，除了根据 VIP 和80端口辨别是否需要处理的流量，还可根据七层的 URL、浏览器类别、语言来决定是否要进行负载均衡。
- 这些url就是属于应用层的内容
- 七层负载均衡要根据真正的应用层内容选择服务器，只能先代理最终的服务器和客户端建立连接(三次握手)后，才可能接受到客户端发送的真正应用层内容的报文，然后再根据该报文中的特定字段，以及负载均衡设备设置的服务器选择方式，决定最终选择的内部服务器。负载均衡设备在这种情况下，更类似于一个代理服务器。负载均衡和前端的客户端以及后端的服务器会分别建立 TCP 连接。

### F5(F5 Network Big-IP)
- 是一个网络设备，可以简单的理解成类似于网络交换机的东西，性能是非常的好，每秒能处理的请求数达到百万级，当然价格也就非常非常贵了，十几万到上百万人民币都有。
- F5会以一定的频率去探测一组服务器资源可用的port，之后提供一个统一的虚拟IP，应用请求到这个虚拟的IP后，F5会请求转发到服务器资源中能够处理请求的服务器里，之后把response响应给请求方。

### VirtualService
- link：https://developer.baidu.com/article/details/3277416
- Istio是一个开源的服务网格解决方案，它提供了一种灵活且强大的方式来管理和控制微服务架构中的服务间通信。在Istio中，VirtualService是一个核心概念，它允许用户定义如何路由进入服务的流量。通过VirtualService，可以实现诸如灰度发布、故障注入、A/B测试等高级功能。

### Endpoints
- link: https://blog.csdn.net/catoop/article/details/122072608
- Endpoints 是一组实际服务的端点集合。一个 Endpoint 是一个可被访问的服务端点，即一个状态为 running 的 pod 的可访问端点。一般 Pod 都不是一个独立存在，所以一组 Pod 的端点合在一起称为 EndPoints。只有被 Service Selector 匹配选中并且状态为 Running 的才会被加入到和 Service 同名的 Endpoints 中。


### parpet
- 管理机器linux配置