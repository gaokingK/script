# doc
- 经典教材中文翻译：https://golang-china.github.io/gopl-zh/preface.html
- 文档（比较全）https://learnku.com/docs/the-way-to-go/the-basic-structure-and-elements-of-the-go-program/3583
- 文档2（不全）：https://learnku.com/go/wikis/38122

# some
- go虽然是把代码写在了一个一个的程序文件当中，但当程序运行的时候，是通过main函数运行的，会运行所有的文件
# GO语言的特点
- 没有隐式的数据转换、没有构造函数和析构函数、没有运算符重载、没有默认参数、没有继承、没有泛型、没有异常、没有宏、没有函数修饰、没有线程局部存储
- 诺保证向后兼容：用之前的Go语言编写程序可以用新版本的Go语言编译器和标准库直接构建而不需要修改代码。
- Go语言的面向对象机制与一般语言不同。它没有类层次结构，甚至可以说没有类；仅仅通过组合（而不是继承）简单的对象来构建复杂的对象。方法不仅可以定义在结构体上，而且，可以定义在任何用户自定义的类型上；并且，具体类型和抽象类型（接口）之间的关系是隐式的，所以很多类型的设计者可能并不知道该类型到底实现了哪些接口


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

# go get 是获取、编译、安装项目
- 安装到$GOPATH/bin下

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



# 运算符
- 不同类型的值之间比较会报错
- 在 Go 语言中，&& 和 || 是具有快捷性质的运算符，当运算符左边表达式的值已经能够决定整个表达式的值的时候（&& 左边的值为 false，|| 左边的值为 true），运算符右边的表达式将不会被执行。利用这个性质，如果你有多个条件判断，应当将计算过程较为复杂的表达式放在运算符的右侧以减少不必要的运算。
- 取余运算符只能作用于整数：9 % 4 -> 1。
- 同时，带有 ++ 和 -- 的只能作为语句，而非表达式，因此 n = i++ 这种写法是无效的
  

# defer
- 在return 返回前执行
- 如果有多个defer 先定义的后执行（按照栈的顺序），因为执行了就销毁了，如果先前面的资源先释放了，后面的语句就没法执行了。
- defer un(trace("b")) 运行到这里的话会先执行trace("b")
  
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
### Go 语言规范定义了接口方法集的调用规则：

- 类型 *T 的可调用方法集包含接受者为 *T 或 T 的所有方法集
- 类型 T 的可调用方法集包含接受者为 T 的所有方法
- 类型 T 的可调用方法集不包含接受者为 *T 的方法

### range  # 返回索引和内容
```
for _, val := range sl
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
variable_name := structure_variable_type { key1: value1, keyn: valuen}
// 或
var Book2 Books        /* 声明 Book2 为 Books 类型 */
Book1.title = "Go 语言"
ms = struct1{10, 15.5, "Chris"}
// 或
book2:=new(Books)
book2.value1=xxx
//或
ms := &struct1{10, 15.5, "Chris"}
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


# range
- link：https://www.runoob.com/go/go-range.html
- range 关键字用于 for 循环中迭代数组(array)、切片(slice)、通道(channel)或集合(map)的元素。在数组和切片中它返回元素的索引和索引对应的值，在集合中返回 key-value 对。
- 可以省略key或者value
    - 果只想读取 key，格式如下：`for key := range oldMap`
    - 读取value `for _, value := range oldMap`
- 如果只有一个接收者，会只返回索引
```go
a := [...]string{"a", "b", "c", "d"}
for i := range a {
    fmt.Println("Array item", i, "is", a[i])
}
```

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
- 在指针类型前面加上 * 号（前缀）来获取指针所指向的内容，这里的 * 号是一个类型更改器
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

# 输出 # prin
- Print 只能输出字符串
- Printf 可以将数字、变量、字符串格式化到第一个格式化字符串后输出
- Println 和print一样，只不过后面会输出一个换行符

## 格式化字符串
- https://blog.csdn.net/TomorrowAndTuture/article/details/133680818
- 输出变量类型 `fmt.Printf("%T\n", p)    // *int`
- 输出地址`fmt.Printf("%p\n", &num) // 0xc0000ae008` 但参数需要是地址
- 格式化输出时，你可以使用 %t 来表示你要输出的值为布尔型
- %d 十进制表示 
  - %2d 长度为2，不足2位以空格填充,超过2位的就以实际长度显示
- %T     相应值的类型的Go语法表示
- %v	值的默认格式表示
- %s     字符串或切片的无解译字节