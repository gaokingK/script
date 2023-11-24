### goto https://blog.csdn.net/weixin_33806509/article/details/91988385
- 指定跳转到标签，找到标签后，程序将处理从下一行开始的命令。
```
@echo off
:start
cls
set /p numis=请输入数字1或2：
if /i "%numis%"=="1" goto 1
if /i "%numis%"=="2" (goto 2) else (echo 输入有误!&&pause>nul&&goto start)
:1
echo 你输入的是1
pause>nul&&goto start
:2
echo 你输入的是2
pause>nul&&goto start

```