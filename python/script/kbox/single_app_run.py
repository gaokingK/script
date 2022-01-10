#包名：
#com.ss.android.lark  /飞书
#com.pingan.smt   /i深圳
#com.happyelements.AndroidAnimal /开心消消乐
#com.tencent.tim /tim
#com.example.chinesechess /途游象棋
#测试脚本如下：
import uiautomator2 as u2
import time
usb_connect_addr="0.0.0.0:8501"
d=u2.connect(usb_connect_addr)
d.logger
#i深圳
for i in range (5000):
    try:
        d.xpath(
            '//*[@resource-id="com.pingan.smt:id/app_navigation"]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar-b[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(0.5)
        d.xpath(
            '//*[@resource-id="com.pingan.smt:id/recycler_view"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        time.sleep(0.5)
        d.xpath(
            '//*[@resource-id="com.pingan.smt:id/officehall_recyclerView"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]').click()
        time.sleep(1)
        d.xpath('//*[@text="二、三级运动员授予"]').click()
        time.sleep(4)
        d.xpath('//*[@resource-id="com.pingan.smt:id/iv_title_left"]').click()
        d.xpath('//*[@resource-id="com.pingan.smt:id/iv_title_left"]').click()
        time.sleep(0.5)
        d.xpath('//*[@resource-id="com.pingan.smt:id/iv_title_left"]').click()
        d.xpath(
            '//*[@resource-id="com.pingan.smt:id/app_navigation"]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar-b[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(30)
        print(i)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        d.p
    except:
        pass
#飞书
for i in  range (1000000):
    try:
        d.xpath('//*[@resource-id="com.ss.android.lark:id/toolbox_et_message"]').click()
        d.xpath('//*[@content-desc="W"]').click()
        d.xpath('//*[@content-desc="r"]').click()
        d.xpath('//*[@content-desc="g"]').click()
        d.xpath('//*[@resource-id="com.ss.android.lark:id/btn_send"]').click()
        d.swipe_ext("up", 0.2)  # 向上滑动%20,退出输入法
        time.sleep(45)
        d.xpath('//*[@resource-id="com.ss.android.lark:id/toolbox_btn_emoji"]').click()
        time.sleep(3)
        d.xpath(
            '//*[@resource-id="com.ss.android.lark:id/emoji_recv"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]').click()
        time.sleep(0.5)
        d.xpath('//*[@resource-id="com.ss.android.lark:id/btn_send"]').click()
        time.sleep(25)
        d.swipe_ext("up", 0.2)
        time.sleep(15)
        print(i)
        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    except:
        pass
#tim
for i in range (100000):
    try:
        d.xpath(
            '//*[@resource-id="com.tencent.tim:id/recent_chat_list"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]').click()
        time.sleep(0.5)
        d.xpath('//*[@resource-id="com.tencent.tim:id/input"]').click()
        d.xpath('//*[@content-desc="q"]').click()
        d.xpath('//*[@content-desc="w"]').click()
        d.xpath('//*[@content-desc="e"]').click()
        d.xpath('//*[@content-desc="f"]').click()
        d.xpath('//*[@resource-id="com.tencent.tim:id/cq9"]').click()
        time.sleep(0.5)
        d.xpath('//*[@resource-id="com.tencent.tim:id/e89"]').click()
        time.sleep(0.5)
        d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[2]').click()
        time.sleep(2)
        d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[1]').click()
        time.sleep(30)
        print(i)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    except:
        pass
#象棋
for i in range (100000):
    try:
        d.click(116, 817)
        d.click(359, 823)
        time.sleep(0.5)
        d.click(200, 745)
        time.sleep(0.5)
        d.click(200, 669)
        time.sleep(0.5)
        d.click(117, 981)
        time.sleep(0.5)
        d.click(196, 825)
        time.sleep(0.5)
        d.click(43, 980)
        d.click(119, 980)
        time.sleep(0.5)
        d.click(676, 738)
        d.click(682, 664)
        time.sleep(0.5)
        d.click(599, 581)
        d.click(680, 827)
        time.sleep(0.5)
        d.click(84, 126)
        time.sleep(0.5)
        d.click(364, 317)
        time.sleep(26)
        print(i)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    except:
        pass
#消消乐
for i in range (100000):
    try:
        d.click(362, 880)
        d.click(435, 880)
        time.sleep(0.5)
        d.click(574, 750)
        d.click(574, 808)
        time.sleep(0.5)
        d.click(431, 736)
        d.click(425, 661)
        time.sleep(28)
        print(i)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    except:
        pass
# 需要分别测试，测试i深圳时直接打开到主页面即可；tim需要进入某一个联系人通信界面；飞书进入主界面，只要有可以通讯的联系人即可；象棋启动到主界面即可，但是需要点击掉其他弹出页面；消消乐需要进入某一个关卡内即可。
# 需要分辨保存日志，使用adb logcat -> xxx_log.txt
