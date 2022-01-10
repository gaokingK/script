#! /bin/bash
#i=1
#sum=0
#包名 /类名
#com.ss.android.lark/.main.app.MainActivity   /飞书
#com.pingan.smt/.SplashActivity   /i深圳
#com.happyelements.AndroidAnimal/com.happyelements.hellolua.MainActivity /开心消消乐
#com.tencent.tim/com.tencent.mobileqq.activity.SplashActivity /tim
#com.example.chinesechess/com.tuyoo.main.EnterActivity  /途游象棋
# 测试时间持续1h，测试不同应用时按照注释修改脚本.。
# 测试过程中使用命令 adb shell logcat |grep 包名 >> log.txt 保存logcat 日志
while true
do
        adb install /home/huawei/Desktop/8_众智apk/feishu_4.10.3.apk #当前目录下apk包 
        adb shell am start -W   com.ss.android.lark/.main.app.MainActivity 
        sleep 2
        adb shell am force-stop com.ss.android.lark #包名
        adb shell am start -W  com.ss.android.lark/.main.app.MainActivity 
        sleep 2
        adb shell am force-stop com.ss.android.lark
        adb  uninstall com.ss.android.lark
done
