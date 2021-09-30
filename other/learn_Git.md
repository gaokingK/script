### git
##### 1. 为什么切换分支后 把改动在另一个分支上提交后这个分支上就看不到改动了?
##### 1. .gitignore 失效
    在.gitignore 中定义的文件还会出现在git status中
    新建的文件在git中会有缓存，如果某些文件已经被纳入了版本管理中，就算是在.gitignore中已经声明了忽略路径也是不起作用的，这时候我们就应该先把本地缓存删除，然后再进行git的push，这样就不会出现忽略的文件了。git清除本地缓存命令如下：
    ```
    # 先进入根目录中
    git rm -r --cached .
    git add .
    git commit -m 'update .gitignore'
    ```
##### 1. git add -e 好像是用来编辑改变的，就还是编辑删除了什么内容，添加的什么内容的那个显示
##### 1. 忽略git 文件 .gitignore 会上传到库变成公共的
    `git update-index --assume-unchanged /path/to/file`
    `git update-index --no-assume-unchanged /path/to/file`
    or 
    https://blog.csdn.net/chenshufeng115/article/details/95452914?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.nonecase

## 了解远程仓库
    查看远程仓库的提交历史来看开发进度，也能判断出那个是主分支
    > isourceb中从主仓activity中看 codehub中从动态中看
## 更新 fork 库的代码

在iSource上有个功能叫fork，可以将别人的项目复制到自己账号下。这个功能很方便，但其有一个缺点是：当主库（源项目）更新后，fork库并不会一起更新，需要自己手动去更新。

**方法：**通过线下更新fork库的代码（可以使用Git bash、TortoiseGit两种工具）