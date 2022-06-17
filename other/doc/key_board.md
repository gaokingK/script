# vscode
- 移动当前行 alt + up/down
- alt + shift + up/down 复制当前行
- ctrl + shift +up/down 多行编辑，移动光标
- 配置颜色
    ```json
    // link: https://code.visualstudio.com/docs/getstarted/themes
   	"settings": {
		"workbench.colorCustomizations": {
			//"searchEditor.findMatchBackground": "#ff0000",
			//"searchEditor.textInputBorder": "#ff0000",
			//"editor.findMatchBackground": "#ff0000",
			"editor.findMatchHighlightBackground": "#ff0000",
			// "editor.findRangeHighlightBackground": "#ff0000",
			// "editor.findMatchBorder": "#ff0000",
			// "editorOverviewRuler.findMatchForeground": "#ff0000"
		}
	}
    ```

# pycharm 
- pycharm 定位打开的文件(select opened file) 不显示成员
	- 在旁边的设置中，取消选中show members
- 创建文件时，自动生成文件头
	- Files>Setting>Editor>File and Code Templates
- 可以重命名project 和 directory
- 一般是按ctrl 点击寻找定义，如果变量找不到可以按ctrl+alt
- 按下Alt 点击close = 关闭all other 
- inspections 一些检查项
- ctrl + E 最近文件
- ctrl + shift + E 最近记录
- ctrl + F12 当前文件中的函数和变量概览
- ctrl + N 搜索类、文件名、方法等
- 可以从log 里看 仓库各个分支的提交log， 来判断动态（profess）
- 没有git状态栏 
    - setting>Version Control 添加project VCS 映射就有了
- 新建的文件忘了命名类型,被记住了Setting>File Types>Recognized File Types> Auto-detect file 然后删掉
- pycharm c f v 代表什么?
    - link: https://www.jetbrains.com/help/pycharm/symbols.html
    - link2:  
- pycharm 设置自动换行
  - link：https://www.cnblogs.com/grimm/p/12401826.html
  -  File-> Settings-> Editor-> General 找到Soft Wraps，勾选Soft-wrap files

- pycharm 统计代码行数
	- 搜索安装Statistic插件
	- pycharm状态栏中点击插件；点击refresh selected on；（要选中项目）
- 包裹代码
	- 选中代码，ctrl+Alt+T 但是这个只能加if这种
	- 如果先要加函数的就先选中，再按括号，再跳到左边
- 调试
	- 看成员引用的时候 read 和 write过滤
		- self.hosts[host['id']] = hostObj 会在读里面
	- 运行到光标处时， 空的for循环会停下，但false的if不会停下 
# uos
- ctrl + ; 剪贴板
   
# linux
- 终端 ctrl + Shift + / 快捷键信息
- 怎么搜索历史命令 切换下一条?
- 在终端中使用上次命令中的内容 ---------------------------no
- [shell命令行 快捷键](https://www.cnblogs.com/betterquan/p/11456820.html)
```
Alt + f, b ：按单词前移（右向）/后移（左向）

```