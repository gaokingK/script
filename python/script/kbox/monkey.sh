# 包名：
# com.ss.android.lark  /飞书
# com.pingan.smt   /i深圳
# com.happyelements.AndroidAnimal /开心消消乐
# com.tencent.tim /tim
# com.example.chinesechess /途游象棋
# 测试命令：
adb shell monkey -p 包名 --hprof --pct-touch 50 --pct-motion 30 --pct-appswitch 10 --pct-majornav 10    --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes --ignore-crashes  --throttle 500 -v -v -v 19000 1>>/home/thtf/Desktop/monkey_test_info.log 2>>/home/thtf/Desktop/monkey_test_error.log