[link](https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html#virtualenv)
### 安装（确保 virtualenv 已经安装了）：
对于Windows，您可以使用 virtualenvwrapper-win 。
`pip install virtualenvwrapper-win`
在Windows中，WORKON_HOME默认的路径是 %USERPROFILE%\Envs 。

### 基本使用
- 创建一个虚拟环境：
`$ mkvirtualenv [-p python_verison_path] my_project`
这会在 ~/Envs 中创建 my_project 文件夹。

- 在虚拟环境上工作：
`$ workon my_project`

- 或者，您可以创建一个项目，它会创建虚拟环境，并在 $WORKON_HOME 中创建一个项目目录。 当您使用 workon myproject 时，会 cd 到项目目录中。

`$ mkproject myproject`
virtualenvwrapper 提供环境名字的tab补全功能。当您有很多环境， 并且很难记住它们的名字时，这就显得很有用。
workon 也能停止您当前所在的环境，所以您可以在环境之间快速的切换。

- 停止是一样的：
`$ deactivate`

- 删除：
`$ rmvirtualenv my_project`
### 其他有用的命令
- `lsvirtualenv` 列举所有的环境。
- `cdvirtualenv` 导航到当前激活的虚拟环境的目录中，比如说这样您就能够浏览它的 site-packages 。
- `cdsitepackages` 和上面的类似，但是是直接进入到 site-packages 目录中。
- `lssitepackages` 显示 site-packages 目录中的内容。
- `virtualenvwrapper` 命令的完全列表 。
- `cpvirtualenv oldenv newenv; rmvirtualenv oldenv` 重命名虚拟空间