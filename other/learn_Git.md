### git
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