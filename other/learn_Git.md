# git
## 问题
- git stash 会把所有的改动都存起来，文件就没有改动了，但是如果此时再次改动b， 然后stash pop， 改动b仍然存在。
- git stash 后各分支都有一样的stash栈
   - git satsh apply stash_name
- git stash error: 权限不足，无法在仓库对象库 .git/objects 中添加对象 不能记录工作区状态
   - 等一会重试就可以了（不知道为啥， 可能是别的编辑器正在占用？）
- error: 权限不足，无法在仓库对象库 .git/objects 中添加对象 fatal: git-write-tree: error building trees 无法保存当前索引状态
  - insufficient permission for adding an object to repository database
  - 原因： 服务端上把repo的owner改了，再改回来
  - link：https://my.oschina.net/u/4437884/blog/4416200
- 如何搜索历史记录， 想搜索字段， 但这些字段不知道在那个版本中被删除了
  - link：https://blog.csdn.net/asdfgh0077/article/details/103453994
  - git log -G/-S|grep <pattern>
  - pycharm 里点击历史 上面的是被修改的commit id 下面的是修改后的
- fatal: unable to access https://github.com/xxxx.git/: server certificate verification failed. CAfile: none CRLfile: none 或者是 x509
  - x509很熟悉，是SSL传输的证书标准，应该是ssl认证失败，执行如下命令禁用SSL认证：
  - `git config --global http.sslverify false`
- gnutls_handshake() failed: the tls connection was non-properly terminated
  - 设置代理，在终端中设置
- git-lfs filter-process failed 
   - link: 
      - lfs介绍：https://iguoli.github.io/2019/07/10/Git-LFS.html
         - Git LFS 是由 Atlassian, GitHub 和其他开源贡献者开发的 Git 扩展，目的是减少大文件对 Git 仓库的影响，其以一种偷懒的方式下载相关版本的文件
      - 解决：https://stackoverflow.com/questions/43989902/git-pull-smudge-filter-lfs-failed
   - 问题原因 git lfs 拉取时不知道lfs的url？
      - in my case the SSH-authenticated repository was updated to use LFS from another client and on my side Git-LFS didn't know about the SSH remote-url
   - 解决办法：
      - git config lfs.url $(git config remote.origin.url)
      - git lfs pull
- EOF
   - link：https://github.com/git-lfs/git-lfs/issues/3519
   - 出现EOF原因意味着在拉取过程中客户端和服务器出现了问题
## 帮助
- https://docs.gitlab.com/ee/topics/git/stash.html
## other

### git stash
- link:
   - https://www.cnblogs.com/zndxall/p/9586088.html
- git stash –keep-index。只会备份那些没有被add的文件。
### GIT_TRACE显示日志
   - link：https://blog.csdn.net/icyfox_bupt/article/details/91627314
### git patch --------------------------------no
### 删除未跟踪
   - link: https://blog.csdn.net/uhippo/article/details/46365737
   - git clean -nf 看那些会被删除
### 远程分支回滚的三种方法：
   link :https://www.cnblogs.com/Super-scarlett/p/8183348.html
   自己的分支回滚直接用reset
   公共分支回滚用revert
   错的太远了直接将代码全部删掉，用正确代码替代
### git reset
   ```
   # commit id A
   This is test
   # 修改为：
   This is test2
   # commit
   # 修改为 This is test3
   # reset --soft A 文件内容会变为如下，不会冲突
   # This is test3 # 然后本行有改动的颜色标识，就像直接修改一样
   ```
### 冲突
   - 什么情况下会有冲突
      - user a 修改file_a 10行, commit and push, user b 已另一种内容修改file_a 10行, commit and push, 会发现push 被拒绝, 然后push -f, 这时usera 再pull 就需要merge 这种情况的解决办法:
         - 可以user b reset --hard 然后 pull push
         - user a add . /commit 这时log 会不对(其实也是对的), reset hard 到 双方都提交之前的那个commit ,然后在pull ,这时库上是b的改动(想想也合理)
         - 
### 强制更新是什么意思
   ```
   huawei ~/Desktop/jjw% git pull
   remote: Counting objects: 7, done.
   remote: Compressing objects: 100% (3/3), done.
   remote: Total 4 (delta 3), reused 2 (delta 1)
   展开对象中: 100% (4/4), 完成.
   来自 90.90.0.140:/home/git/pc_kbox
 + 2961049(本地HEAD)...20f9d9a(origin master HEAD 可以show ta) master     -> origin/master  (强制更新)

   ```
### 配置
   - 全系统的(/etc/gitconfig)<当前用户的(~/.gitconfig)<当前仓库的(/.git/config)
   - 某个配置在当前仓库的中的配置中取消,但查看还在的原因是用的上层的配置
   - autocrlf 
   - git config --global 不加global只对当前仓库生效
   - git config -l 查看配置
### git checkout
   - `git checkout branch_name high_quality/dingding/function/.` 即使这个要检出的文件在现在的分支上不存在也可以检出的
### 这张图里怎么把code从repo checkout到workspace
      ![git fetch和git pull的概念](http://kmknkk.oss-cn-beijing.aliyuncs.com/image/git.jpg)
### [git fetch](https://www.cnblogs.com/runnerjack/p/9342362.html) -----------------------------no
### [git hook](https://www.git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-Git-%E9%92%A9%E5%AD%90)
   - 非0值是指程序异常退出
   - 为hook添加运行程序是chmod这样加
   - 程序需要 `#！/path/to/python3`
### git diff 忽略换行符格式/ 忽略所有的tab, white space, 换行符 
   - [link](https://blog.csdn.net/nanyilou_xiaoye/article/details/79075092) -------------------------no
   - [link](https://www.it1352.com/801295.html) ok
      - git diff --no-index --color --ignore-all-space< file1> < file2> # 忽略换行符
      - git diff --no-index --word-diff-regex=[^[:space:]] a.html b.html # 只看文字是否相同, 但这个没有用,不知为啥

### 查看分支的提交历史 git log --graph --pretty=oneline --abbrev-commit branch1 branch2
    ```
    * fad6d82 (HEAD -> back-master, origin/master, origin/HEAD, master) 根据冒烟用例适配
    * 8f8de25 根据日构建修改
    * f84aed0 新增虎扑app用例
    * 8a8a15b 修改kbox_run.py
    * 90011a7 日构建ini适配
    * 13cca5e 日构建适配
    * f464707 音频测试底层方法
    * b38b8e3 根据日构建修改网易云音乐、小红书用例
    * a3a11d9 生态用例修改
    * e2304c5 新增monkey文件
    * bac2f98 修改uos_app.ini,修改微信窗口事件用例，新增虎扑monkey测试用例
    | *   e16cb07 (origin/test_debug_floder, cherry-pick) Merge branch 'test_debug_floder' of 90.90.0.140:/home/git/pc_kbox into test_debug_floder 
    | |\  
    | | * e046c02 按照检视意见修改异常处理代码
    | * | 6f71848 适配钉钉/豆瓣/今日头条/金山词霸/美团open用例
    | * | 2d12e09 按照检视意见修改异常处理代码
    | |/  
    | * b7f5966 异常处理未检视代码
    | * e7bedfb 调试信息
    |/  
    *   e7d9c47 Merge branch 'master' of 90.90.0.140:/home/git/pc_kbox
    ```
### git log merge
```
commit dadfd7d8547cf5a34d73da27e54a00575800f667
Merge: aef79ca e19dd62 aef79ca 是本地的, e19dd62是远端的
Author: jjw <jjw@fuck.com>
Date:   Wed Sep 15 09:21:00 2021 +0800

    Merge branch 'master' of 90.90.0.140:/home/git/pc_kbox

commit aef79cab68a700bc720888746117117b2f6c1823
Author: jjw <jjw@fuck.com>
Date:   Wed Sep 15 09:20:45 2021 +0800

    修改抖音部分用例
```
### git mergetool -t opendiff --------------------------------------no
### 解决merge冲突
- git stash 存储本地修改，git pull origin master 
- 使用pycharm 解决冲突
   - 一共有三个格，you version 其实是服务器上pull下来的、result你操作后文件的真实结果，from server代表是你stash的 就是你本地的
### git cherry-pick 来将A分支的部分提交合并到B分支上
   - 如果需要多个commitid `git cherry-pick commitid_a commitid_b commitid_c` 只合并这三个
   - 先合并a, 如果有冲突就结局, 然后git cherry-pick --continue 完成后就把a给搞好了; 然后合并b,如果有冲突, 解决,然后git cherry-pick --continue....
### [把同一个分支里的提交放到其他的分支里](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md#rebasing-%E5%92%8C%E5%90%88%E5%B9%B6merging)
   - git log commitid1, commitid2, commit3
   - git reset --hard commit3
   - git checkout -b new_branch
   - git cherry-pick commid1 # 即使commitid 在git log中看不到了, 已经reset-hard了,仍然能找到这个commit
### git branch
   - [git branch 命令查看分支、删除远程分支、本地分支](https://blog.csdn.net/duxing_langzi/article/details/80295573)
   - 在新建分支上切换到master之前, 要留意你的工作目录和暂存区里那些还没有被提交的修改， 它可能会和你即将检出的分支产生冲突从而阻止 Git 切换到该分支。 最好的方法是，在你切换分支之前，保持好一个干净的状态。 有一些方法可以绕过这个问题（即，暂存（stashing） 和 修补提交（commit amending））
   - 当你切换分支的时候，Git 会重置你的工作目录，使其看起来像回到了你在那个分支上**最后一次提交**的样子
   - 将本地新建的分支同步到origin `git push --set-upstream origin merge2`
   - `git branch -vv `查看本地分支关联（跟踪）的远程分支之间的对应关系
   - `git branch -a `查看所有分支 remote/origin/master表示的是远程分支
   - `git push origin --delete Chapater6` 可以删除远程分支Chapater6 在删除远程分支时，同名的本地分支并不会被删除，所以还需要单独删除本地同名分支
      - 如果发生以下错误:
         error: unable to delete ‘origin/xxxxxxxx-fixbug’: remote ref does not exist
         error: failed to push some refs to ‘git@github.com:xxxxxxxx/xxxxxxxxxx.git’
         解决办法： git checkout xxxxx-fixbug 切换到当前分支上， 然后再 进行 git push --delete origin origin/xxxxx-fixbug
   - `git branch -d Chapater8 `可以删除本地分支（在主分支中）
   - `git fetch -p` 清理本地无效分支(远程已删除本地没删除的分支): 
#### 使用分支合并
   - git pull git_url
   - git checkout -b branch_name origin/branch_name # 远程已经新建了branch_name
   - git pull master # 在自己分支上
   - 只拉取远程分支 `git init; git remote add origin xxx.git; git fetch origin develop（develop为远程仓库的分支名）`
      - link: https://blog.csdn.net/carfge/article/details/79691360
#### 创建远程分支
   - git checkout -b my-test
   - git push origin my-test
   - git branch --set-upstream-to=origin/jw0013109
### git log -p filename /git log filename
### git rebase
   - git rebase 是干什么的
   - ##### 使用 git rebase -i commits 来修改已经提交的commit
      - [link](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2)
      - 修改的那个提交在log中会有两个
      - 修改前需要清空 工作目录吗
        - error: 不能rebase：您有未暂存的变更。
        - error: 另外，您的索引中包含未提交的变更。
        - error: 请提交或贮藏修改。
      - 可以stash pop 吗
        - 可以，只是要是stash pop后再把不需要的内容stash后这个stash的标题就会变成变基的那个
### 强推(force push) 为什么会对大的团队造成麻烦 ----------------------no
### 为什么切换分支后 把改动在另一个分支上提交后这个分支上就看不到改动了?
### .gitignore 失效
    在.gitignore 中定义的文件还会出现在git status中
    新建的文件在git中会有缓存，如果某些文件已经被纳入了版本管理中，就算是在.gitignore中已经声明了忽略路径也是不起作用的，这时候我们就应该先把本地缓存删除，然后再进行git的push，这样就不会出现忽略的文件了。git清除本地缓存命令如下：
    ```
    # 先进入根目录中
    git rm -r --cached .
    git add .
    git commit -m 'update .gitignore'
    ```
### git add -e 好像是用来编辑改变的，就还是编辑删除了什么内容，添加的什么内容的那个显示
### 忽略git 文件 .gitignore 会上传到库变成公共的
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
