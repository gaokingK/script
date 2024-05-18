#### 从底层检测弹窗
- link
  - [了解window](https://blog.csdn.net/A38017032/article/details/70148665?locationNum=9&fps=1)
  - [adb指南](https://developer.android.google.cn/training/testing/performance)
- 检测app的活动窗口
  - adb shell dumpsys window w 输出window list
    - 分析发现, 输出的窗口列表中, 在首页只有一个与包名相关的window, 在点击首页图标进去的子页面会有两个, 无论是否有弹窗, 猜测可能windows 数量可能与当前窗口的深度有关
  - 从系统日志中发现弹窗事件的日志
Quad/duallit/solo sabre auto board
# 安卓系统
- 将数据线短接能默认开启9008端口，可以拷贝出来系统文件
- 如何从升级包中查看软件包的android版本
  - 安卓系统升级包往往是一个包含多个文件和目录的ZIP文件。升级包中的system分区通常包含本次升级的安卓操作系统。
  - 安卓版本通常会被记录在/system/build.prop这个文件中。你可以从这个升级包中获取到这个文件，然后查找属性ro.build.version.release。这个属性的值就是安卓版本号。
# 安卓投屏，电脑控制android scrcpy
- https://www.iplaysoft.com/scrcpy.html
## 准备
### win
- 下载 https://github.com/Genymobile/scrcpy/blob/master/README.md#prerequisites
- 解压文件，打开open_a_terminal_here.bat
- 打开usb调试，输入scrapy.exe，手机上的弹窗点击同意
- 投屏就出现了
  
## 常用命令
- adb usb
- adb kill-server
- adb start-server
- scrcpy --prefer-text 可以使用键盘输入（必须PC上是英文输入的状态），不然就只能输入英文了
- https://cupster.blog.csdn.net/article/details/111386811
  - -S 打开镜像的时候手机息屏
- 鼠标右键打开屏幕
- Ctrl + P 电源键
- scrcpy.exe -S --prefer-text -m 800

## 问题
- Device unauthorized
  - 开发者模式下重开usb调试，弹窗点击同意
  
## GUI界面
- https://github.com/Tomotoes/scrcpy-gui/blob/master/README.zh_CN.md

# customize phone 
### 太极/taichi
- https://github.com/taichi-framework/TaiChi/blob/master/docs/zh/doc/getting_started.md

- 太极内添加需要的app，然后按照提示进行卸载、安装、优化


# adb
- 确保Android 设备的开发者选项和 USB 调试模式已开启
```cs
# 如下代表已连接
$ adb devices
List of devices attached
R28M32FWJ6X     device
```
- 从手机复制到电脑
adb pull 手机存储路径  电脑路径
`adb pull  sdcard/xxx  /Users/xxxx/ xxx.tx` #注意手机路径最前面不能加/
- 从电脑端向手机复制文件
输入: adb push 电脑路径  手机存储路径  
`adb push  /Users/xxxx/xxx.txt   /sdcard/`
- git 好像不能使用，或者是不能在E盘使用
```sh
adb push /e/Green/aria2/baiduyun/0_艾瑞泽gx18升级包update/fota.conf /sdcard/
E:/Green/aria2/baiduyun/0_艾瑞泽gx18升级包update/fot...: 1 file pushed, 0 skipped. 3.3 MB/s (484 bytes in 0.000s)
adb: error: failed to copy 'E:/Green/aria2/baiduyun/0_艾瑞泽gx18升级包update/fota.conf' to 'E:/software/Git/sdcard/': remote secure_mkdirs failed: No such file or directory
```
- 执行linux命令 输入adb shell 进入adb 命令行界面。
- 输出正在前台交互activity `adb shell dumpsys window | grep mCurrentFocus`
  - 输出的是app的活动名，可以启动
- 确定你想要启动的应用程序的包名和活动名（Activity Name）
  - `adb shell dumpsys package | grep -i '你的应用包名' | grep Activity`
- 启动某个app 需要找到活动名
  - `adb shell am start -n `
- 发送一个模拟 "home" 键的 adb 命令来将应用放到后台：
  - `adb shell input keyevent KEYCODE_HOME`
- adb shell ls sdcard 前面不要加/
- adb install apk.name 不能带空格要在shell外，是电脑端的路径
- 
# 包名
```cs
氢桌面  com.mcar.auto/com.mcar.auto.activity.IndexActivity
```
