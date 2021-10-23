declare -A apps
apps=([meituan]="com.sankuai.meituan" )
/usr/bin/Kbox launcher uninstall -n com.sankuai.meituan -r n
/usr/bin/Kbox launcher install -r y -p /home/huawei/Desktop/pc_source/pc_android/apks/meituan.apk