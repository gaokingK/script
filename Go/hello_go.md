# some
- go虽然是把代码写在了一个一个的程序文件当中，但当程序运行的时候，是通过main函数运行的，会运行所有的文件
# module、package、import
### Go Module
- link
    - https://juejin.cn/post/6869570760738865166#heading-10
    - https://www.jianshu.com/p/2d4d0bd7d2e4
    - 一些问题：https://blog.csdn.net/qq_39852676/article/details/121132613
- 一个Module就是package(go 包)的集合. 即: 一个Module含有多个package; 一个package含有多个.go文件.
- Go Modules不是module，Go Modules是 Go 语言中的一种包管理机制，
    - 它通过go.mod 可以帮助开发者有效地管理项目的依赖库和版本，提高开发效率
    - 除了go.mod之外，go命令还维护一个名为go.sum的文件，其中包含特定模块版本内容的预期加密哈希 go命令使用go.sum文件确保这些模块的未来下载检索与第一次下载相同的位，以确保项目所依赖的模块不会出现意外更改，无论是出于恶意、意外还是其他原因。 go.mod和go.sum都应检入版本控制
    - go.sum 不需要手工维护，所以可以不用太关注。
    - 子目录里是不需要init的，所有的子目录里的依赖都会组织在根目录的go.mod文件里
- Modules是相关Go包的集合，是源代码交换和版本控制的**单元**。go命令直接支持使用Modules，包括记录和解析对其他模块的依赖性。Modules替换旧的基于GOPATH的方法，来指定使用哪些源文件。
- 发展历史
    - Go modules 是 Go 语言的依赖解决方案，发布于 Go1.11，成长于 Go1.12，丰富于 Go1.13，正式于 Go1.14 推荐在生产上使用。
    - Go moudles 目前集成在 Go 的工具链中，只要安装了 Go，自然而然也就可以使用 Go moudles 了，而 Go modules 的出现也解决了在 Go1.11 前的几个常见争议问题：
        - Go 语言长久以来的依赖管理问题。
        - “淘汰”现有的 GOPATH 的使用模式。
        - 统一社区中的其它的依赖管理工具（提供迁移功能）。
```go
// go mod init myservice
module example.com/myservice // 模块路径为example.com/myservice 模块名称为myservice
go 1.12
require (
    github.com/gorilla/mux v1.7.3 //依赖的其他模块及其版本
    github.com/go-sql-driver/mysql v1.5.0
)
```
- 模块路径
    - module关键字指定的模块路径表示当前模块的全局唯一标识符，用于声明当前模块所属的命名空间。在Go语言中，每个模块都有一个唯一的模块路径，可以用来区分不同的模块，并确保模块之间的依赖关系不产生冲突。
    - 具体来说，一个模块的模块路径是以域名倒序排列后，在其后面加上模块名所组成的。例如，github.com/user/project就是一个合法的模块路径。
    - 模块路径的作用如下：
        1. 帮助Go工具管理依赖关系。Go工具在下载、安装或更新依赖的时候，会根据模块路径来识别模块并获取其代码。
        2. 确保代码的唯一性。模块路径是全局唯一的，不同的模块使用不同的模块路径，避免了不同的代码库使用相同的包名导致的代码冲突。
        3. 方便模块发布和分发。通过指定模块路径，可以方便地将模块发布到包管理系统或者其他代码仓库中，并能够在不同的项目中方便地复用。
- 一个项目可以有多个模块
    - Go语言的模块化体系允许在一个项目中使用多个模块。每个模块都可以拥有自己的代码和依赖关系，这样可以使项目结构更加清晰和易于维护。在使用Go模块时，建议每个模块都创建一个新的文件夹来存放其代码，且每个模块都拥有自己的go.mod文件来管理其依赖关系。
### package
- link:
    - https://juejin.cn/post/6869570760738865166
- go使用包来组织源代码的，并实现命名空间的管理，任何一个Go语言程序必须属于一个包，即每个go程序的开头要写上`package <pkg_name>`
- Go语言包一般要满足如下三个条件：
1. 同一个目录下的同级(不包括子目录)的所有go文件应该属于一个包；
2. 包的名称可以跟目录不同名，不过建议同名；
3. 一个Go语言程序有且只有一个main函数(多个文件中只能有一个main函数)，他是Go语言程序的入口函数，且必须属于main包，没有或者多于一个进行Go语言程序编译时都会报错；
### import
- 导入的方式是当前文件的相对目录
- 导入的包必须要使用，否则也会报错。
- 如果一个包要引用另一个包的标识符(比如结构体、变量、常量、函数等)，那么首先必须要将其导出，导出的具体做法就是在定义这些标识符的时候保证首字母大写(首字母小写的标识符只能限制在包内引用)。另外在被导出的的结构体或者接口中，只有首字母大写的字段和方法才能被包外访问，而结构体中首字母小写的字段和方法不能被包外访问
- 设置别名 `设置别名引用 import format_go fmt` 别名在前
- import引入的都是包所在的目录名, 只不过因为有条包名要和所在目录同名的这条规范, 所以会给人一种我是导入的包的错觉
- `import _ "crypto/rand" `只执行init函数
- `import path` 指的是import后面跟的路径即`import <import path>`

### 初始化的执行顺序
```css
go run *.go
├── 执行 Main 包
├── 初始化Mian包所有引用的包
|  ├── 初始化引用包的引用包 (recursive definition, 最后导入的包会最先初始化)
|  ├── 初始化全局变量
|  └── 同一个package如果有多个文件，则以文件名的顺序调用各个文件的init 函数（）
└── 初始化 Main 包
   ├── 初始化全局变量
   └── 以文件名的顺序调用main包中的init 函数
   └── main函数

```
![go语言初始化执行顺序](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab0aa8197d44cf79ac693f3257bb90f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp)

- init()与sync.Once对比------no

# build项目
- build命令
    - -o myexec参数，表示指定输出文件名为 myexec。
- build项目
```go
export GOPROXY=https://goproxy.cn
export GOPATH=[source-dir]/gopath #这里 [source-dir] 是~/go/monitor
cd $GOPATH/src/procexporter
go mod init
go mod tidy
go get -u  // 如果不加这个的话go.mod里面就没有依赖的信息，build就会报错，好像是依赖没有下载下来，但是依赖已经在$GOPATH下面的pkg文件夹里了啊，没有，当时并没有下载
go build -o proc_exporter --ldflags '-w -s -linkmode external -extldflags "-static"' server/main.go
```
### 问题
- go mod tidy 
```
[root@iZuf68h0usx91bux03msu1Z procexporter]# go mod tidy                                                                                   │mod  sumdb
go: finding module for package gopkg.in/alecthomas/kingpin.v2                                                                              │[root@iZuf68h0usx91bux03msu1Z gopath]# ls pkg/mod/
go: finding module for package github.com/prometheus/client_golang/prometheus                                                              │cache  github.com  gopkg.in
go: finding module for package github.com/prometheus/client_golang/prometheus/promhttp                                                     │[root@iZuf68h0usx91bux03msu1Z gopath]# ls pkg/mod/github.com/
go: finding module for package github.com/go-kit/log                                                                                       │go-kit  prometheus
go: found github.com/go-kit/log in github.com/go-kit/log v0.2.1                                                                            │[root@iZuf68h0usx91bux03msu1Z gopath]# grep kingpin.v2 -r .
go: found github.com/prometheus/client_golang/prometheus in github.com/prometheus/client_golang v1.15.1                                    │./src/github.com/prometheus/quantdo_mysqld_exporter_patch/quantdo_seat.go:      "gopkg.in/alecthomas/kingpin.v2"
go: found github.com/prometheus/client_golang/prometheus/promhttp in github.com/prometheus/client_golang v1.15.1                           │./src/procexporter/quantdo_seat.go:     "gopkg.in/alecthomas/kingpin.v2"
go: found gopkg.in/alecthomas/kingpin.v2 in gopkg.in/alecthomas/kingpin.v2 v2.3.2                                                          │./src/go.sum:gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
go: procexporter imports                                                                                                                   │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/doc.go://     import "github.com/alecthomas/kingpin/v2"
        gopkg.in/alecthomas/kingpin.v2: gopkg.in/alecthomas/kingpin.v2@v2.3.2: parsing go.mod:                                             │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/go.mod:module github.com/alecthomas/kingpin/v2
        module declares its path as: github.com/alecthomas/kingpin/v2                                                                      │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/README.md:    $ go get github.com/alecthomas/kingpin/v2
                but was required as: gopkg.in/alecthomas/kingpin.v2
# 解决这个module declares its path as xxx, but was required as:xxxx https://blog.csdn.net/liuqun0319/article/details/104054313
vim go mod 
# 添加
replace github.com/alecthomas/kingpin/v2 => gopkg.in/alecthomas/kingpin.v2 v2.3.2 // indirect
replace gopkg.in/alecthomas/kingpin.v2 => github.com/alecthomas/kingpin/v2 v2.3.2 // indirect
```
- found packages procexporter (cgroup.go) and collector (quantdo_seat.go) in /root/j_go/monitor/gopath/src/procexporter
原因是在同一个folder存在多个package, 则加载失败. 即使是main, 也一样

- used for two different module paths 
```
// 解决办法https://blog.csdn.net/oscarun/article/details/105321846
go mod edit -replace=github.com/alecthomas/kingpin/v2@v2.3.2=gopkg.in/alecthomas/kingpin.v2@v2.3.2 //这时go.mod里会增加一行然后再手动增加一行,结果是下面这样子
replace (
        github.com/alecthomas/kingpin/v2 v2.3.2 => gopkg.in/alecthomas/kingpin.v2 v2.3.2 
        gopkg.in/alecthomas/kingpin.v2 v2.3.2 => github.com/alecthomas/kingpin/v2 v2.3.2
)


// 正确的回显
[root@iZuf68h0usx91bux03msu1Z mysqld_exporter]# go get github.com/prometheus/mysqld_exporter                                                
go: added gopkg.in/alecthomas/kingpin.v2 v2.3.2 
```

# 错误和异常处理
### panic 
- 假如函数F中书写了panic语句，会终止其后要执行的代码

# channel 
- link：
    - channel基础：https://www.topgoer.com/%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B/channel.html
    - 深入理解channel：https://juejin.cn/post/7175028144812851237#heading-0
- （注意：文中的 chan 表示是 go 语言里面的 chan 关键字，而 channel 只是我们描述它的时候用的一个术语）
- channel是用来解决什么问题的
go 里面，在实际程序运行的过程中，往往会有很多协程在执行，通过启动多个协程的方式，我们可以更高效地利用系统资源。
而不同协程之间往往需要进行通信（否则就有可能会出现数据冲突的情况），不同于以往多线程程序的那种通信方式，在 go 里面是通过 channel （也就是 chan 类型）来进行通信的，
实现的方式简单来说就是，一个协程往 channel 里面写数据，然后其他的协程可以从 channel 中将其读取出来。

- 通道操作符
`<-` 运算符被称为通道操作符，其作用是将数据发送到通道（channel）中或从通道中接收数据。
    - 定义时
    channel是一种类型，一种引用类型。声明通道类型的格式如下`var 变量 chan 元素类型`
    `func squarer(out chan<- int, in <-chan int) {`
    chan<- type是一个只能发送的通道，可以发送但是不能接收；
    <-chan type是一个只能接收的通道，可以接收但是不能发送。

    - 使用时
    当 `<-` 用于左侧时，表示将数据发送到通道中。例如，`ch <- 5` 表示将整数 5 发送到名为 ch 的通道中。
    当 `<-` 用于右侧时，表示从通道中接收数据。例如，`x := <- ch` 表示从名为 ch 的通道中接收一个值，并将其赋值给变量 x 。 
    此外，`<-` 运算符还可以与 `select` 语句一起使用，以实现从多个通道中接收数据或向多个通道中发送数据等操作。

- 队列
但在实际中，读 chan 和写 chan 的协程都有一个队列来保存。 我们需要明确的一点事实是：队列中的协程会一个接一个执行，队列头的协程先执行，然后我们对 chan 的读写是按顺序来读写的，先取 chan 队列头的元素，然后下一个元素。

# 变量
- link
    - https://www.topgoer.com/go%E5%9F%BA%E7%A1%80/%E5%8F%98%E9%87%8F%E5%92%8C%E5%B8%B8%E9%87%8F.html?h=%3A%3D
- `:=` 快速声明变量，只能用在函数内部
- 要使用var关键字声明 `var var_name var_type = var_value`
- 全局变量就是导出变量，定义的方式是首字母大写，另外在被导出的的结构体或者接口中，只有首字母大写的字段和方法才能被包外访问，而结构体中首字母小写的字段和方法不能被包外访问

# defer
- 先定义的后执行，因为执行了就销毁了，如果先前面的资源先释放了，后面的语句就没法执行了。
# 函数
- link：
    - https://www.topgoer.com/%E5%87%BD%E6%95%B0/%E5%87%BD%E6%95%B0%E5%AE%9A%E4%B9%89.html
- 函数的定义格式
``` go
func function_name( [parameter list] ) [return_types] {
   函数体
}
// 当两个或多个连续的函数命名参数是同一类型，则除了最后一个类型之外，其他都可以省略
// 左大括号依旧不能另起一行, 要和func关键字放在同一行
// pg
func test(x, y int, s string) (int, string) {
    // 类型相同的相邻参数，参数类型可合并。 多返回值必须用括号。
    n := x + y          
    return n, fmt.Sprintf(s, n)
}
// 可能会偶尔遇到没有函数体的函数声明，这表示该函数不是以Go实现的。这样的声明定义了函数标识符。
func Sin(x float64) float //implemented in assembly language
```
# 结构体
### 定义和初始化语句
```go
// 定义
type struct_variable_type struct {
   member definition
   member definition
   ...
   member definition
}
// 初始化
variable_name := structure_variable_type {value1, value2...valuen}
// 或
variable_name := structure_variable_type { key1: value1, key2: value2..., keyn: valuen}
// 或
var Book2 Books        /* 声明 Book2 为 Books 类型 */
Book1.title = "Go 语言"

// s使用
fmt.Printf( "Book title : %s\n", book.title)

```
- 匿名结构体定义`var user struct{Name string; Age int}`
- 还可以给结构体定义方法
```go
type Person struct {
	Name  string
	Age   uint8
	Money int
}

func (person *Person) GetName() string {
	return person.Name
}

func (person *Person) AddIncome(money int) int {
	person.Money += money
	return person.Money
}
// 使用
name := person.GetName() // 获取该Person变量的Name字段的值
```
# 数组
- link：https://www.runoob.com/go/go-passing-arrays-to-functions.html
- 是同一种数据类型的固定长度的序列。一旦定义，长度不能变。以往认知的数组有很大不同。
- 数组是值类型，赋值和传参会复制整个数组，而不是指针。因此改变副本的值，不会改变本身的值。
- 声明方式：
```
var variable_name [SIZE] variable_type
# 可以把长度和类型写在等号右边
var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
# 可以使用 ... 代替数组的长度，编译器会根据元素个数自行推断数组的长度 var b = [...]string{"hi"}
# 也可以不写 var b = []string{"hi"}
# 如果设置了数组的长度，我们还可以通过指定下标来初始化元素
//  将索引为 1 和 3 的元素初始化
balance := [5]float32{1:2.0,3:7.0}
```
# range
- link：https://www.runoob.com/go/go-range.html
- range 关键字用于 for 循环中迭代数组(array)、切片(slice)、通道(channel)或集合(map)的元素。在数组和切片中它返回元素的索引和索引对应的值，在集合中返回 key-value 对。
- 可以省略key或者value
    - 果只想读取 key，格式如下：`for key := range oldMap`
    - 读取value `for _, value := range oldMap`

# 指针
- link：http://c.biancheng.net/view/21.html
### 认识指针地址和指针类型
- 指针（pointer）在Go语言中可以被拆分为两个核心概念：
    - 类型指针，允许对这个指针类型的数据进行修改，传递数据可以直接使用指针，而无须拷贝数据，类型指针不能进行偏移和运算。
    - 切片，由指向起始元素的原始指针、元素数量和容量组成。而且指针还可以作为函数参数和返回值。
- 指针变量通常缩写为 `ptr`
- 和C语言一样，go中的指针无论什么类型占用的内存都是一样的，32位系统占用4个字节，64位的系统占用8个字节
- 每个变量在运行时都拥有一个地址，这个地址代表变量在内存中的位置。Go语言中使用在变量名前面添加&操作符（前缀）来获取变量的内存地址（取地址操作），格式如下：`ptr := &v    // v 的类型为 T(代号)`
    - 其中 v 代表被取地址的变量，变量 v 的地址使用变量 ptr 进行接收，ptr 的类型为*T，称做 T 的指针类型，*代表指针。
- 变量、指针和地址三者的关系是，每个变量都拥有地址，指针的值就是地址。
### 使用指针获取指针指向的值 普通指针
- 使用`&`取地址操作符对普通变量进行取地址操作可以得到变量的指针；对指针使用`*`取值操作符
```go
func main() {
    // 准备一个字符串类型
    var house = "Malibu Point 10880, 90265"
    // 对字符串取地址, ptr类型为*string
    ptr := &house  # 未定义直接使用
    // 打印ptr的类型
    fmt.Printf("ptr type: %T\n", ptr)  # ptr type: *string
    // 打印ptr的指针地址 
    fmt.Printf("address: %p\n", ptr)  # address: 0xc0420401b0
    // 对指针进行取值操作
    value := *ptr
    // 取值后的类型
    fmt.Printf("value type: %T\n", value)  # value type: string
    // 指针取值后就是指向变量的值
    fmt.Printf("value: %s\n", value)
}
```
- 取地址操作符`&`和取值操作符`*`是一对互补操作符，`&`取出地址，`*`根据地址取出地址指向的值。
- 变量、指针地址、指针变量、取地址、取值的相互关系和特性如下：
    - 对变量进行取地址操作使用`&`操作符，可以获得这个变量的指针变量。
    - 指针变量的值是指针地址。
    - 对指针变量进行取值操作使用*操作符，可以获得指针变量指向的原变量的值。
```go
// *int是类型
// *pointer_name是指针变量，相当于指针指向的变量 如:
var p *int = &var_name
// *p=3 就相当于 var_name=3
```
### 结构体指针
- link：https://zhuanlan.zhihu.com/p/615424412
- 声明：`var ptr *StructName`
- 赋值`var ptr *Person = &person`
- 使用`name := (*ptr).Name` 或者更简单的语法`name := ptr.Name` ; 由于.运算符优先级比`*`高, 所以一定要加上(*)来包住

# 第三方库
- 安装 `go get github.com/jmoiron/sqlx` 在任何目录下都行吧
- 使用
```go
import (
	"context"
	"database/sql"
	"fmt"
	"time"

	"github.com/go-kit/log"
	"github.com/prometheus/client_golang/prometheus"
)

```
## other
- 照葫芦画瓢
- 指针也是一种类型，和int一样，定义int是用`var v_name int = 3` 3是int类型；定义指针就是`var ptr *int = $var_names` *int就是类型 $var_names就是值

# 格式化字符串
- 输出变量类型 `fmt.Printf("%T\n", p)    // *int`
- 输出地址`fmt.Printf("%p\n", &num) // 0xc0000ae008` 但参数需要是地址