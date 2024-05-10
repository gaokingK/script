# ansible
- link:
    -  ansible 常用模块: 
        - https://www.cnblogs.com/keerya/p/7987886.html
        - https://www.cnblogs.com/www233ii/p/11997368.html#service%E6%A8%A1%E5%9D%97
    -  Ansible playbook格式: https://www.cnblogs.com/keerya/p/8004566.html
    -  Ansible中文权威指南：http://ansible.com.cn/docs/intro_configuration.html?highlight=gather_facts
    - automation-controller： https://docs.ansible.com/automation-controller/4.0.0/html_zh/userguide/overview.html
    - https://getansible.com/advance/playbook/tasks
    - 看这个文档：https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html
    - 如何使用Ansible local_action模块在本地执行任务 https://juejin.cn/post/7122350498732048397
- 一些规范的介绍：
    - inventory文件，定义变量和目标机器
    - playbook 定义在哪组节点上执行那些role
    - module 如copy是一个module负责复制、file是一个module，负责文件
    - playbook的风格有ini风格和yaml风格
    - 可以用all关键字 一次性操作清单中的所有主机
- 一些自定义变量：https://www.cnblogs.com/breezey/p/9275763.html
    - inventory_hostname是Ansible所识别的当前正在运行task的主机的主机名，如果在inventory里定义过别名，那么这里就是那个别名
- 任务的执行状态
    - link:https://zhuanlan.zhihu.com/p/587770251
    - sucess或succeeded：通过任务执行结果返回的信息判断任务的执行状态，任务执行成功则返回true
    - failure或failed：任务执行失败则返回true
    - change或changed：任务执行状态为changed则返回true
    - skip或skipped：任务被跳过则返回true
## tips
- shell 模块的参数要用单引号包括起来，双引号和单引号的效果是不同的`'sed -i "/rule_files/a\  - /etc/alerts/{{cluster}}-common.yaml\n  - /etc/alerts/{{cluster}}-quantdo.yaml"  {{appdir}}/prometheus/etc/prometheus-config.yaml'`双引号会报错
- 参看帮做的命令 ansible-doc -s shell
## 命令参数
- https://www.cnblogs.com/keerya/p/7987886.html
- ansible的：https://docs.ansible.com/ansible/latest/cli/ansible.html#ansible

- m 指定要使用的模块
- -e -a 指定参数时没有具体的模式，反正下面几种换着来就对了
- e 指定额外参数 一个变量使用一个-e
  - 也可以这样`ansible my_host -m shell -a "mkdir test" -e "{'chdir': '/tmp', 'creates': '/tmp/test'}"`
- a 指定这个模块的参数，就像配置文件中写在该模块下面的内容
  - The action’s options in space separated k=v format: -a ‘opt1=val1 opt2=val2’ or a json string: -a ‘{“opt1”: “val1”, “opt2”: “val2”}’
-i INVENTORY #指定主机清单的路径，默认为/etc/ansible/hosts 没有会报错
``` 
# 常用命令 注意会在host所指定的机器上面都会产生影响
ansible testB -m template -e "testvar1=redhat" -a "src=test1.j2 dest=/opt/test1" ## 这个命令会报错
ansible all -i rootfs/deploy/inventory_10.0.5.44.yaml -m template -a "src=/root/deploy-20230529/rootfs/deploy/templates/new_worker_exporter.yaml dest=/apt/hi.yaml" # ansible 后面要加主机组名， 路径要写绝对路径或者相对路径
ansible test-group -m debug -a "msg={{inventory_hostname}}"
# sudo chroot rootfs /bin/sh -c "unset LANG;/usr/local/bin/ansible all -i /tmp/all_monitor_workers.yaml -m shell -a 'sed -i /http.*{{master}}/s/{{master}}/$new_master/ /apt/promtail/opt/promtail-config.yaml'"
# sudo chroot rootfs /bin/sh -c "unset LANG;/usr/local/bin/ansible all -i /tmp/all_monitor_workers.yaml -m service -a '{\"name\": \"promtail\", \"state\": \"restarted\"}'"
```
- vvv 看到命令的完整报错
### 命令报错
- 命令要指定主机清单，否则会报[WARNING]: Could not match supplied host pattern, ignoring: servers
- https://blog.csdn.net/weixin_33919950/article/details/93467666

## module
- link:
  - https://blog.csdn.net/qq_52993001/article/details/117483364
  - https://blog.csdn.net/m0_49265034/article/details/119825995
  - 所有module：https://docs.ansible.com/ansible/latest/collections/index_module.html
### setup 可以收集机器的一些信息
- https://www.cnblogs.com/young233/p/15094346.html
- gather_facts: on，如果我们使用，即可让ansible去收集各机的信息。
```
- hosts: whatever
  gather_facts: no or yes  #决定是否开启收集功能
```
### copy
```
- name: migrate_prometheus_conf2
  copy: 
    src: prometheus-config.yaml # 会在一些目录下搜索，可以随便写个路径，搜索不到的话在报错信息里会提示从那些路径中搜索这个文件
    dest: "/apt/"
  when:
    - new_master
    - inventory_hostname in new_master
```
### file
```
- name: workspace exist
  file:
    path: "{{appdir}}"
    state: directory
# 这个的bin是在files文件夹内
- name: upload binary
  copy:
    src: "bin/proc_exporter"
    dest: "/usr/bin/proc_exporter" 
    mode: "a+rx"
```
### fetch https://docs.ansible.com/ansible/latest/collections/ansible/builtin/fetch_module.html#ansible-collections-ansible-builtin-fetch-module
```
- name: fetch all_monitor_workers.yaml
  fetch:
    src: "{{ appdir }}/all_monitor_workers.yaml"
    dest: "{{appdir}}/all_monitor_workers.yaml" 
    # 1. 如果是相对路径，这个路径是相对于playbook的位置的，如果是绝对路径，就是绝对路径，不过如果是rootfs内的那么是rootfs的绝对路径
    # 2. 会存放在all_monitor_workers.yaml/hostname/srcfilename
    # 3. 
  when:
    - inventory_hostname in master
```
### template
- link:
  - https://blog.csdn.net/qq_35887546/article/details/105266675
  - https://www.cnblogs.com/wanstack/p/8650687.html
模板语法的缩进会影响结果的缩进
```
# 格式一
  "amoduleset":{
{% for r in apprules %}
    "{{r.name}}",
{% endfor %}
# 格式二
  "amoduleset":{
    {% for r in apprules %}
    "{{r.name}}",
    {% endfor %}
# 虽然{{r.name}}的缩进没有变，但格式一和格式二的结果是不一样的
```
ansible会根据"模板"文件，为每一台主机生成对应的配置文件，大致步骤如下：
1、找一个现成的redis配置文件，作为"模板"文件，你可以从之前安装过redis的主机中拷贝一份，也可以从redis的rpm包中提取一份。
2、修改模板文件，将IP设置部分使用变量进行替换。
3、使用ansible调用"template"模块，对"模板文件"进行渲染，根据模板生成每个主机对应的配置文件，并将最终生成的配置文件拷贝到目标主机中。

- 调试方法
```
# 模板文件 test1.j2
[root@server4 jinja2]# cat test1.j2 
test jinja2 variable
test {{ testvar1 }} test
# 调试命令
ansible testB -m template -e "testvar1=redhat" -a "src=test1.j2 dest=/opt/test1" # 这个命令会报错，但把内容放到palybook里去执行就不会出错
ansible all -i rootfs/deploy/inventory_10.0.5.89.yaml -m template -a "src=rootfs/deploy/templates/new_worker_exporter.yaml dest=~/jjw-deploy0529/new_worker_exporter.yaml"  这样也可以

# 查看结果
[root@server3 opt]# cat test1 
test jinja2 variable
test redhat test
```
- 不会报错的
``` 
---
- hosts: exp
  remote_user: root
  tasks:
  - name: Install Apache by YUM
    yum: name=httpd state=installed
  - name: Config Apache
    template: src=httpd.conf.j2 dest=/etc/httpd/conf/httpd.conf
$ansible-playbook tmp.yml -e "listen_port=81" 
```
- if 会判断变量是否为空，不会判断变量是否定义
### unarchive 解压文件
- link：https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html
### shell 模块， 可以用env中的cp防止找不到命令
- link: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html#examples
- 有点命令要用引号包括'curl -X GET  https://0848-140-206-192-11.ngrok-free.app/alerts/update_conf' ,有点就不用ls /apt
- 假如是用的rootfs内的ansible，使用shell可以访问该rootfs外的文件`sudo chroot rootfs /bin/sh -c "unset LANG;/usr/local/bin/ansible-playbook -i $inventory_path2 /deploy/master_install.playbook.yaml"`
```cs
命令行中使用shell 不用加cmd
ansible my_host -m shell -a "mkdir test" -e "{'chdir': '/tmp', 'creates': '/tmp/test'}"
- name: This command will change the working directory to somedir/ and will only run when somedir/somelog.txt doesn't exist
  ansible.builtin.shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/
    creates: somelog.txt

# You can also use the 'cmd' parameter instead of free form format.
- name: This command will change the working directory to somedir/
  ansible.builtin.shell:
    cmd: ls -l | grep log
    chdir: somedir/
- name: copy local dns resolv conf
  shell: "env cp /etc/resolv.conf {{appdir}}/django/etc/resolv.conf"
  when: xxx
# sed只有这样才能输入空格
shell: "sed -i '/{{item}}/d;/hosts:$/a\\    - {{item}}' {{appdir}}/all_workers.yaml" 后面的\\要有两个，正常只有一个 如果sed不适用双引号，那么a后面只需要一个斜杠
```


## 条件控制
- link:
    - Ansible条件判断的介绍和使用 https://zhuanlan.zhihu.com/p/587770251
### when
- link: 
  - 多个an / or条件 https://www.codenong.com/44838421/
  - 更多判断的指标 https://www.jianshu.com/p/e972dd8c1557
```cs
- name: start log mounts
  service:
    name: "{{appdir|trim('/')|replace('/','-')}}-promtail-{{['hlogs',item]|join('')|trim('/')|replace('/', '-')}}.mount"
    state: restarted
    enabled: yes
  when: inventory_hostname != "10.0.5.89"

- role: firewalld
  when:
    - firewall_enable == 'true'
    - inventory_hostname in workers or inventory_hostname in add_workers
# 判断循环长度大于多少才执行
  loop: "{{ add_workers }}"
  when:
    - add_workers
    # - add_workers != '' # 这个没有用 不知道怎么判断为空
    - add_workers != None 要用这样
    - ansible_loop.length > 3
  loop_control:
    extended: true
# 判断变量是否存在 不加循环的时候只有when这两个条件就可以
- https://stackoverflow.com/questions/35105615/ansible-use-default-if-a-variable-is-not-defined
- name: variable is not null
  debug:
    msg: "add_workers is[{{ add_workers }}], item is [{{ item }}]"
  loop: "{{ query('item', add_workers|default([])) }}"
  when:
    - add_workers 
    - add_workers != None
```
- variable is define/undefine 变量定义了就为true，不管有没有值
- when: output | bool 必须是能转换为bule的值yes、on、1、true结果才为true，否则就为false
### loop
- link:
  - 高级 https://blog.csdn.net/qq_35887546/article/details/105249631
  - doc: https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_loops.html
  - query/lookup
    - 语法："{{ query('item', add_workers|default([])) }}"
    - 两个使用的插件是通用的
    - 所有的插件https://docs.ansible.com/ansible/latest/collections/index_lookup.html
    - items 把变量换为列表
    - list 如果有嵌套列表，不展开
    - lines 从命令行执行 "{{ lookup('lines', \"pwd\") }}" 位置是playbook的位置
```cs
# 从自定义变量loop
loop:
  - django
  - grafana
  - loki
  - prometheus
# 从inventory的变量loop
loop: "{{ logmounts }}"
```
### delegate_to
- link: https://blog.csdn.net/xixihahalelehehe/article/details/113702903
- 指定某一台主机
## task
- link:https://blog.csdn.net/Lem0n_Tree/article/details/106218719
- 忽略错误 
```cs
    - name: Shell Command
      command: /bin/false
      ignore_errors: yes #忽略错误 ture 也可以
```
- 任务运行一次
  - link:https://cloud.tencent.com/developer/ask/sof/105954727
```
    - name: update all_monitor_workers.yaml
      debug:
        msg: "{{ lookup('lines', \"pwd;sed -i '1adddd' /tmp/all_monitor_workers.yaml \")}}"
      run_once: true
```
## role
- 可以使用include引用别的角色
- 可以加上tag，来执行某个tag https://blog.caoyu.info/ansible-role-tags.html
## inventory 怎么写
- all关键字中只能有 "vars", "children" and "hosts" 这三个key，其他的key只能在这三个key里面
hosts中的ip要以冒号结尾，下面可以写tag
```
---
all:
  hosts:
    10.0.5.44:
    10.0.5.89:

``` 
## playbook
- link：
    - 变量：https://www.cnblogs.com/lvzhenjiang/p/16102588.html
    - https://www.cnblogs.com/lvzhenjiang/p/16060637.html
- 如果指定多个用户组，就以`,`分隔
- 如何在playbook里修改发起ansible命令的主机上的内容
```
      debug:
        msg: "{{ lookup('lines', \"pwd;sed -i '1addd' /tmp/all_monitor_workers.yaml \")}}"
      when:
        - inventory_hostname in master 这个是保证运行一次的
# 还有一种办法就是把这个文件复制到remote后修改后再复制回来
```
- 一个playbook里可以写多个host的任务
```
hosts 后面也能放多个用户组
---
- hosts: localhost  # 将 A 主机作为目标主机
  tasks:
    - name: Modify file on A host
      lineinfile:
        path: /path/to/file_on_a_host
        line: "some_setting = new_value"
        state: present

- hosts: my_host_b  # 将 B 主机作为目标主机
  tasks:
    - name: Task on B host
      # Add your tasks for host B here
```
- 只能读入当前使用的组里面定义的变量，如果有同名的变量会并集；如果使用未在hosts中包含的组的变量，需要通过set_fact结合hostvars的方式，实现了跨play获取其他主机中的变量信息的功能
- 变量被引用时如下，处于开头的位置且当使用冒号为模块的参数赋值时 需要加上引号`"{{ nginx.conf80 }}"`后面就不用跟空格了
```
---
- hosts: test181
  remote_user: root
  vars:
    nginx:
      conf80: /etc/nginx/conf.d/80.conf
      conf8080: /etc/nginx/conf.d/8080.conf
  tasks:
  - name: task1
    file:
      path:"{{ nginx.conf80 }}"
      state=touch
  - name: task2
    file:
      path={{ nginx['conf8080'] }} # 使用等号就不用
      state=touch
```
- playbook的风格有ini风格和yaml风格
```cs
#仍然先写出INI风格的示例以作对比，如下
[proA]
192.168.99.181
 
[proB]
192.168.99.182
 
[pro:children]
proA
proB
 
#对应YAML格式的配置如下
all:
  children:
    pro:
      children:
        proA:
          hosts:
            192.168.99.181:
        proB:
          hosts:
            192.168.99.182:
#上述配置表示，pro组有两个子组，分别为proA组和proB组，而这两个组分别有自己组内的主机。
```
- children关键字表示当前组中存在子组
- 里面可以指定任务：
```
- hosts: centos
  gather_facts: true
  any_errors_fatal: yes
  become: yes
  max_fail_percentage: 0
#  roles:
#    - role: cleanupworker
#      when: inventory_hostname in workers
  tasks:
    - name: test
      shell: "echo hhh"

```
## 输出
```cs
$ bash install

PLAY [centos] ******************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************
ok: [10.0.5.44]
ok: [10.0.5.89]

TASK [firewalld : add host subnets] # firewalld 为role名字，后面的时任务名称 ********************************************************************************************************
skipping: [10.0.5.89] => (item=192.168.110.0/24dd)
skipping: [10.0.5.44] => (item=192.168.110.0/24dd)
skipping: [10.0.5.89]
skipping: [10.0.5.44]

TASK [firewalld : reload service firewalld] ************************************************************************************************
skipping: [10.0.5.89]
skipping: [10.0.5.44]

TASK [nginx : create user] *****************************************************************************************************************
ok: [10.0.5.89]
ok: [10.0.5.44]
```
# 问题：
- Failed to parse /deploy/inventory_10.0.5.44 with ini plugin: Invalid host pattern '---' supplied, '---' is normally a sign this is a YAML file.
    - 解决办法，inventory文件加上.yml后缀名
    - 也有可能是yaml的格式不对
    ```
      hosts:
        10.0.5.44: # 这里不能带-
          tag: "10.0.5.44-tag"
        10.0.5.89:
          tag: "10.0.5.89-tag"
    ```
