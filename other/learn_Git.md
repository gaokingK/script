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
- client_global_hostkeys_private_confirm: server gave bad signature for RSA key 0: error in libcrypto
   - link: https://stackoverflow.com/questions/67401049/pulling-from-git-fails-and-gives-me-following-error-client-global-hostkeys-priv
   - 原因：
   - 是某些ssh版本的issue
   - 不影响
   - 解决：
   - 未解决
   - 按照link上操作没有生效，可能是config这个文件的扩展名没有用

- Filename too long in Git for Windows
   - link: https://stackoverflow.com/questions/22575662/filename-too-long-in-git-for-windows
   - 解决：
   - git config --system core.longpaths true
   - - 原因：
   - git 版本使用的是windows的老版本API，对字符长度的限制是260个
- git remote设置的是ssh地址，push 提示ssh: connect to host github.com port 22: Connection refused
   - link:https://zhuanlan.zhihu.com/p/521340971
   - windows也可以使用更改config文件修改22端口到443端口
   ```cs
   vim ~/.ssh/config
   # Add section below to it
   Host github.com
      Hostname ssh.github.com
      Port 443
   ```
- git clone https://github.com/derekparker/delve.git 报Failed to connect to github.com port 443
   - 采用ssh地址，看不到是因为github没有登陆账号
- fatal: unable to access 'https://github.com/ScoopInstaller/Main.git/': Failed to connect to github.com port 443 after 21204 ms: Couldn't connect to server 
   - 明明开了vpn
   - 因为git没有用代理，在git中设置：
      - `git config --global http.proxy http://127.0.0.1:10809` 这个端口是你vpn在本地的http监听端口
      - `git config --global https.proxy http://127.0.0.1:10809`
   - 清除设置
      - `git config --global --unset http.proxy`
      - `git config --global --unset https.proxy`

## 帮助
- https://docs.gitlab.com/ee/topics/git/stash.html
## other
### 工作区、暂存区、版本库
- 直接修改的文件会在工作区显示出来，使用git add 后被添加到暂存区；commit后就在版本库了
- 对暂存区的文件执行`git reset HEAD .`后，文件的改动在工作区
- 对工作区的文件执行 `git checkout -- path/to/file` 后， 文件的改动被撤销了
-- git checkout commit_id  -- app/reso_info/views.py 将文件回退到某个版本
### git clone
-- git clone --depth=1 只克隆下包含最近一次commit的一个分支，这样这个项目文件就不会很大 https://blog.csdn.net/qq_43827595/article/details/104833980
-- git clone --recursive
-- git clone --recurse-submodules递归克隆子项目 https://blog.csdn.net/Mark_md/article/details/121640755 如果直接clone，子模块的代码为空
- clone http配置免密 git config --global credential.helper store 只需要输入一次密码就可以
- 直接输入密码 git clone http://username:password@10.xxxx/path/to/repo.git
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
```sh
# 删除 untracked files
git clean -f
 
# 连 untracked 的目录也一起删掉
git clean -fd
 
# 连 gitignore 的untrack 文件/目录也一起删掉 （慎用，一般这个是用来删掉编译出来的 .o之类的文件用的）
git clean -xfd
 
# 在用上述 git clean 前，墙裂建议加上 -n 参数来先看看会删掉哪些文件，防止重要文件被误删
git clean -nxfd
git clean -nf
git clean -nfd

uhippo
关注
```
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
执行 `git reset --hard` 命令会对你的 Git 仓库产生三方面的影响：

1. **HEAD 移动到指定的提交**：
   - `git reset --hard` 命令会把当前分支的 HEAD（也就是当前分支的指针）移动到你指定的提交上。如果你没有指定提交，默认是当前分支的最新提交。这意味着所有该提交之后的修改都会被“抛弃”。

2. **工作区（Working Directory）的更改**：
   - 这个命令会更新你的工作区（Working Directory），使其内容与 HEAD 指向的提交完全一致。这意味着在工作区的所有本地修改（无论是已暂存的还是未暂存的更改）都会被删除。仓库会恢复到执行该命令指定的那个提交状态。

3. **暂存区（Staging Area）的更改**：
   - 该命令还会清除暂存区（Staging Area）中的所有更改，使其与 HEAD 指向的提交完全一致。实际上，执行 `git reset --hard` 后，你的工作区和暂存区会和你使用该命令指定的那个提交一模一样。

使用 `git reset --hard` 命令时需要非常谨慎，因为它会丢弃所有未提交的更改，并且这个操作是无法撤销的。如果你删除了还未推送（push）到远程仓库的提交，这些提交可能会永久丢失。

如果你不确定，或者想保留对文件所做的更改，可以考虑使用 `git reset --soft` 或 `git reset --mixed`：

- `git reset --soft`：会保留工作区和暂存区的更改，只移动 HEAD 指针。
- `git reset --mixed`（这是默认选项）：会保留工作区的更改，但清空暂存区，也会移动 HEAD 指针。

在使用 `git reset --hard` 之前，确保你真的不需要那些更改，或者你已经做了足够的备份。另外，如果你在执行这个命令之后意识到了错误，并且你的某些更改尚未被 git 垃圾收集（garbage collected），你可能还能通过 `git reflog` 和 `git reset` 命令找回一些“丢失”的提交。

## 恢复使用 `git reset --hard` 丢失的更改可能会有些复杂，但并非完全不可能。下面是一些可能帮助你恢复丢失更改的方法：

### 1. 使用 `git reflog`

1. **检查引用日志（Reflog）**:
   - 执行 `git reflog` 可以查看你本地仓库的历史操作记录（包括提交、重置等）。每条记录都关联着一个 HEAD@{n} 引用和一个提交哈希值。
   - 找到你想回到的状态对应的提交哈希值。这可能是一个丢失的提交，或者是使用 `git reset --hard` 之前的状态。

2. **切换到该状态**:
   - 使用 `git reset --hard HEAD@{n}` 命令（其中，`n` 是你从 reflog 中找到的索引号），你可以将当前分支的 HEAD 指针重置到那个状态，从而恢复到 `git reset --hard` 执行之前的状态。

### 2. 如果你有未推送的提交

如果你执行了 `git reset --hard`，但实际上有一些更改已经提交但未推送到远程仓库，那么你可以看看远程仓库的状态是否有帮助：

1. **检查远程分支的状态**:
   - 使用 `git log origin/<branch_name>` 查看远程分支的提交历史（这里 `<branch_name>` 是你的远程分支名）。如果你在重置之前已经将更改提交到了本地仓库，但没有推送，可以通过远程仓库中的提交记录找到线索。

2. **如果更改已经推送**:
   - 如果你的更改已经推送到远程仓库，你可以使用 `git fetch` 更新本地仓库的远程跟踪分支，然后使用 `git reset --hard origin/<branch_name>` 将本地分支重置到远程分支的当前状态。

### 注意：

- `git reflog` 是根据你的本地操作记录来的，所以它可能包含那些还没有推送到远程仓库的提交。这使得它成为恢复因硬重置而丢失的本地更改的有效手段。
- 使用 `git reset` 时要非常小心，尤其是加上 `--hard` 选项，因为它可以将你的更改（包括未提交的更改）彻底清除。

记住，如果你的更改还未曾被提交过，那么 `git reset --hard` 后这些更改很可能会被彻底丢失，除非这些更改有备份。因此，恢复操作主要针对那些已被提交但后来由于操作失误而丢失的情况。

# 冲突
   - 冲突的原因
     - 无论是branchA合并到branchB还是branchB合并到branchA 只要有某个文件的改动前内容不一致就会冲突（branchA从内容A改到内容B 如果branchB有改动 只要branchA的内容A和branchB的内容A不一样就会产生冲突）
   - 什么情况下会有冲突
      - user a 修改file_a 10行, commit and push, user b 已另一种内容修改file_a 10行, commit and push, 会发现push 被拒绝, 然后push -f, 这时usera 再pull 就需要merge 这种情况的解决办法:
         - 可以user b reset --hard 然后 pull push
         - user a add . /commit 这时log 会不对(其实也是对的), reset hard 到 双方都提交之前的那个commit ,然后在pull ,这时库上是b的改动(想想也合理)

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
   - `core.autocrlf` [link](https://www.jianshu.com/p/f13ef9e538e0)
```
core.autocrlf=true:      core.autocrlf=input:     core.autocrlf=false:

     repository               repository               repository
      ^      V                 ^      V                 ^      V
     /        \               /        \               /        \
crlf->lf    lf->crlf     crlf->lf       \             /          \
   /            \           /            \           /            \
```
   - `git config --global` 不加global只对当前仓库生效
   - `git config -l` 查看配置
   - git config --system core.autocrlf false            # per-system solution
   – git config --global core.autocrlf false            # per-user solution
   – git config --local core.autocrlf false              # per-project solution
   
   - git config --global user.name "bryan sun"
   - git config --global user.email "hitsjt@gmail.com"
### git checkout
   - `git checkout branch_name high_quality/dingding/function/.` 即使这个要检出的文件在现在的分支上不存在也可以检出的
在Git中，如果你想将某个文件恢复到某个特定的版本（也称为提交或者commit），你可以使用以下命令：

1. 首先，找到你想恢复到的那个版本的提交ID。你可以使用 `git log` 命令来查看提交历史，并找到对应的提交ID。提交ID是一个长串的哈希值，但通常只需要前几个字符就足够区分不同的提交了。

   ```sh
   git log
   ```
   
   或者，如果你知道文件的名称，可以使用 `git log` 加上文件路径来获取该文件的提交历史：

   ```sh
   git log -- path/to/your/file
   ```

2. 一旦你找到了想要回滚到的那个提交的ID（比如 `commitID`），使用以下命令将文件回滚到那个版本：

   ```sh
   git checkout commitID -- path/to/your/file
   ```

   这里 `commitID` 是你在步骤1中找到的提交ID，`path/to/your/file` 是你想要恢复的文件路径。

3. 此时，该文件在你的工作区已经是那个历史版本的内容了。如果你想将这个变更保存到你的仓库中，就需要像平常提交代码一样，先使用 `git add` 将其暂存，然后使用 `git commit` 创建一个新的提交。

   ```sh
   git add path/to/your/file
   git commit -m "Restore path/to/your/file to its state as of commitID"
   ```

   这个步骤会在你的提交历史中创建一个新的提交，其内容是你指定的那个历史版本的文件。

请注意，使用这种方法恢复文件到特定版本会影响你的工作区和暂存区的状态，但不会修改你的提交历史（除了你最后创建的那个新提交）。确保在执行这些操作之前，你的工作区是干净的（没有未提交的更改），否则你可能会遇到冲突。
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
      - git diff [<options>] <commit> <commit>…​ <commit> [--] [<path>…​] 看某个路径下的两个提交之间的不同
      - git diff 5605d96 HEAD --stat  -- app/reso_info/views.py 如果没有head 就是和当前做比较

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
   - 先合并a, 如果有冲突就解决然后git add ., 然后git cherry-pick --continue 完成后就把a给搞好了; 然后合并b,如果有冲突, 解决,然后git cherry-pick --continue....
### [把同一个分支里的提交放到其他的分支里](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md#rebasing-%E5%92%8C%E5%90%88%E5%B9%B6merging)
   - git log commitid1, commitid2, commit3
   - git reset --hard commit3
   - git checkout -b new_branch
   - git cherry-pick commid1 # 即使commitid 在git log中看不到了, 已经reset-hard了,仍然能找到这个commit
### branch
   - [git branch 命令查看分支、删除远程分支、本地分支](https://blog.csdn.net/duxing_langzi/article/details/80295573)
   - 在新建分支上切换到master之前, 要留意你的工作目录和暂存区里那些还没有被提交的修改， 它可能会和你即将检出的分支产生冲突从而阻止 Git 切换到该分支。 最好的方法是，在你切换分支之前，保持好一个干净的状态。 有一些方法可以绕过这个问题（即，暂存（stashing） 和 修补提交（commit amending））
   - 当你切换分支的时候，Git 会重置你的工作目录，使其看起来像回到了你在那个分支上**最后一次提交**的样子
   - 将本地新建的分支同步到origin `git push --set-upstream origin merge2`
   - `git branch -vv `查看本地分支关联（跟踪）的远程分支之间的对应关系
   - `git branch -a `查看所有分支 remote/origin/master表示的是远程分支
   - `git push origin --delete Chapater6` 可以删除远程分支Chapater6 在删除远程分支时，同名的本地分支并不会被删除，所以还需要单独删除本地同名分支
      - for branch in $(git branch -a|grep new_branch|awk -F"/" '{print $NF}');do git push origin --delete $branch;done
      - 如果发生以下错误:
         error: unable to delete ‘origin/xxxxxxxx-fixbug’: remote ref does not exist
         error: failed to push some refs to ‘git@github.com:xxxxxxxx/xxxxxxxxxx.git’
         解决办法： git checkout xxxxx-fixbug 切换到当前分支上， 然后再 进行 git push --delete origin origin/xxxxx-fixbug
   - `git branch -d Chapater8 `可以删除本地分支（在主分支中）
   - `git fetch -p` 清理本地无效分支(远程已删除本地没删除的分支): 
   - git branch -M main 重命名当前分支为main
#### 使用分支合并
   - git pull git_url
   - git checkout -b branch_name origin/branch_name # 远程已经新建了branch_name
   - git pull master # 在自己分支上
   - 只拉取远程分支 `git init; git remote add origin xxx.git; git fetch origin develop（develop为远程仓库的分支名）`
      - link: https://blog.csdn.net/carfge/article/details/79691360
#### 创建远程分支
   - link：https://juejin.cn/post/6844903841507311623
   - git checkout -b my-test
   - push时设置：git push -u origin test
   - branch设置：git branch --set-upstream-to=origin/jw0013109  or git branch -u origin/test
   - 取消设置：git branch --unset-upstream [<branchname>]
### git log
- git log -p filename /git log filename
- git log branch_name 查看某个分支的log
- git log 查看当前分支的提交历史
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

# git 初始化仓库时添加多个已经存在的仓库，从本地文件添加
- git init repo;cd repo
- git submodule add /path/to/already_repo
- 使用 Git 子模块的方式可以保留并查看每个子模块（即现有仓库）的提交历史。每个子模块实际上是一个独立的 Git 仓库，保留了它自己的提交记录、分支和标签。但是需要进入仓库看
### git submodule 时git submodule add fatal: transport 'file' not allowed
-  git config --global protocol.file.allow always

# git add 
### git add -e 好像是用来编辑改变的，就还是编辑删除了什么内容，添加的什么内容的那个显示
### 将除了a.txt 外的文件都添加到
- git add . -- :!a.txt
- git add .; git reset a.txt


### 搜索改动过某个文件的提交
```py
- git log --oneline --since="1 week" -- "*.config.js"
- git log --name-status --grep="package.json"
# 显示每次提交中修改的文件列表和状态
git log --oneline --name-status

# 查看某个文件的变更历史
git whatchanged -- 文件名
# 显示统计信息
git whatchanged --stat -- 文件名

# 搜索提交信息中包含文件名的提交
git log --oneline --grep="文件名"
```
### 可以按提交信息搜索
- 加上grep
