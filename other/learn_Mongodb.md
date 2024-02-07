# TO： 关于mongodb监控指标的一些内容 & 其他的内容
# 其他内容
- 连接字符串：
```cs
mongodb://username:password@remotehost:27017/mydatabase
# 多ip
mongodb://host1:27017,host2:27017,host3:27017/mydatabase
```
- 使用命令行连接
```cs
bin/mongo -host 10.0.70.4 -port 27017 -u bizseer -p 8Qllyhy! --authenticationDatabase admin
# -u 用户名
# -p 密码
# admin 数据库
```
# 一些概念
### "mongos instance"：这是指当前正在运行的 mongos 实例，是 MongoDB 分片集群中的路由器组件，用于处理客户端的查询请求。
###  CSRS 是 MongoDB 集群中用于存储集群配置信息的副本集

### mongodb的jumbo' chunks是什么意思啊
在 MongoDB 中，"jumbo chunks" 是指分片集合（sharded collection）的某些分片上的数据块（chunks）变得过大而无法再进行均匀的分片。这种情况通常发生在数据平衡（balancing）过程中。

MongoDB使用分片键（shard key）将集合的数据分成多个块（chunks）并分布到不同的分片服务器上，以实现数据的分布和负载均衡。每个块都有一个特定的大小（默认为64MB），当某个块的大小超过这个限制时，它被称为 "jumbo chunk"。

"Jumbo chunks" 可能会导致数据分布不均匀，因为它们无法再均匀地分片到其他分片上。这可能会影响系统性能和可伸缩性。为了解决这个问题，通常需要进行手动干预，将 jumbo 块分割成更小的块，以便它们可以重新均匀地分布到不同的分片上。

要解决 "jumbo chunks" 问题，可以使用 `split` 命令将 jumbo 块分割为更小的块，然后让 MongoDB 自动将它们分片到其他服务器上。在实际操作中，需要小心处理这个问题，以避免数据不一致和性能问题。确保在执行分片操作时备份数据以防止意外数据丢失。

# 其他内容
### mongodb架构
https://cloud.tencent.com/document/product/240/64126?from_cn_redirect=1


### 在 MongoDB 中，"outgoing scoped synchronous connections" 是指针对每个 MongoDB 驱动程序或客户端在执行操作时创建的一种连接类型。这些连接是针对特定的操作（如查询或写入）而创建的，且通常在操作完成后被释放。

以下是这一术语中的关键部分的解释：

- "Outgoing" 表示这是从客户端到 MongoDB 服务器的连接，即客户端发出的请求。

- "Scoped" 表示这些连接是有范围的，它们与特定操作相关联，并且通常用于处理单个操作。它们不是全局共享的连接，而是在需要时按需创建，并在操作完成后被释放。

- "Synchronous" 表示这些连接通常是同步的，它们等待操作完成后才会返回结果。与之相对的是异步连接，它们不会等待操作完成，而是允许同时执行多个操作。

这些 "outgoing scoped synchronous connections" 在 MongoDB 驱动程序中是常见的，它们用于执行数据库操作，如查询、写入和更新。每次客户端执行操作时，都会创建一个或多个这样的连接，这些连接在操作完成后会被释放，以便其他操作可以使用它们。

总之，这些连接是为了支持客户端与 MongoDB 服务器之间的通信，并在客户端执行数据库操作时起到关键作用。这有助于确保操作的有序性和可靠性。

### 关于jumbo chunk及chunk size
MongoDB默认的chunk size为64 MB，如果chunk超过64 MB且不能分裂（假如所有文档的Shard Key都相同），则会被标记为jumbo chunk，balancer不会迁移这样的chunk，从而可能导致负载不均衡，应尽量避免。

当出现jumbo chunk时，如果对负载均衡要求不高，并不会影响到数据的读写访问。如果您需要处理，可以使用如下方法：
对jumbo chunk进行split，split成功后mongos会自动清除jumbo标记。
对于不可再分的chunk，如果该chunk已不是jumbo chunk，可以尝试手动清除chunk的jumbo标记。
说明 清除前，您需要先备份config数据库，避免误操作导致config库损坏。
调大chunk size，当chunk大小不超过chunk size时，jumbo标记最终会被清理。但是随着数据的写入仍然会再出现jumbo chunk，根本的解决办法还是合理的规划Shard Key。
需要调整chunk size（取值范围为1~1024 MB）的场景：
迁移时I/O负载太大，可以尝试设置更小的chunk size。
测试时，为了方便验证效果，设置较小的chunk size。
初始chunk size设置不合理，导致出现大量jumbo chunk影响负载均衡，此时可以尝试调大chunk size。
将未分片的集合转换为分片集合，如果集合容量太大，需要（数据量达到T级别才有可能遇到）调大chunk size才能转换成功。具体方法请参见Sharding Existing Collection Data Size。

### mongodb 监控项：节点每秒钟 command 请求次数，这个告警的阈值应该设置为多少呢
ChatGPT
阈值的设置通常取决于您的特定应用程序和部署环境。为了设置适当的阈值，您需要首先了解您的 MongoDB 部署的性能基线和正常操作的范围。然后，您可以将阈值设置为超出这些正常操作范围的一定百分比，以便在超出正常操作时触发告警。

具体阈值的设置因环境和用例而异，但以下是一些一般性的考虑：

性能基线：首先，监控一段时间内的节点每秒 command 请求次数，了解正常操作的范围。这将成为您设置阈值的基准。

负载：考虑服务器的硬件资源和负载。如果您的硬件资源（CPU、内存、磁盘等）在正常操作期间已经高度利用，那么较低的请求速率可能需要触发告警。相反，如果硬件资源有很大的闲置，您可以容忍更高的请求速率。

特定用例：不同的应用程序和用例可能具有不同的访问模式和请求频率。某些用例可能需要更高的请求速率才能正常工作，而其他用例可能可以容忍较低的速率。

季节性变化：有些应用程序可能在一天中的某些时间段内或特定的季节性活动期间会产生更多的请求。您可能需要根据这些变化来动态调整阈值。

容忍度：最终，根据您的容忍度来设置阈值。如果您更注重性能和稳定性，您可能会设置较低的阈值，以便在问题出现之前尽早发出告警。如果您更注重可伸缩性和容错性，您可以设置更高的阈值以延迟告警。

根据上述考虑因素，您可以监测命令请求速率并逐渐调整阈值，以找到最适合您的特定 MongoDB 部署的值。定期回顾和调整阈值是维护监控系统的关键部分，以确保它对您的需求保持敏感。

###  Reports the total number of outgoing connections from the current mongos instance to other members of the sharded cluster that are currently being refreshed.
"mongos instance"：这是指当前正在运行的 mongos 实例，是 MongoDB 分片集群中的路由器组件，用于处理客户端的查询请求。

"outgoing connections"：这是 mongos 实例主动发起的与其他分片集群成员之间的连接。这些连接通常用于查询和数据路由等操作。

"to other members of the sharded cluster"：这表明这些连接是与 MongoDB 分片集群中的其他成员（如分片服务器、副本集成员等）建立的。它们用于与分片集群的不同部分进行通信。

"currently being refreshed"：这表示这些连接当前正在被刷新或更新。这可能意味着 mongos 正在执行某些操作，例如重新加载分片路由信息或重新连接到其他成员。在这种情况下，这些连接可能会被关闭并重新打开。

总的来说，这个监控指标报告了从当前 mongos 实例到分片集群中其他成员的出站连接总数，并指出这些连接当前正在进行刷新或更新操作。这个监控信息可能有助于监视 mongos 与其他分片集群成员之间的连接状态，尤其是在执行一些需要连接刷新的操作时。

### Number of open cursors with the option DBQuery.Option.noTimeout set to prevent timeout after a period of inactivity.
"Number of open cursors"：这是指在 MongoDB 数据库中已经打开的游标（cursors）的数量。游标用于查询操作，允许逐批地获取大量文档而不会一次性加载全部数据。

"with the option DBQuery.Option.noTimeout set"：这部分描述说明这些游标是使用特定选项设置的。具体来说，它们使用了 DBQuery.Option.noTimeout 选项。这个选项的作用是为游标设置不超时的特性，意味着游标在一段时间的不活动之后不会自动超时关闭。

"to prevent timeout after a period of inactivity"：这部分描述解释了为什么使用了 DBQuery.Option.noTimeout 选项。这是为了防止游标在一段不活动时间后自动关闭。游标通常会在一段时间内没有新的请求或操作时被服务器自动关闭，以释放资源。但通过设置 noTimeout 选项，可以防止游标在不活动期间自动关闭。

综合来看，这个监控指标表示具有特定设置（DBQuery.Option.noTimeout）的打开游标的数量，这些游标不会因为一段时间内没有活动而自动关闭。这对于某些需要维护长时间打开的游标的应用场景可能很有用，以避免在不活动期间丢失游标的状态。
### Number of pinned open cursors
"Number of pinned open cursors" 表示打开的并且被固定（pinned）的游标数量。在 MongoDB 中，游标是用于查询的数据库对象，允许在一次查询中逐批地获取结果而不一次性加载整个结果集。游标可以在查询操作之间保持打开状态。

这个监控指标关注的是被固定的游标数量。游标固定通常是在特定的使用情境下使用的一种技术，例如长时间运行的查询或持久化游标。游标固定后，它们不会在不活动一段时间后自动关闭，这有助于保持查询的上下文和状态。

游标固定适用于以下情况：

长时间运行的查询：当需要执行长时间运行的查询，例如数据分析或大批量数据处理时，可以使用游标固定来确保查询的中间结果在不活动时不会丢失。

持久化游标：有些应用需要在多次查询之间保留游标的状态。例如，在某些分页查询中，用户需要浏览多个页面，而游标固定可以确保在页面之间保留查询状态。

监控 "Number of pinned open cursors" 有助于了解系统中长时间运行或需要持久状态的查询的数量，这可以帮助管理数据库资源和查询性能。

### Number of cursors that MongoDB is maintaining for clients
"Number of cursors that MongoDB is maintaining for clients" 表示 MongoDB 正在为客户端维护的游标数量。在 MongoDB 中，游标是用于查询的数据库对象，允许在一次查询中逐批地获取结果而不一次性加载整个结果集。这个监控指标跟踪了当前由 MongoDB 服务器管理的活动游标的数量。

这个监控指标关注的是 MongoDB 服务器正在管理的游标数目。每当客户端执行查询时，服务器会为其分配一个游标，用于迭代查询结果。一旦查询结束或游标不再使用，MongoDB 将关闭游标以释放资源。游标的数量可以用来衡量系统中正在进行的查询操作和查询资源的使用情况。

监控 "Number of cursors that MongoDB is maintaining for clients" 对于理解 MongoDB 数据库的查询活动以及资源管理非常有用。它可以用来检测查询负载的高低、系统资源的使用情况以及是否存在过多的游标未被释放。这些信息对于性能调整和故障排除都非常有帮助。

### Number of cursors that time out, per second.
"Number of cursors that time out, per second" 表示每秒钟游标超时的数量。在 MongoDB 中，游标是用于查询的数据库对象，它们用于逐批地获取查询结果而不是一次性获取整个结果集。游标通常有一个超时时间，一旦超过这个时间，游标将被关闭以释放资源。

这个监控指标跟踪了每秒钟因超时而关闭的游标数量。如果客户端打开了游标但在规定的超时时间内没有读取或获取足够的数据，服务器将自动关闭游标以避免资源浪费。这个指标的监测可以帮助管理员了解在 MongoDB 系统中游标的使用情况，是否存在查询阻塞或客户端未及时处理查询结果的情况。

在监控 "Number of cursors that time out, per second" 时，如果发现该值非常高，可能需要检查查询性能、客户端应用程序是否有效处理了游标，以及系统负载是否过高等问题。通常，较高的游标超时率可能会影响性能和资源利用效率。
### The number of "getmore" operations the mongos per second. This counter can be high even if the query count is low.
这监控指标描述了 mongos 实例每秒执行的 "getmore" 操作的数量。"getmore" 是 MongoDB 中用于从游标获取更多数据的操作，通常与查询操作一起使用。这个计数器即使在查询操作数量较低的情况下也可能很高，因为它与游标的使用有关。

在分析这个监控指标时，以下是一些考虑因素：

getmore操作的性能开销：高 "getmore" 操作速率可能意味着查询的结果集很大，需要多次 "getmore" 操作来获取完整结果。这会增加服务器的工作负载，因此需要关注这个指标以确保不会对性能产生负面影响。

应用程序查询和游标使用：这个指标的意义在于了解您的应用程序如何使用游标和查询。一些查询可能返回大量数据，导致 "getmore" 操作的频率上升。在某些情况下，这可能是正常的行为。

告警阈值：设置适当的告警阈值通常需要根据您的应用程序的特定需求和正常操作模式来决定。阈值的选择应基于性能基线数据，这些数据反映了正常操作时的指标值。一种常见的方法是将阈值设置为平均或正常情况下的 "getmore" 操作速率的两倍，以确保在异常情况下触发告警。

根据您的具体用例和性能要求，建议从正常操作的性能数据开始，了解 "getmore" 操作速率的典型范围，然后设置阈值。一般来说，如果 "getmore" 操作速率显著超过正常范围，可能需要触发警报，以便您能够及时检查并解决性能问题。这个阈值的确切值可能因环境而异，因此需要不断监控并进行调整。

### The latest optime of the CSRS primary that the mongos has seen.
这个监控指标描述了 mongos 实例所看到的 CSRS（Config Server Replica Set，配置服务器副本集）主节点的最新的 oplog 时间戳（optime）。oplog 是 MongoDB 的操作日志，用于复制和恢复操作。CSRS 是 MongoDB 集群中用于存储集群配置信息的副本集。

在这个监控指标中，"optime" 表示操作的时间戳，是 CSRS 主节点中 oplog 记录的一个标识。mongos 通过检查 CSRS 主节点的 oplog 来了解最新的操作，以便在分片集群中路由查询请求和数据写入操作。

通过监控 mongos 所看到的 CSRS 主节点的最新 optime，您可以了解到 mongos 的操作是否与 CSRS 主节点上的配置信息同步。如果监控指标的值长时间没有更新，可能表示 mongos 无法正常访问或与 CSRS 主节点同步配置信息。这可以是一个潜在的问题，因为 mongos 需要实时的配置信息来正确路由查询请求。

要设置合适的告警阈值，通常需要根据您的 MongoDB 部署和性能需求来评估。监控这个指标可以帮助您及早发现配置同步问题并采取适当的措施来解决。通常，如果最新 optime 长时间未更新，可能需要触发警报以便进行诊断和维护。
"The latest optime of the CSRS primary that the mongos has seen" 是 MongoDB 中的一个监控指标，通常表示当前 mongos 实例所观察到的 CSRS 主节点的最新操作时间（optime）。如果这个指标异常，可能有以下原因和解决办法：

**异常原因**：

1. **CSRS 主节点宕机**：如果 CSRS 主节点宕机或不可用，mongos 无法获取新的操作时间。

**解决办法**：

1. **监控 CSRS 主节点**：首要解决办法是监控 CSRS 主节点的状态。如果 CSRS 主节点宕机或不可用，需要尽快修复它，确保它的正常运行。

2. **检查网络连接**：确保 mongos 实例与 CSRS 主节点之间的网络连接正常。如果网络中断或有问题，它可能影响到 mongos 能否获取 CSRS 主节点的操作时间。

3. **查看 MongoDB 日志**：查看 MongoDB 的日志以获取有关 CSRS 主节点的任何错误或异常情况的更多信息，这可能有助于定位问题。

4. **故障转移**：如果 CSRS 主节点不可用，确保你的 MongoDB 部署实现了故障转移机制，以便在主节点宕机时可以自动切换到备用节点。

需要特别注意的是，该监控指标异常通常是 MongoDB 集群的问题，而不仅仅是 mongos 实例的问题。因此，维护和监控整个 MongoDB 集群对于确保系统的可用性和稳定性非常重要。解决问题时需要仔细检查并定位根本原因。

### Difference between the latest optime of the CSRS primary that the mongos has seen and cluster time.
这个监控指标描述了 mongos 实例所看到的 CSRS（Config Server Replica Set，配置服务器副本集）主节点的最新的 oplog 时间戳（optime）与集群时间（cluster time）之间的差异。

"optime" 是 CSRS 主节点上操作的时间戳，是 oplog 记录的一部分，用于复制和恢复操作。而 "cluster time" 是 MongoDB 集群内部用于协调操作的时间标记。

这个监控指标的含义在于评估 mongos 实例与 CSRS 主节点之间的配置同步延迟。具体来说，"latest optime of the CSRS primary" 表示 CSRS 主节点上的最新操作时间戳，"cluster time" 表示集群内部协调操作的时间。

如果这个监控指标的值为正数，表示 mongos 的配置信息相对于集群内部的时间标记是滞后的，也就是 mongos 尚未看到 CSRS 主节点上最新的操作。如果这个差异的值较大并持续增加，可能表示 mongos 与 CSRS 主节点之间的同步延迟较大。这可以是一个潜在的问题，因为 mongos 需要实时的配置信息来正确路由查询请求。

要设置合适的告警阈值，通常需要根据您的 MongoDB 部署和性能需求来评估。监控这个指标可以帮助您了解配置同步延迟情况，及早发现问题并采取适当的措施来解决。如果同步延迟持续增加，可以触发警报以进行诊断和维护。

### 上面两个监控指标的不同
这两个监控指标都与 MongoDB 中的 CSRS（Config Server Replica Set，配置服务器副本集）有关，但它们关注的方面略有不同：

"The latest optime of the CSRS primary that the mongos has seen" 描述了 mongos 实例所看到的 CSRS 主节点的最新 oplog 时间戳（optime）。这个指标告诉您 mongos 当前知道的 CSRS 主节点的 oplog 时间戳。它与 mongos 和 CSRS 主节点之间的配置同步有关，确保 mongos 拥有最新的配置信息。

"Difference between the latest optime of the CSRS primary that the mongos has seen and cluster time" 描述了 mongos 实例看到的 CSRS 主节点的最新 oplog 时间戳与集群时间（cluster time）之间的差异。这个指标用于评估 mongos 与 CSRS 主节点之间的配置同步延迟，即 mongos 在其配置信息中的时间戳与集群时间之间的差异。

简而言之，第一个指标提供了 mongos 当前所了解的 CSRS 主节点的 oplog 时间戳，而第二个指标提供了 mongos 的配置时间戳与集群时间之间的差异。这两个指标都用于监控和评估 mongos 与 CSRS 主节点之间的配置同步情况，以确保正确路由查询请求并维持配置信息的实时性。

在实践中，您可以同时监控这两个指标，以更全面地了解配置同步的状况。如果时间戳的差异较大或持续增加，可能需要采取措施来减小同步延迟，以确保系统正常运行

### mongodb有个两个监控指标的描述分别为：
1. Rate of all incoming connections created to the server.
2. The number of incoming connections from clients to the database server.
你能跟我解释下这两个指标的不同吗
ChatGPT
这两个监控指标涉及到 MongoDB 数据库服务器的连接，但它们关注的方面有所不同：

"Rate of all incoming connections created to the server" 描述了 MongoDB 服务器创建的所有入站连接的速率。这个指标衡量了数据库服务器接受新连接的速度，无论这些连接是来自客户端、驱动程序、mongos 实例还是其他服务器的。它通常以每秒钟创建的连接数量来表示。

"The number of incoming connections from clients to the database server" 描述了当前连接到 MongoDB 数据库服务器的客户端的数量。这个指标表示当前活动的客户端连接数，通常是一个瞬时值，反映了服务器上的并发连接数。

简而言之，第一个指标关注连接的创建速率，是一个速率或流量指标，用于监控连接活动的增长趋势。而第二个指标关注当前连接数，提供了实时的连接状态信息，用于监控服务器的负载和连接资源的使用情况。

这两个指标通常一起使用，以便完整地了解 MongoDB 服务器上的连接活动。如果第一个指标显示连接速率持续增加，而第二个指标显示连接数持续高于正常水平，这可能表明服务器正经历连接问题，需要进一步调查和处理。

###
mongodb有个两个监控指标的描述分别为：
1. The number of unused incoming connections available.
2.The total number of available outgoing connections from the current mongos instance to other members of the sharded cluster.
你能跟我解释下这两个指标的不同吗

这两个监控指标关注 MongoDB 数据库服务器的连接，但涉及不同类型的连接和方向：

"The number of unused incoming connections available" 描述了当前 MongoDB 数据库服务器中可用的未使用的入站连接数。这些未使用的连接是服务器已经建立但尚未分配给客户端或请求的连接，通常用于提高连接响应速度，以便在需要时可以迅速提供连接。这个指标有助于了解服务器上可供客户端连接的剩余连接数。

"The total number of available outgoing connections from the current mongos instance to other members of the sharded cluster" 描述了当前 mongos 实例到分片集群中其他成员的可用出站连接的总数。在 MongoDB 分片集群中，mongos 实例需要与各个分片服务器通信，这包括请求和路由数据。这个指标反映了 mongos 实例维护的用于与分片服务器通信的连接总数。

这两个指标不同之处在于一个关注了服务器接受客户端连接的情况，另一个关注了 mongos 实例与分片服务器之间的连接。第一个指标表示未分配的入站连接，而第二个指标表示 mongos 实例的出站连接。通过监控这两个指标，您可以更好地了解服务器连接资源的利用情况，以及 mongos 实例与分片服务器之间的连接状态。