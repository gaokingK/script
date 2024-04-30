### androidManifest.xml文件
是的，我知道关于 APK 文件中的 AndroidManifest.xml 文件的信息。
AndroidManifest.xml 是一个 Android 应用程序中的核心文件，位于 APK 的根目录。这个文件包含了关于应用程序的重要信息和配置细节。它必须按照 Android 平台定义的特定格式编写。
以下列出了一些 AndroidManifest.xml 文件中包含的主要信息：
Package 名称：应用程序的唯一标识符，通常采用反向域名格式。
应用版本：定义了 APK 的版本号和版本代码。
权限：申明应用程序请求的权限，比如访问网络、读写存储等。
应用组件：包括活动（Activity）、服务（Service）、内容提供者（Content Provider）、广播接收者（Broadcast Receiver）。
Intent Filter：声明了应用程序可以响应的各种 Intent。
支持的硬件和软件特性：比如需要摄像头或者某个特定的屏幕尺寸。
SDK 最小要求：定义了应用程序需要的最小 Android API 级别。
API 兼容性和目标版本：定义了编写应用程序时所针对的 API 级别。
由于 XML 文件在 APK 中是经过压缩和编译的，因此要查看 AndroidManifest.xml 文件的内容，可能需要特定的工具来解码。有时这个过程被称为“反编译” APK。常见的工具比如 apktool，可以用来抽取和查看 APK 中的 AndroidManifest 文件内容。

# apktool
apktool.bat d -f 2_酷我音乐车机版\ v6.0.1.0车机共存会员版.apk -o test_app

# 签名
 keytool -genkey -v -keystore my-release-key.keystore -alias my_release_key -keyalg RSA -keysize 2048 -validity 10000
 密码短语 jaingjinwei
 生成的密码文件会保存在命令的执行目录下
 文件不能被移动