# TO：部署GO，和go的hello_world
###  一些配置项
- 通过命令行运行`go env` 来查看
- GOARCH 表示目标处理器架构。
- GOBIN 表示编译器和链接器的安装位置。（为空也是正常的）
- GOPATH 表示当前工作目录。
- GOROOT 表示 Go 开发包的安装目录(是go的安装目录)。

### hello_world
```cs
mkdir hello
cd hello 
go mod init hello 

// touch main.go
package main // 

import "fmt"

func main(){
    fmt.Println("hello")
    main2()
}
func main2(){
    fmt.Println("hello")
}
// go build main.go 会生成main.exe 在main.go的同级目录下使用./main.exe 执行
// go install main.go 不管是否执行go mod init 都会在$GoPath/bin下找到main.exe 使用./path/to/main.exe执行
```

### windows安装
- download: https://go.dev/dl/
- 选择kind为Installer的后缀名为msi的文件进行下载；有1.20.x和1.19.x的版本，我下的1.20的
- 设置go的安装文件夹(E:\software\GO)，然后点击next直到完成 （Go 开发包在安装完成后，将 GOPATH 赋予了一个默认的目录%USERPROFILE%/go）
- 设置用户变量GOPATH：刚刚的文件夹(E:\software\GO), 然后将(E:\software\GO\bin)放入用户变量的Path和系统变量的Path中
- go version有关于go版本的输出


### go option
- link：https://c.biancheng.net/view/123.html

- go build 用于编译但不安装 Go 程序，而 go install 用于编译并安装 Go 程序，使其可以在终端中直接运行。

- install 编译，编译完成的可执行文件会保存在 $GOPATH/bin 目录下。
```cs
// 在go init 后的目录下也可以，这些目录是moudle
PS C:\Users\Quantdo\Desktop\people\quantdo\monitor\monitor\gopath\src> go install quantdo22
package quantdo22 is not in GOROOT (D:\software\Go120\src\quantdo22)
// 如果不是module会提示
PS C:\Users\Quantdo\Desktop\people\quantdo\monitor> go install quant
go: 'go install' requires a version when current directory is not in a module
    Try 'go install quant@latest' to install the latest version
// go build ./main.go go install ./main.go go build main.go go install main.go
// go build ./hello go build hello
// go install ./hello 
// go install hello hello如果不是在$GoPath/src下，会报错
```

### vscode配置go工具包
- 设置代理：`go env -w GO111MODULE=on`;`go env -w GOPROXY=https://goproxy.cn,direct`
- Ctrl+Shift+P 然后输入`Go:Install/Update Tools`然后选中安装
- 安装dlv报错，说架构不支持，
    - 方法一没有用解决https://github.com/derekparker/delve/blob/master/Documentation/installation/windows/install.md
    - 方法二：https://blog.csdn.net/tongyi04/article/details/127980476
        - `go env -w GOARCH=amd64`
        - dlv会安装在D:\software\Go120\bin\windows_amd64；需要把这个windows_amd64也放到path当中
    - 安装后cmd输入dlv有反应说明安装成功
    - 方法三：手动安装：https://www.jianshu.com/p/2802d71ab9e9
        - 进入go安装目录的src下git clone git@github.com:derekparker/delve.git


### launch.json 使用自动生成的 位置和当前的不在一块也没有关系
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "${fileDirname}",
            // "program": "${workspaceFolder}",
            
        }
    ]
}
```

# 问题
- ambiguous import 提示有两个go，把除了%GOPATH%之外的给删除了
- 直接F5报错，在提示信息中的文件夹下运行git mod init redom_name 