# 前言
- 一些配置项
    - 通过命令行运行`go env` 来查看
    - GOARCH 表示目标处理器架构。
    - GOBIN 表示编译器和链接器的安装位置。（为空也是正常的）
    - GOPATH 表示当前工作目录。
    - GOROOT 表示 Go 开发包的安装目录。
- GOPATH 是一个什么概念的
    - link：http://c.biancheng.net/view/88.html
    - 应该是自己写的代码的位置，不是go的安装位置
    - 在 GOPATH 指定的工作目录下，代码总是会保存在 $GOPATH/src 目录下。在工程经过 go build、go install 或 go get 等指令后，会将产生的二进制可执行文件放在 $GOPATH/bin 目录下，生成的中间缓存文件会被保存在 $GOPATH/pkg 下。
    - 如果需要将整个源码添加到版本管理工具（Version Control System，VCS）中时，只需要添加 $GOPATH/src 目录的源码即可。bin 和 pkg 目录的内容都可以由 src 目录生成。
    ```go 
    // 设置当前目录为GOPATH /home/davy/go
    // 建立GOPATH中的源码目录 mkdir -p src/hello
    // 在hello下添加main.go源码文件
    // Go语言中可以通过 GOPATH 找到工程的位置。所以可以直接执行命令编译源码
    go install hello // 编译完成的可执行文件会保存在 $GOPATH/bin 目录下。
    // 在go init 后的目录下也可以，这些目录是moudle
    PS C:\Users\Quantdo\Desktop\people\quantdo\monitor\monitor\gopath\src> go install quantdo22
    package quantdo22 is not in GOROOT (D:\software\Go120\src\quantdo22)
    // 如果不是module会提示
    PS C:\Users\Quantdo\Desktop\people\quantdo\monitor> go install quant
    go: 'go install' requires a version when current directory is not in a module
        Try 'go install quant@latest' to install the latest version
    ```

# windows
- download: https://go.dev/dl/
- 选择kind为Installer的后缀名为msi的文件进行下载；有1.20.x和1.19.x的版本，我下的1.20的
- 设置go的安装文件夹，然后点击next直到完成
- 设置用户变量GOPATH：刚刚的文件夹
## vscode配置go工具包
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
## 第一个程序
- 直接F5报错，按照提示给的文件夹下运行git mod init redom_name 
## launch.json 使用自动生成的 位置和当前的不在一块也没有关系
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
## go module 模式
- link：https://zhuanlan.zhihu.com/p/105556877
Go Modules是语义化版本管理的依赖项的包管理工具

## tmp
- 用户变量 GOPATH：%USERPROFILE%\go path：%USERPROFILE%\go\bin---
# 问题
- ambiguous import 提示有两个go，把除了%GOPATH%之外的给删除了