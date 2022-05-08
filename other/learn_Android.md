#### 从底层检测弹窗
- link
  - [了解window](https://blog.csdn.net/A38017032/article/details/70148665?locationNum=9&fps=1)
  - [adb指南](https://developer.android.google.cn/training/testing/performance)
- 检测app的活动窗口
  - adb shell dumpsys window w 输出window list
    - 分析发现, 输出的窗口列表中, 在首页只有一个与包名相关的window, 在点击首页图标进去的子页面会有两个, 无论是否有弹窗, 猜测可能windows 数量可能与当前窗口的深度有关
  - 从系统日志中发现弹窗事件的日志