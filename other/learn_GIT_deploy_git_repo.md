### 搭建git repo
- [基于已有仓库搭建，但不能直接看代码](https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E5%9C%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E6%90%AD%E5%BB%BA-Git)
- [新创建一个git](https://www.liaoxuefeng.com/wiki/896043488029600/899998870925664)
#### 选择方法2
1. `git init --bare reponame.git` 创建一个不带工作区的裸仓库,避免直接在仓库中改代码
2. 修改owner符合通用 `chown -R git:git reponame.git`
3. 在其他服务器上clone `git clone git@/file/to/reponame.git`
4. 配置免密方便使用 `ssh-copy-id -i ~/.ssh/id_rsa.pub git@ip`
让每个需要写权限的人发送一个 SSH 公钥， 然后将其加入 git 账户的 ~/.ssh/authorized_keys 文件

#### 建立一个直接能看代码的仓库
- link：https://www.cnblogs.com/irockcode/p/8761954.html
- 使用--bare 创建的仓库不能自己看代码
```
# 远端
git init
# 本地
git clone xxx
git checkout -b merge_use
一些修改
git push --set-upstream origin merge_use # 将本地的修改整到远端
# 远端
git merge merge_use # 在master上操作

# 让远端呆在master、让本地呆在merge_use；本地的改动push到远端、然后远端在git merge merge_use
# 但是这样会出现一个问题，就是pull的时候老是会出现merge，明明远端也没有改动 使用git pull origin merge_use也是这样
```
#### FWQ
- bare 选项
`--bare` 纯净的 
`git init --bare`搞出来的git 目录不带工作区,只有版本库(HEAD/hooks这些),想看里面的内容必须git clone 出来
`git init` 带工作区
基于本地仓库初始化远程仓库是最好选择--bare, 因为git init 会让远程仓库也包括分支的work tree, 那么当push 本地新的改变的时候, 远程仓库不会显示push的内容, 远程仓库对应的目录下还是之前的内容,必须通过git reset --hard 回退到此时的HEAD 才能看到push后的内容
f