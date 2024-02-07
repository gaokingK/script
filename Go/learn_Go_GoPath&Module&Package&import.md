# TO: GoPath、Module、GO111MODULE、package、import和展示项目结构
### GOPATH 是干什么的
- 在早期版本中GoPath负责项目代码的管理和依赖包的管理，自1.16开始，GoPath只负责项目代码的管理，依赖包的管理由Go Module负责
- link：http://c.biancheng.net/view/88.html
- 是自己写的代码的位置，不是go的安装位置
- 在 GOPATH 指定的工作目录下，代码总是会保存在 $GOPATH/src 目录下。在工程经过 go build、go install 或 go get 等指令后，会将产生的二进制可执行文件放在 $GOPATH/bin 目录下，生成的中间缓存文件会被保存在 $GOPATH/pkg 下。
- 如果需要将整个源码添加到版本管理工具（Version Control System，VCS）中时，只需要添加 $GOPATH/src 目录的源码即可。bin 和 pkg 目录的内容都可以由 src 目录生成。
```cs
// 设置当前目录为GOPATH /home/davy/go 
export GOPATH=`pwd`
// 建立GOPATH中的源码目录 
mkdir -p src/hello
// 在hello下添加main.go源码文件
// Go语言中可以通过 GOPATH 找到工程的位置。所以可以直接执行命令编译源码
go install ./hello // 编译完成的可执行文件会保存在 $GOPATH/bin 目录下。(链接里是go install hello 会报错package hello is not in std (/usr/local/go/src/hello))
```
### Go Module
- link
    - https://juejin.cn/post/6869570760738865166#heading-10
    - https://www.jianshu.com/p/2d4d0bd7d2e4
    - 一些问题：https://blog.csdn.net/qq_39852676/article/details/121132613
- 一个Module就是package(go 包)的集合. 即: 一个Module含有多个package; 一个package含有多个.go文件.
- Go Modules不是module，Go Modules是 Go 语言中的一种包管理机制，
    - 它通过go.mod可以帮助开发者有效地管理项目的依赖库和版本，提高开发效率
    - 除了go.mod之外，go命令还维护一个名为go.sum的文件，其中包含特定模块版本内容的预期加密哈希 go命令使用go.sum文件确保这些模块的未来下载检索与第一次下载相同的位，以确保项目所依赖的模块不会出现意外更改，无论是出于恶意、意外还是其他原因。 go.mod和go.sum都应检入版本控制
    - go.sum 不需要手工维护，所以可以不用太关注。
    - 子目录里是不需要init的，所有的子目录里的依赖都会组织在根目录的go.mod文件里
- Modules是相关Go包的集合，是源代码交换和版本控制的**单元**。go命令直接支持使用Modules，包括记录和解析对其他模块的依赖性。Modules替换旧的基于GOPATH的方法，来指定使用哪些源文件。
- 发展历史
    - Go modules 是 Go 语言的依赖解决方案，发布于 Go1.11，成长于 Go1.12，丰富于 Go1.13，正式于 Go1.14 推荐在生产上使用。
    - Go moudles 目前集成在 Go 的工具链中，只要安装了 Go，自然而然也就可以使用 Go moudles 了，而 Go modules 的出现也解决了在 Go1.11 前的几个常见争议问题：
        - Go 语言长久以来的依赖管理问题。
        - GoPath包管理模式的重复
        - 统一社区中的其它的依赖管理工具（提供迁移功能）。
```go
// go mod init myservice
// 其中的 myservice 表示所定义的模块名称，模块名称也可以是一个路径，比如 world/youwu.today。这个名称将决定了后续包引用时的前缀
// 如果要发布这个模块，最好把模块名换为git仓库的地址如github.com/hello
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

### GO111MODULE
- 设置是否使用go module版本管理工具的开关.
- auto  默认值，go命令会根据当前目录来决定是否启用modules功能。需要满足两种情形：
    - 该目录不在GOPATH/src/下
    - 当前或上一层目录存在go.mod文件

### 使用Go Module替代GoPath管理包的好处
- link： https://juejin.cn/post/6964577426290507789?searchId=20231107103817A4C31F8EF3A3816B258C
- 结论1.11以后的版本，GoPath只有一个（是Go的安装目录，src的上层目录），GoModule有多个（哪里执行go mod init就会把这个文件夹当成一个新的GoModule)
- 在GoPath时代
    - 代码必须在GoPath中才能运行
    - 运行go get <package> 时，GoPath 会把包下到 GOPATH/src 路径上安装第三方包
- 那么当由多个项目时，就会有两种选择
    - 每个项目用自己的GoPath, 这样的好处是每个项目的依赖都分开了，坏处是如果项目用到的依赖都会重新下载一遍，第二是GoPath/src下会有你自己的代码和依赖的（`go get <package> `）代码.
    - 不同的项目共用一个GoPath，这样虽然能解决多项目的相同依赖重复下载的问题，但是多个项目的代码会混杂到一块、更别提还有依赖包的代码。还不如第一种呢
- 从1.11版本起，Go引入了GoModule来解决这个问题。就是再GoPath外再弄一个GoModule目录（就是执行go mod init的目录），这样每个项目自己的代码就安装在自己的GoModule目录，第三方的则都安装在GoPath里。 每个项目对第三方包的依赖由自己GoModule下的go.mod维护
- 补充：https://youwu.today/skill/backend/using-go-modules/
    - 如果你在互联网上查找 go 语言的 helloworld 示例程序时，还看到别人的例子，让你如何配置 GOPATH 的话，基本可以说明那篇文章大概率是比较老的。
    - go 程序的代码工程是需要 GOPATH 环境变量，并且要按照如下的目录结构来组织：
    ```cs
    path of $GOPATH:
    ├─bin
    ├─pkg
    ├─src
    │  └─helloworld
    │      └─helloworld.go
    ```
    - 当有了 go modules 之后，你的目录可以这么组织:
    ```cs
    path of everywhere:
    ├─go.mod
    └─helloworld.go
    ```

### package
- link:
    - https://juejin.cn/post/6869570760738865166
- go使用包来组织源代码的，并实现命名空间的管理，任何一个Go语言程序必须属于且只属于一个包，即每个go程序的开头要写上`package <pkg_name>`
- Go语言包一般要满足如下三个条件：
1. 同一个目录下的同级(不包括子目录)的所有go文件应该属于一个包（子文件夹是另一个包）；
2. 包的名称可以跟目录不同名，不过建议同名，包的名称使用小写字母；
3. 一个Go语言程序有且只有一个main函数(多个文件中只能有一个main函数)，他是Go语言程序的入口函数，且必须属于main包，没有或者多于一个进行Go语言程序编译时都会报错；
- 包的入口文件是根据里面含有main函数决定的，那个文件含有入口函数main，那个就是；根据是否含有main函数，分为可执行包和不可执行包

### import
- 导入的方式是当前文件的相对目录
- 导入的包必须要使用，否则也会报错。
- 如果一个包要引用另一个包的标识符(比如结构体、变量、常量、函数等)，那么首先必须要将其导出，导出的具体做法就是在定义这些标识符的时候保证首字母大写(首字母小写的标识符只能限制在包内引用)。另外在被导出的的结构体或者接口中，只有首字母大写的字段和方法才能被包外访问，而结构体中首字母小写的字段和方法不能被包外访问
- 设置别名 `设置别名引用 import format_go fmt` 别名在前
- import引入的都是包所在的目录名, 只不过因为有条包名要和所在目录同名的这条规范, 所以会给人一种我是导入的包的错觉
- `import _ "crypto/rand" `只执行init函数
- `import path` 指的是import后面跟的路径即`import <import path>`
- import 需要依赖package的源码包。如果是标准库包: 源码在$GOROOT/src下；如果是第三方依赖包: 源码在$GOPATH/src下

### 项目结构和怎么导入的
- 同一个module的同一目录下只能有一个含有main函数的文件，否则go build 的时候会报错，在嵌套的包里面的没事
- 注意如果要包方法在其他包中可以调用，包方法需要首字母大写，例如：fmt.Println() fmt.Printf()。
- 别名 import  myBaz "foo/bar/baz" myBaz就是别名
- . 导入可以让包内的方法注册到当前包的上下文中，直接调用方法名即可，不需要再加包前缀。
- 小写开头的变量名是私有的，别的包不能访问，大写开头的变量别的可以使用
```cs
import . "foo/bar/baz" 
fmt.Println(Hello(), World()) // 直接使用包内的方法即可 不需要显式使用包名
```
- _ 是包引用操作，只会执行包下各模块中的 init 方法，并不会真正的导入包，所以不可以调用包内的其他方法
```go
import   _ "foo/bar/baz"

fmt.Println(baz.Hello(), baz.World()) // 错误 _ 并没有导入包 只是引入并执行包模块的 init  方法
```