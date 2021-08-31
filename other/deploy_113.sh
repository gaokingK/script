#!/bin/bash
if [ "$BASH" != "/bin/bash" ] && ["$BASH" != "/usr/bin/bash" ]
then
	bash "$0" "$@"
	exit $?
fi
echo `whoami`
if [ `whoami`  != "root" ]
then
	echo "请使用root"
	su
	echo "$?"
	if [ $? = 0]
	then
		echo "su sucess"
	else
		echo "su failed"
	fi
        echo "..."	
	exit $?
fi
echo "结束"
exit $?
app_packages=(com.hexin.plat.android,com.tencent.wemeet.app,com.tencent.mm)
function error(){
	echo -e "\033[1;31m$1\033[0m"
	exit 1
}

function check_network(){
	ping -c 3 90.90.0.112 > /dev/null 2>&1
	[ $? != 0 ] && error "有线未连接"
}

function update_kbox(){

	#scp -rp huawei@90.90.0.112:/home/huawei/kbox /home/huawei
	cd /home/huawei/kbox
	sh Uninstall.sh
	sleep 5
	sh Install.sh
	sleep 30
	#adb connect 172.17.0.2:5555
}

function uninstall_app(){
	pc_user=$(env|grep USER|awk -F '=' '{print $2}')
	echo $pc_user
	for package_name in `adb shell pm list package -3`
	do
		su ${pc_user} -c '/usr/bin/Kbox launcher uninstall -n '${package_name#*:}' -r n'
	done
	# 删除图标
	rm -rf /usr/share/applications/*.desktop
}
		
function install_app(){
	cd /home/huawei/Desktop/pc_source/pc_android/apks
	user=$(env|grep USER)
	pc_user=${user:5}
	for file in `ls|grep apk`
	do
		echo "准备安装/home/huawei/Desktop/pc_source/pc_android/apks/${file}"
		su ${pc_user} -c "/usr/bin/Kbox launcher install -p /home/huawei/Desktop/pc_source/pc_android/apks/${file} -r n"
		sleep 3
		if [ $? != 0 ]
		then
			error "安装失败${file}"
		fi
	done

}

function create_icon(){
	user=$(env|grep USER)
	pc_user=${user:5}
	for package_name in `adb shell pm list package -3`
	do
		sleep 3
		su ${pc_user} -c '/usr/bin/Kbox launcher createicon -n '${package_name#*:}' -p /usr/share/applications/'
		if [ $? != 0 ]
		then
			error "创建${package#*:}图标失败"
		fi
	done
}

main(){
	#check_network
	update_kbox
	install_app
	create_icon
}	
main
exit 0
	
