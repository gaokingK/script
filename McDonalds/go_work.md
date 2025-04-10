### 0402
- 详情页 虚拟机 网络设备
- 资源概览
- 数据采集 中间件 数据库 k8s 技术
- 关联 虚拟机 物理机 ip子网 技术
- 

### 问题记录
- 检查生产门店分配集群的数据
- 更换wukong chardet包为支持许可证的开源软件
- 处理puppet配置修改工单申请权限的bug

- 给iaas新建aws集群
- 项目表字段清洗，去掉多余的字符 
- 如果有异常的事务未回滚，会影响别的请求吗

### 0324
- 费用预估 所有人
- 审计日志查看- idc只能看idc的 cloud看clound
- 定价策略 修改 infra-admin 查看rts
- 
- sqlalchemy 有失败时，影响范围有哪些 本会话，其他会话 mysql客户端 如果时本会话，本会话的什么操作会影响
```
riase exception_a from exception_b

db.bulk_save_objects(all_data)
 File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1364, "Field 'id' doesn't have a default value")
db.query(VirtualMachine).count()
File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\sqlalchemy\orm\session.py", line 973, in _raise_for_prerequisite_state
    raise sa_exc.PendingRollbackError(
sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.OperationalError) (1364, "Field 'id' doesn't have a default value")
```
### 0319
- 区域default变换值
### 0317
- office-vc归到hedan还是putuo
- onecloud 归到哪里呢
### 0314
- clound为空的字段怎么办
- start_fail running ready unknown
### 0313
  #842323 - 

rgb(0, 214, 65)
rgb(26, 164, 72)
rgb(14, 111, 47)
rgb(8, 84, 33)
i5-8300h 7408
i7-8750H 9854
i5-6300U 3222
i5-9300H 7529
i7-9750H 10750
i5-10200H 8028



### 0307
1. cluster新增编辑里没有新增标签 修改里没有删除标签  表头k8s_ip里不对


1. 补偿dev环境集群改为生产导致的未校验属性
2. 修改用户填写错误的集群属性
3. 
### 0305
- ip校验 最后一个,号分割
- 校验失败提示
- market改成只能是一个维度的

- domain的数据放到clound_account 
- resource_id删去
- 把tags里的数据再拿出来
- domain、group_count、user_count/description/mcd_project/clound/cloud_subscription/resource_uid


- 虚拟机取得时候不包括调度失败的

### 0304
- 修改表结构
alter table server_cluster_create_ticket_data add column k8s_ip varchar(128) not null default ""  comment "k8s ip", 
add column ob_ip varchar(128) not null default ""  comment "ob ip",
add column ob_vip varchar(128) not null default ""  comment "ob vip";

alter table store_cluster add column k8s_ip varchar(128) not null default ""  comment "k8s ip", 
add column ob_ip varchar(128) not null default ""  comment "ob ip",
add column ob_vip varchar(128) not null default ""  comment "ob vip";
### 0221
- 加data_center 和机房room
- cloud_account 为空
- hd pt tengxun ali store office 
- 网络设备
- cloud_manager -> cloud_subscription
- cloud
- cloud_account
- data_center
- 
### 0219
- cpu_count -> cpu
- os_type - > os_version
- image 删去
- 宿主机 取名字
- 二层网络和ip子网关联 删去
- auto_start 删除
- external_ip -> eip
- owner不要
- created_by update_by 删去


- 平台字段内容换一下 换成hd pto ali tengxun
- 安全组 null 去掉；改成名字
- vpc 不要 换成ip子网
- 
- resource_id -> 云上id

# 网络设备
- 加date_center数据中心 putuo、hedan
- 
- 加一个字段放房间信息

### 0217
- 看puppet子流程发布申请人权限问题
- 改使用率校验
  - 是校验新机器放进去后集群的使用率，但是挪到第一步的时候这个机器还没有真正放进去，因为后面工单可能会审批决绝，而且有可能同时有多个工单都分配的这个集群
- 改堡垒机跳转

### 0214 Q!@34mcd  Q!@34mcn
- 修改模型定义
- 沟通根据集群查询门店接口信息
- 堡垒机授权问题
cn-wukong-rstorets05-edge01.mcd.store
### puppet配置修改流程发布回滚
- 尽量不要回滚
- 回滚后这个工单就不能继续发布了，只能回滚完全部已发布的子流程并取消工单
- 当工单回滚后，在下次工单提交前要同步各分支，否则在下次合并的时候会发生从冲突
```cs
回滚的顺序：
从临时分支合并到了uat
从uat合并到了production
从production合并到了第一批的分支（zone01 zone02 zone03 zone04) 
假如此时发现需要回滚
第一批分支回滚production合过来的merge
production回滚uat合过来的merge
uat回滚临时分支合过来的merge
点击取消工单
然后需要提一个uat到production分支的merge request用来将uat上的revert记录同步到production
提一个production到zone01分支的merge request用来将uat和production上的revert记录同步到zone01
提一个production到zone02分支的merge request用来将uat和production上的revert记录同步到zone01
...
提一个production到zone04分支的merge request用来将uat和production上的revert记录同步到zone01

然后再提交新的puppet配置修改工单
....

```
### 0212
- production上的合并请求revert不了
```shell
# 回滚production 没操作
git checkout production
git pull
git revert 65d706267 9bb9ba15
git push

# 回滚uat的改动
git checkout uat
git pull 
git revert 3d7883
git push

# 将production合并到了uat
# 又将uat合并到了production
```
### 0211
- 版本发布
- 模型设计
- 根据集群查询门店接口文档
- puppet问题排查
- https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/merge_requests?scope=all&utf8=%E2%9C%93&state=all
- puppetfile 提交历史https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/commits/production/Puppetfile
- puppet 文件内容 https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/blob/uat/Puppetfile
- 392
- Merge newbranch392 into uat 267 
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
- Merge uat into production 266
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'

- 393
- Merge newbranch393 into uat 268
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- Merge uat into production 269 closed 2025-02-11 17:17:40
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d' uat是403d
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- Merge uat into production -- 271
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- 当前合并冲突 Merge uat into production 276
  :commit => '09977aff00d6413b5f20ba9ff92dbde80b1bd00a' ours 3d7883c4 
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5' theirs

- uat 提交
- 3d7883c4 yanyan 
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
  :commit => '09977aff00d6413b5f20ba9ff92dbde80b1bd00a'
- 4df57e0e infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- production提交
- 65d70626 yanyan
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- 4df57e0e infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
- ac55e8dc Revert "Merge branch 'newbranch392' into 'uat'"
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- a590733c Revert "Merge branch 'uat' into 'production'"
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- c4179cfe infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'

- 
- 为什么合并又回滚的内容再次合并到uat能成功，而合并到production就不成功，是因为到uat的merge_request是一个新分支提的，而到production的还是uat

- merge request 268合并成功 回滚失败
问题原因 是因为从!269可以看到uat中内容和prod内容不一致，因为prod回滚分支后，uat未和prod同步
### 0210
- hedan puduo 
- 


### 0122
- 数据中心一致
- 生产环境才校验编号，其他不校验


### 0115
1. 集群容量预警逻辑修改
2. 集群使用率计算需适配不同容量
3. 集群查询时使用率过滤逻辑修改
4. 由于需要获取store_count 需要把之前表中的store_count删除
5. 首页集群查询加上分页
```sql
-- 修改store_cluster
ALTER TABLE store_cluster DROP COLUMN store_count, drop column market_count, drop column do_count, drop column utilization;
-- 修改store_cluster
alter table store_cluster add column sku varchar(24) not null default "" comment "集群sku";
alter table store_cluster add column rancher_cluster_id varchar(100) not null default "" comment "rancher集群id";
-- 修改server_cluster_create_ticket_data
alter table server_cluster_create_ticket_data add column sku varchar(24) not null default "" comment "集群sku";
alter table server_cluster_create_ticket_data add column rancher_cluster_id varchar(100) not null default "" comment "rancher集群id";
```
### 0106
- 那个设备，了解在网络边界中处于那个位置
- 申请人有几个 5 个
- 可以把操作人加到消息通知里
- dev 没有标签 删除集群的数据，只保留1个
- 改成中文

ingress_ip DTO store_cluster ticket里
env = fields.String(required=True, 
                    validate=validate.OneOf(["sit", "uat", "pt", "prod"]),
                    error='env可选值为["sit", "uat", "pt", "prod"]')

### 0103
- 修改acl 
alter table acl_rule modify source_port varchar(512) not null comment '源cidr port',  modify dest_port varchar(512) not null comment '目标cidr port';

-- 修改server_config_release_ticket_data
alter table server_config_release_ticket_data add column op_users varchar(256) not null default "" comment "可操作发布回滚的用户";
-- 修改AccessRecordData中user_account 为 nickname
alter table access_record_data change user_account nickname varchar(64) NOT NULL COMMENT '访问用户账号';
alter table access_record_data change user_name username varchar(64) NOT NULL COMMENT '访问用户名';

-- 修改ip字段
alter table store_cluster add column ingress_ip varchar(25) not null default "" comment "ip信息";
alter table server_cluster_create_ticket_data change ip ingress_ip varchar(25) not null default "" comment "ip信息";


1
411024199504278567 18737329773
411024199801290765 13963966532
411024199801290765 18237497786
411024199801290765 
3
411024199801290765 15290618188
411024199801290765 15290618188
411024199801290765 18237497786
411024199801290765 15290618188
411024199801290765 15290618188



### 0102
- 有些规则的protocol解析成了source
- 需要将反掩码转换成正掩码
- 有的协议还没有算出来
### 1225
- DNS自动化配置新建申请 -> WuKong CaseA集群申请DNS-{集群名称}
- cluster id 排序
- celery 消息补偿

### 120
提示词工程  编排 工作流
- alter table server_cluster_create_ticket_data add column domain varchar(100) not null default "";


### 1219
- 修改数据库
```sql
alter table store_cluster add tags json comment "标签信息";
alter table store_cluster change gateway domain varchar(100);

alter table server_cluster_create_ticket_data drop column gateway;
alter table server_cluster_create_ticket_data add column data_center varchar(32) not null default "" comment "机房中心" after env;
alter table server_cluster_create_ticket_data add tags json comment "标签信息" after domain;
```
### 1205
- 申请人也会修改吗
修改查询集群接口结果为倒序
- 修改集群 生产对应生产、uat/dev 随便选
- 返回dns检查信息
- 集群日期查询过滤
- 添加集群后添加集群表
- 图表中空数据怎么办
### 1203
- 版本上线 
  - 添加case a 外部接口token
- 修改数据库
```sql
-- 新增集群流程 注意更新id
INSERT INTO wukong_iaas.approval_processes
(id, created_at, updated_at, is_deleted, process_name)
VALUES(9, '2024-11-07 13:23:22', '2024-11-07 15:34:52', 0, 'CASE_A集群修改流程');
INSERT INTO wukong_iaas.approval_processes
(id, created_at, updated_at, is_deleted, process_name)
VALUES(10, '2024-12-06 14:40:43', '2024-12-06 14:40:43', 0, '创建集群流程');


INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(49, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '用户填写信息', 0, 1, 'CASE_A集群修改流程第一步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(50, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, 'infra审批', 0, 2, 'CASE_A集群修改流程第二步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(51, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '执行变更', 0, 3, 'CASE_A集群修改流程第三步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(52, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '完成', 0, 4, 'CASE_A集群修改流程完成');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(58, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '已取消', 0, -1, 'CASE_A集群修改流程取消');

INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(53, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '已取消', 0, -1, '已取消');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(54, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '用户提交信息', 0, 1, '工单提交');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(55, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, 'Infra审批', 0, 2, 'Infra审批');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(56, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, 'DNS生效中', 0, 3, 'DNS生效中');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(57, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '完成', 0, 4, '完成');

-- wukong_iaas.server_cluster_create_ticket_data definition

-- wukong_iaas.server_cluster_create_ticket_data definition

CREATE TABLE `server_cluster_create_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `cluster_name` varchar(100) NOT NULL COMMENT 'cluster name',
  `env` varchar(24) NOT NULL COMMENT 'cluster env',
  `gateway` varchar(100) NOT NULL COMMENT '网关信息',
  `ip` varchar(25) NOT NULL COMMENT 'ip信息',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `domain` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
)COMMENT '新建集群工单详情';

--
alter table store_info add column cluster_id int NOT NULL default '-1' after store_id, add index idx_cluster_id (cluster_id);
alter table store_info add column do_name varchar(64) NOT NULL default '' after market_city_name_cn;
alter table store_info add column ownership varchar(32) NOT NULL default '' after do_name;

-- wukong_iaas.store_cluster definition

CREATE TABLE `store_cluster` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `cluster_name` varchar(100) NOT NULL COMMENT 'cluster name',
  `env` varchar(24) NOT NULL COMMENT 'cluster env',
  `store_count` int NOT NULL COMMENT '门店数量',
  `market_count` int NOT NULL COMMENT '市场数量',
  `do_count` int NOT NULL COMMENT 'DO数量',
  `utilization` float NOT NULL COMMENT '集群使用率',
  `gateway` varchar(100) NOT NULL COMMENT '网关信息',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`)
) COMMENT '集群信息';

-- wanglin
ALTER TABLE server_foreman ADD COLUMN model VARCHAR(100) DEFAULT '' COMMENT 'model_name';
ALTER TABLE store_info ADD COLUMN node_num INT NOT NULL DEFAULT 0 COMMENT '节点数量';
ALTER TABLE store_apply_ticket_data ADD COLUMN node_num INT NOT NULL DEFAULT 0 COMMENT '节点数量';
ALTER TABLE store_apply_ticket_data ADD COLUMN store_cluster VARCHAR(100) DEFAULT ''COMMENT '门店所属集群';
ALTER TABLE store_info ADD COLUMN in_process  tinyint NOT NULL DEFAULT '0' COMMENT '是否在流程中';

插入流程
INSERT INTO wukong_iaas.approval_processes
(id,  is_deleted, process_name)
VALUES(9,  0, 'CASE_A集群修改流程');

INSERT INTO wukong_iaas.approval_process_nodes
(is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES (0, 9, '用户填写信息', 0, 1, 'CASE_A集群修改流程第一步')
VALUES (0, 9, 'infra审批', 0, 2, 'CASE_A集群修改流程第二步')
VALUES(0, 9, '执行变更', 0, 3, 'CASE_A集群修改流程第三步')
VALUES(0, 9, '完成', 0, 4, 'CASE_A集群修改流程完成')
VALUES(0, 9, '已取消', 0, -1, 'CASE_A集群修改流程取消');


CREATE TABLE change_cluster_ticket_data (
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    is_deleted INT NOT NULL DEFAULT '0' COMMENT '是否删除',
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'id',
    ticket_id INT NOT NULL COMMENT '关联的工单id',
    store_id VARCHAR(256) NOT NULL COMMENT '门店id',
    store_name_cn VARCHAR(256) NOT NULL COMMENT '门店中文名',
    group_name VARCHAR(128) NOT NULL COMMENT 'group',
    node_num INT NOT NULL DEFAULT '0' COMMENT '节点数',
    cluster_id INT NOT NULL COMMENT '集群id',
    cluster_name VARCHAR(128) NOT NULL COMMENT '集群名字',
    province_name VARCHAR(128) NOT NULL COMMENT 'gis info 省',
    market_city_name_cn VARCHAR(128) NOT NULL COMMENT 'gis info 市场名',
    do_name VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'do姓名',
    ownership VARCHAR(32) NOT NULL DEFAULT '' COMMENT '所有权',
    open_status VARCHAR(50) NOT NULL COMMENT 'gis info 市场名', 
    change_cluster_id INT NOT NULL COMMENT '改变的集群id',
    change_cluster_name VARCHAR(100) NOT NULL COMMENT '改变的集群名字',
    PRIMARY KEY (id)
) COMMENT='Store Change Cluster Ticket Data';
```
### 1020
- dev uat 手动填 prod自动分配 
- 512 算占用率 可以大于100% 
- 大于80% 发消息提醒 4000 1100 cl x00 
- 
- do分散
- 一个集群保证有两个市场
- 一个集群里直营、dl、cl是有比例的

- 分配逻辑
- 集群展示功能 查询可以先不做 新建流程也先不做
- 门店管理筛选功能先不做 展示功能先做
- 查询有哪些集群、 集群内有哪些门店、门店在哪个集群
- 门店申请流程里的可以先不上
- puppet发布批次里没有门店增加一行没有门店信息
- 消息通知里流程名改成发布计划名称
- 修改f5返回
- 1节点域名信息要在申请门店第一步就展示吗？
```json

				"id": 3392, 1
				"name": "ITO-2117", 1
				"destination": ":443", 
				"partition": "VRF_Test",
				"full_path": "/VRF_Test/ITO-2117",
				"virtual_ip": "10.126.152.21",
				"route_domain": "1",
				"servers_port": "443",
				"ip_protocol": "tcp",
				"source": "0.0.0.0%1/0",
				"last_modifiedTime": "",
				"enabled": "1",
				"master": "hedan-F5/NDC-Test-LB01/172.18.129.252",
				"pool_name": "tob_sit_443",
				"pool_full_path": "/VRF_Test/tob_sit_443",
				"pool_monitor": "/Common/tcp",
				"created_at": "2024-11-05T14:30:49",
				"updated_at": "2024-11-05T14:30:49",
				"pools": [
					{
						"id": 27817,
						"name": "10.126.156.165:30443",
						"partition": "VRF_Test",
						"fullPath": "/VRF_Test/10.126.156.165:30443",
						"monitor": "default",
						"address": "10.126.156.165%1",
						"ip_addr": "10.126.156.165",
						"port": "30443",
						"master": "hedan-F5/NDC-Test-LB01/172.18.129.252",
						"pool_full_path": "/VRF_Test/tob_sit_443"
					},

```

### 1113
https://ninja-dev.mcdchina.net/api/stores?page=1&page_size=50
https://ninja-dev.mcdchina.net/iaas_swagger
![alt text](imgs/go_work.image.png
- 但用这样的连接这样才能访问：https://boss.dev.mcdonalds.cn/api/inner/devops/devops-wukongiaasserv/api/inner/devops/devops-wukongiaasserv/iaas_swagger/index.css
```
CREATE TABLE `msg_notice` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `msg` text NOT NULL COMMENT '消息详情',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`)
) ;
```
### 1108
```py
'ip_addr':virtual_ip, # 可以用原来的virtualip代替 = f5_vip_pool.virtual_ip
'file_name':file_name,  #  可以用原来的代替 = f5_vip_pool.master
'port':port,   # 可以用原来的代替 = f5_vip_pool.server_port
'pools':pools, 对应的f5_node里的ip和port
'account':FILE_ENV_MAP.get(file_name,'')
```
- 数据的处理使用fastapi内置的方法
- port 是从 destination 里解析出来的，新数据没有该字段 可以用lbconfig中的port代替，部分时一样的可能时更新的日期不一样导致的
- 缺少pool表（一对多）缺少member_ip和member_port
### 1106
- 修改审计日志获取信息逻辑
- 将user信息放到g对象中 发现有些用户在user中不存在 继续修改
- 处理大小写
- puppet流程增加权限校验
- 修改审计日志解析用户信息逻辑
- 修改puppet发布子流程企微通知样式 修复门店重复
- 
### 1104
```sql
-- 审计日志新增表
CREATE TABLE `access_record_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `opt_module` varchar(64) NOT NULL COMMENT '操作模块',
  `opt_type` tinyint NOT NULL DEFAULT '0' COMMENT '请求类型',
  `opt_desc` varchar(256) NOT NULL COMMENT '操作描述',
  `opt_module_path` varchar(128) NOT NULL COMMENT '方法路径',
  `url` varchar(256) NOT NULL COMMENT '请求url',
  `ip` varchar(15) NOT NULL COMMENT '请求url',
  `require_args` text NOT NULL COMMENT '请求参数',
  `res_code` int NOT NULL COMMENT '返回状态码',
  `res_msg` varchar(256) NOT NULL COMMENT '返回信息',
  `res_body` text NOT NULL COMMENT '返回data',
  `user_name` varchar(64) NOT NULL COMMENT '访问用户名',
  `user_account` varchar(64) NOT NULL COMMENT '访问用户账号',
  PRIMARY KEY (`id`)
)COMMENT '审计日志数据';
-- 修改server_config_release_data
ALTER TABLE server_config_release_data modify batch_res text NOT NULL Default "" Comment "发布详情";
ALTER TABLE server_config_release_data modify merge_id varchar(256) NOT NULL Default "" Comment "合并iid";
-- wanglin
ALTER TABLE server_state ADD COLUMN out_band_ip  VARCHAR(20) NOT NULL DEFAULT '' COMMENT '带外ip';
```
### 1030
- 代理ip不准、操作人不准ok、操作类型换成请求方式ok、操作名称 ok
- 分页 排序是倒序 ok
- 重置报错 ok
- 分页报错
- 回滚完不能再次发布把发布按钮置灰
- 流程完成 取消 按钮灰色 
- 加日志 ok
- uat发布失败的不能是已回滚

```py
def test(self, branch_name):
    code, msg, data = self.puppet_service.merge_branch_service(branch_name, "uat")
    if not data:
        logger.error("{source_branch}发布失败: " + msg.strip())
        return "第一次发布失败"
    else:
        merge_id = data["merge_request_id"]
    code, msg, res = self.puppet_service.rollback_branch_service(int(merge_id))
    code, msg, data = self.puppet_service.merge_branch_service(branch_name, "uat")
    if not data:
        logger.error("{source_branch}发布失败: " + msg.strip())
        return "{source_branch}发布失败: " + msg.strip()
    return "success"
```

### 1025
将每个mergid分别放到回滚任务队列中；将状态改为回滚中，返回
任务逻辑：如果回滚失败，写入msg和mergeid到表 回滚成功，将msg回写
如何识别回滚部分失败和全部失败呢，此函数只注册一个任务、由这个任务里去循环调用回滚任务，每个任务执行完后将结果写回表，这样前端页面就可以实时刷新
所有任务完成后，判断批次的结果

### 1023
- 修改server_config_change_data
- 需要安装jwt
```sql
-- wukong_iaas.server_config_release_data definition
ALTER TABLE server_config_release_data modify batch_res text NOT NULL Default "" Comment "发布详情";
ALTER TABLE server_config_release_data modify merge_id varchar(256) NOT NULL Default "" Comment "合并iid";

```
### 1021
- 首页增加一个工单状态(ticket_status)，现在状态改为发布状态(release_status) ok
- 新建申请页面和审批页面修改批次时会报错，获取到的内容直接填到输入框里，批次内容不包括uat和dev（我会在接口里去掉这两个） ok
- 编辑分批的时候将批次1的内容删除后不在其他批次的可选框中 ok
- 发布计划名称和变更内容左对齐，其他列居中 
- 发布页面详情默认不展开 ok
- 发布步骤中需要判断是否可以取消（后端会加）必须要把临时分支删除掉 ok

- 未修改不能提交 ok
- 修改详情接口优化 
- 校验完模板后如果再次修改文件就不用校验了
- 取消里都要加入删除分支 ok
- 发布时判断发布时间过期 ok
- 时间判断大于一个小时 ok
- 分批不包括uat dev ok
- infra审批页面编辑 ok
- 配置详情 
- 首页排序从大到小 ok
- 修改详情美化
- 合并从prod合并到第一批，第二批 ok
- 加一个弹窗显示分批的信息，里面有该批是zone几 ok
- 发布详情换行 ok
- 改成异步
- ALTER TABLE server_config_release_ticket_data MODIFY COLUMN branch_name VARCHAR(32) DEFAULT '';
- ALTER TABLE server_config_release_ticket_data MODIFY COLUMN first_commit VARCHAR(32) DEFAULT '';
- ALTER TABLE server_config_release_data MODIFY COLUMN batch_res VARCHAR(512);
### 1008
```sql
# store_server_ticket_data 新增role puppet_status两列
alter table store_server_ticket_data add role varchar(50) not null default "" after ticket_id,add puppet_status  varchar(50) not null default ""  after role;
INSERT INTO approval_processes  (process_name)  VALUES('Puppet证书删除流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '完成', 0, 4, '工单完成');

INSERT INTO approval_processes  (process_name)  VALUES('Group修改流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '完成', 0, 4, '工单完成');

INSERT INTO approval_processes  (process_name)  VALUES('新建发布流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '修改配置', 0, 2, '修改配置');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, 'infra审批', 0, 3, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '发布配置', 0, 4, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '完成', 0, 5, '工单完成');
```
# 新增change_server_group_ticket_data存储修改group工单数据
```sql
-- wukong_iaas.change_server_group_ticket_data definition

CREATE TABLE `change_server_group_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `dn` varchar(120) NOT NULL COMMENT 'LDAP的DN',
  `store_id` varchar(256) NOT NULL COMMENT '门店id',
  `env` varchar(50) NOT NULL COMMENT 'env',
  `store_name` varchar(256) NOT NULL COMMENT '门店中文名',
  `hostname` varchar(256) NOT NULL COMMENT 'hostname',
  `ip_addr` varchar(128) NOT NULL COMMENT 'ip_addr',
  `group` varchar(128) NOT NULL,
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `role` varchar(50) NOT NULL COMMENT 'role',
  `puppet_status` varchar(50) NOT NULL COMMENT 'puppet status',
  `new_group` varchar(128) NOT NULL COMMENT '要修改的group',
  PRIMARY KEY (`id`),
  KEY `idx_group` (`group`),
  KEY `idx_dn` (`dn`)
);
```
新增server_config_release_ticket_data存储puppet发布流程数据
```sql
-- wukong_iaas.server_config_release_ticket_data definition

CREATE TABLE `server_config_release_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `title` varchar(256) NOT NULL COMMENT '发布流程标题',
  `batch_num` int NOT NULL COMMENT '分批次数',
  `batch_detail` varchar(512) NOT NULL COMMENT '发布批次详情',
  `user_name` varchar(64) NOT NULL COMMENT '申请用户名',
  `change_desc` varchar(256) NOT NULL COMMENT '修改内容描述',
  `plan_time_l` timestamp NOT NULL COMMENT '计划开始时间',
  `plan_time_r` timestamp NOT NULL COMMENT '计划结束时间',
  `branch_name` varchar(32) NOT NULL,
  `first_commit` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
);
```

# 新增server_config_release_data存储puppet发布子流程数据
```sql
-- wukong_iaas.server_config_release_data definition

CREATE TABLE `server_config_release_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `is_activate` tinyint NOT NULL DEFAULT '0' COMMENT '是否是当前子流程',
  `batch_res` varchar(256) NOT NULL COMMENT '发布详情',
  `merge_id` varchar(64) NOT NULL COMMENT '发布详情',
  `batch_name` varchar(32) NOT NULL COMMENT '批次名',
  `batch_order` tinyint NOT NULL COMMENT '批次顺序',
  `batch_status` tinyint NOT NULL COMMENT '当前批次状态0待发布、1发布中、2发布失败、3发布成功、4回滚中、5回滚失败',
  PRIMARY KEY (`id`)
);
``` 
### 0928
```py
@ticket_bp.route("/test", methods=["GET"])
def test():
    """
    获取修改详情
    :return:
    """
    try:
        data = {
            "process_name": SERVER_PUPPET_SSL_DELETE_PROCESSNAME,
            "desc": "xxxxx-desc",
            "env": "dev",
            "ticket_id": 49
        }
        send_msg2qw(**data)
        ticket_service = TicketService()
        res = ticket_service.is_server_config_process()
        return create_response(200, "ok", data={})
    except Exception as e:
        return create_response(500, str(e), {})
```
### 0919
- 重新编译python
- 编译报错，Could not import runpy module 升级gcc
### 0903
- 删除puppet流程
- 修改server信息的流程
  - 点击某条信息旁边的修改，进入新页面，展示对改server信息的查询结果，数据库中不做任何修改
  - 门店Server信息修改页面：如果点击取消，数据库中也没有任何修改；点击确定，tickiet中插入一条，current为2，同时server_state表中in_process状态为1，把工单数据插入到store_server_ticket_data中
  - 审批页面点击取消：数据库中没有任何修改；点击拒绝，tickiet中current变为-1，同时server_state表中in_process变为0；点击同意，current变为4同时server_state表中in_process变为0
- 执行结果去哪里获取呢？
- group分区中审批角色
### 0822
- k8s相关表加上属性后，假如查询表Ingress，那么结果中可能有该匹配条件的多行，那么需要根据版本进行去重
- 如果某行没有最新版本的数据呢？要展示老数据吗？

### 1008
```sql
store_server_ticket_data 新增role puppet_status两列
# alter table store_server_ticket_data add role varchar(50) not null default "" after ticket_id,add puppet_status  varchar(50) not null default ""  after role;
# INSERT INTO approval_processes  (process_name)  VALUES('Puppet证书删除流程');

INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '完成', 0, 4, '工单完成');

# INSERT INTO approval_processes  (process_name)  VALUES('Group修改流程');

# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '已删除', 0, -1, '申请取消');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '用户提交信息', 0, 1, '工单提交');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, 'infra审批', 0, 2, '工单审批');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '工单执行', 0, 3, '工单执行');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '完成', 0, 4, '工单完成');

# INSERT INTO approval_processes  (process_name)  VALUES('新建发布流程');
# 
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '修改配置', 0, 2, '修改配置');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, 'infra审批', 0, 3, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '发布配置', 0, 4, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '完成', 0, 5, '工单完成');
```
# 新增change_server_group_ticket_data存储修改group工单数据
```sql
-- wukong_iaas.change_server_group_ticket_data definition

CREATE TABLE `change_server_group_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `dn` varchar(120) NOT NULL COMMENT 'LDAP的DN',
  `store_id` varchar(256) NOT NULL COMMENT '门店id',
  `env` varchar(50) NOT NULL COMMENT 'env',
  `store_name` varchar(256) NOT NULL COMMENT '门店中文名',
  `hostname` varchar(256) NOT NULL COMMENT 'hostname',
  `ip_addr` varchar(128) NOT NULL COMMENT 'ip_addr',
  `group` varchar(128) NOT NULL,
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `role` varchar(50) NOT NULL COMMENT 'role',
  `puppet_status` varchar(50) NOT NULL COMMENT 'puppet status',
  `new_group` varchar(128) NOT NULL COMMENT '要修改的group',
  PRIMARY KEY (`id`),
  KEY `idx_group` (`group`),
  KEY `idx_dn` (`dn`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
```
新增server_config_release_ticket_data存储puppet发布流程数据
```sql
-- wukong_iaas.server_config_release_ticket_data definition

CREATE TABLE `server_config_release_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `title` varchar(256) NOT NULL COMMENT '发布流程标题',
  `batch_num` int NOT NULL COMMENT '分批次数',
  `batch_detail` varchar(512) NOT NULL COMMENT '发布批次详情',
  `user_name` varchar(64) NOT NULL COMMENT '申请用户名',
  `change_desc` varchar(256) NOT NULL COMMENT '修改内容描述',
  `plan_time_l` timestamp NOT NULL COMMENT '计划开始时间',
  `plan_time_r` timestamp NOT NULL COMMENT '计划结束时间',
  `branch_name` varchar(32) NOT NULL,
  `first_commit` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
```
新增server_config_release_data存储puppet发布子流程数据
```sql
-- wukong_iaas.server_config_release_data definition

CREATE TABLE `server_config_release_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `is_activate` tinyint NOT NULL DEFAULT '0' COMMENT '是否是当前子流程',
  `batch_res` varchar(256) NOT NULL COMMENT '发布详情',
  `merge_id` varchar(64) NOT NULL COMMENT '发布详情',
  `batch_name` varchar(32) NOT NULL COMMENT '批次名',
  `batch_order` tinyint NOT NULL COMMENT '批次顺序',
  `batch_status` tinyint NOT NULL COMMENT '当前批次状态0待发布、1发布中、2发布失败、3发布成功',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
```
