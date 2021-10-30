### git
1. ##### git patch --------------------------------no
2. ##### git checkout
   1. `git checkout branch_name high_quality/dingding/function/.` 即使这个要检出的文件在现在的分支上不存在也可以检出的
3. ##### 这张图里怎么把code从repo checkout到workspace
      ![git fetch和git pull的概念](http://kmknkk.oss-cn-beijing.aliyuncs.com/image/git.jpg)
4. ##### [git fetch](https://www.cnblogs.com/runnerjack/p/9342362.html) -----------------------------no
5. ##### [git hook](https://www.git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-Git-%E9%92%A9%E5%AD%90)
   - 非0值是指程序异常退出
   - 为hook添加运行程序是chmod这样加
   - 程序需要 `#！/path/to/python3`
6. ##### 忽略换行符
   1. [link](https://blog.csdn.net/nanyilou_xiaoye/article/details/79075092) -------------------------no
7. ##### 查看分支的提交历史 git log --graph --pretty=oneline --abbrev-commit branch1 branch2
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
8. ##### git mergetool -t opendiff --------------------------------------no
9.  ##### git cherry-pick 来将A分支的部分提交合并到B分支上
   1. 如果需要多个commitid `git cherry-pick commitid_a commitid_b commitid_c` 只合并这三个
   2. 先合并a, 如果有冲突就结局, 然后git cherry-pick --continue 完成后就把a给搞好了; 然后合并b,如果有冲突, 解决,然后git cherry-pick --continue....
10. ##### [把同一个分支里的提交放到其他的分支里](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md#rebasing-%E5%92%8C%E5%90%88%E5%B9%B6merging)
   3. git log commitid1, commitid2, commit3
   4. git reset --hard commit3
   5. git checkout -b new_branch
   6. git cherry-pick commid1 # 即使commitid 在git log中看不到了, 已经reset-hard了,仍然能找到这个commit
11. ##### git branch
   7. [link](https://blog.csdn.net/duxing_langzi/article/details/80295573?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)
   8. 在新建分支上切换到master之前, 要留意你的工作目录和暂存区里那些还没有被提交的修改， 它可能会和你即将检出的分支产生冲突从而阻止 Git 切换到该分支。 最好的方法是，在你切换分支之前，保持好一个干净的状态。 有一些方法可以绕过这个问题（即，暂存（stashing） 和 修补提交（commit amending））
   9. 当你切换分支的时候，Git 会重置你的工作目录，使其看起来像回到了你在那个分支上**最后一次提交**的样子
12. ##### git log -p filename /git log filename
13. ##### git rebase
   10. git rebase 是干什么的
   11. ##### 使用 git rebase -i commits 来修改已经提交的commit
      - [link](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2)
      - 修改的那个提交在log中会有两个
##### 强推(force push) 为什么会对大的团队造成麻烦
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
