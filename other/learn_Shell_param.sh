#!/usr/bin/env bash
:<<!
函数参数/命令行参数
命令行参数:
    位置参数: https://www.cnblogs.com/cangqinglang/p/11942567.html
    link2: http://www.361way.com/shellcscd/329.html
        $0 表示程序名。
            如果要使用脚本名称来进行判断，可以先用命令 basename 把路径的信息给过滤掉
        $1 至 \$9则是位置参数。
            超过10个, 要用${10}这样的形式引用, 不用花括号的话，$10 会被认为是 $1 和一个字符 0。
        $# 表示参数的个数。
            ${!#}来返回最后一个命令行参数
        $* 将所有参数当做一个整体来引用
        $@ 把每个参数作为一个字符串返回，可以使用for循环来遍历
        $? 最近一个执行的命令的退出状态。0表示执行成功
        $_ 上一个命令的最后一个参数。使用快捷键 ESC+. 也是这个效果
        shift 默认将每个参数变量左移一个位置（变量$0不变，把$1丢弃，注意 不可以恢复了！)
            在不清楚参数数目情况下，这是一个迭代参数的好办法。
            可 以为shift提供一个参数，来实现多位移变化。
  getopt/getopts
在bash中测试这个参数的取值
set -- 1 2 3
echo $0 # -bash
echo $1 # 1
!
# 位置参数
function position_param(){
    action=$1
    case $action in
        create)
            check_modules
            create_container
        ;;
        stop)
            stop_container
        ;;
        restart)
            check_modules
            restart_container
        ;;
        *)
              echo "unknown action"
              return 1
        ;;
    esac
}
# position $@

# getopts
:<<block
getopts optstring name [args]
    optstring 选项
        下面定义了6个选项 a/b/c/e/f/h
        选项后面加：的是说明能接受参数， 会把这些参数放在OPTARG这个变量当中
        第一个：让getops区分 invalid option (无效选项) 错误和 miss option argument（丢失选项的参数）错误
            当为 invalid option 时 varname 会被设成? 可以在case中使用\? 或者 [?]来匹配
            当为 miss option argument 时 varname 会被设成:
            不以”:“冒号开头，invalid option 错误和 miss option argument 错误都会使 varname 被设成?(但是这样getops会给出提示）
            加不加：$OPTARG都是出问题的选项
    name 变量
    OPTARG 必须是大写
    有一些字母选项具有标准含义最好按照标准含义定义选项意义
block

function getopts_learn() {
    while  getopts :abc:e:f:h argvs ; do
        case $argvs in
        a)
            echo "input is -a, parms is: ${OPTARG}"
            ;;
        b)
            echo "input is -b"
            ;;
        c)
            echo "input is -c, parms is: ${OPTARG}"
            ;;
        e)
            echo "input is -e, parms is: ${OPTARG}"
            ;;
        h)
            echo "input is -h"
            ;;
        f)
            echo "input is -f, parms is: ${OPTARG}"
            ;;
        \?)
            echo "无效或不存在的选项： ${OPTARG}"
            ;;
        [:])
            echo "缺少参数"
            ;;
        esac
    done
}

getopts_learn $@
exit $?