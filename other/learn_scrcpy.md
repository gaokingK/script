# 安卓投屏，电脑控制android
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