### 抓微信小程序 小塔预约练车
- 微信选择使用代理登录，ip写pc的使能ip，端口写filder里配置的端口
- link：https://www.bilibili.com/read/cv18896521/

### 获取列表接口 showGroupInfo
- 请求
```
url: https://api.ccore.cc/group/showGroupInfo?appointId=1501824148991008769&activeDate=2023-02-20&carManagerId=1503315595447656449 HTTP/1.1 GET
appointId 应该是驾校的，carmanagerid是教练的
header:
    access_token: 1570937481111212034
```
- 响应 已经开始的
- configItems里面是8个时间段的信息，里面的id就是预约时提交的itemId，
- configItems->recordlist里面是预约人的信息（未开启预约时这里是空列表），join可预约时是true,id是取消预约时的id

```json
{
    "success": true,
    "content": {
        "configItems": [
            {
                "id": "1502554985576824833",
                "configId": "1502554985560047617",
                "startTime": "08:00",
                "endTime": "09:00",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-04-30 09:22:58",
                "recordList": [
                    {
                        "id": "1627095625128681474",
                        "appointId": "1501824148991008769",
                        "itemId": "1502554985576824833",
                        "itemDate": "2023-02-20",
                        "startTime": "08:00",
                        "endTime": "09:00",
                        "userId": "1558046228933709826",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "27",
                        "createTime": "2023-02-19 08:00:01",
                        "appUser": {
                            "id": "1558046228933709826",
                            "userName": "一口薛糕ᰔᩚ",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/jazNqJ87bGLe33ED0kKpYYZDjowmuvLy1KchkxiblX202iarTl6AnQaunTXrCwb23hjq944x3WCmdb44MMMK6O6Q/132",
                            "unionId": "oz6cFwBka1YtVn1jx_JOc2WruGQQ",
                            "ref": "1501777218906775554",
                            "createTime": "2022-08-12 19:02:22",
                            "updateTime": "2022-08-12 19:03:09",
                            "subscribe": "false",
                            "realName": "薛精俏",
                            "mobileNo": "18538174629"
                        }
                    },
                    {
                        "id": "1627095632556793857",
                        "appointId": "1501824148991008769",
                        "itemId": "1502554985576824833",
                        "itemDate": "2023-02-20",
                        "startTime": "08:00",
                        "endTime": "09:00",
                        "userId": "1609777958779916289",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "8",
                        "createTime": "2023-02-19 08:00:03"
                    },
                    {
                        "id": "1627095633109487617",
                        "appointId": "1501824148991008769",
                        "itemId": "1502554985576824833",
                        "itemDate": "2023-02-20",
                        "startTime": "08:00",
                        "endTime": "09:00",
                        "userId": "1574358699348791297",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "15",
                        "createTime": "2023-02-19 08:00:03"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555028042702850",
                "configId": "1502554985560047617",
                "startTime": "09:00",
                "endTime": "10:00",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:00:09",
                "recordList": [
                    {
                        "id": "1627095823359877122",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555028042702850",
                        "itemDate": "2023-02-20",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "userId": "1560557285333995521",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "11",
                        "createTime": "2023-02-19 08:00:48",
                        "appUser": {
                            "id": "1560557285333995521",
                            "userName": "MX",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKIfqPicK4ibpxL1bOuicRaKKIiaz0OCSAjwesplMKBx6ibeVvbs5XoaNg7aU5Ww3xfJ5ob5sxuAqx8ToA/132",
                            "unionId": "oz6cFwCjsxYVMSYoWq1OZO61xD4o",
                            "ref": "1501777218906775554",
                            "createTime": "2022-08-19 17:20:25",
                            "updateTime": "2022-08-19 17:21:05",
                            "subscribe": "false",
                            "realName": "王明雪",
                            "mobileNo": "15938674626"
                        }
                    },
                    {
                        "id": "1627095845379973121",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555028042702850",
                        "itemDate": "2023-02-20",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "userId": "1508017686874750977",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "32",
                        "createTime": "2023-02-19 08:00:54"
                    },
                    {
                        "id": "1627095872000266241",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555028042702850",
                        "itemDate": "2023-02-20",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "userId": "1575760067215646722",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "12",
                        "createTime": "2023-02-19 08:01:00"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555080145797122",
                "configId": "1502554985560047617",
                "startTime": "10:00",
                "endTime": "11:00",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:00:21",
                "recordList": [
                    {
                        "id": "1627096646260396033",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555080145797122",
                        "itemDate": "2023-02-20",
                        "startTime": "10:00",
                        "endTime": "11:00",
                        "userId": "1520203887934095361",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "8",
                        "createTime": "2023-02-19 08:04:05",
                        "appUser": {
                            "id": "1520203887934095361",
                            "userName": "承诺*^_^*幸福",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/LT00eIZBicOAuyvWg7EcuU5AEDHAnN4LNicQ09UYyLOjsCke4H5pLicKR8mLaO3WMpeCSLwU19oCpRQnK7ibDw8H7A/132",
                            "unionId": "oz6cFwLWG2Fx4aSf3RjlNM0Or8zk",
                            "ref": "1501777218906775554",
                            "createTime": "2022-04-30 08:50:25",
                            "updateTime": "2022-05-02 17:47:35",
                            "subscribe": "false",
                            "realName": "霍飞鸽",
                            "mobileNo": "18838115482"
                        }
                    },
                    {
                        "id": "1627099478209273857",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555080145797122",
                        "itemDate": "2023-02-20",
                        "startTime": "10:00",
                        "endTime": "11:00",
                        "userId": "1570934624545300481",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "17",
                        "createTime": "2023-02-19 08:15:20"
                    },
                    {
                        "id": "1627131156922404865",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555080145797122",
                        "itemDate": "2023-02-20",
                        "startTime": "10:00",
                        "endTime": "11:00",
                        "userId": "1625388333593206786",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "3",
                        "createTime": "2023-02-19 10:21:13"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555129412091906",
                "configId": "1502554985560047617",
                "startTime": "11:00",
                "endTime": "12:00",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:00:33",
                "recordList": [
                    {
                        "id": "1627095720946601986",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555129412091906",
                        "itemDate": "2023-02-20",
                        "startTime": "11:00",
                        "endTime": "12:00",
                        "userId": "1606896022097960962",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "16",
                        "createTime": "2023-02-19 08:00:24",
                        "appUser": {
                            "id": "1606896022097960962",
                            "userName": "微信用户",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132",
                            "unionId": "oz6cFwBH9VIuzR9vjF9UWprgLB3Q",
                            "ref": "1501777218906775554",
                            "createTime": "2022-12-25 14:14:01",
                            "updateTime": "2022-12-25 14:14:19",
                            "subscribe": "false",
                            "realName": "龚莉",
                            "mobileNo": "17760782196"
                        }
                    },
                    {
                        "id": "1627123217063944193",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555129412091906",
                        "itemDate": "2023-02-20",
                        "startTime": "11:00",
                        "endTime": "12:00",
                        "userId": "1528559457955241986",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "48",
                        "createTime": "2023-02-19 09:49:40"
                    },
                    {
                        "id": "1627280640818057217",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555129412091906",
                        "itemDate": "2023-02-20",
                        "startTime": "11:00",
                        "endTime": "12:00",
                        "userId": "1570937481086046209",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "39",
                        "createTime": "2023-02-19 20:15:12"
                    }
                ],
                "join": true,
                "timeOut": false,
                "recordId": "1627280640818057217",
                "status": "open"
            },
            {
                "id": "1502555246575779841",
                "configId": "1502554985560047617",
                "startTime": "13:30",
                "endTime": "14:30",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:01:01",
                "recordList": [
                    {
                        "id": "1627102466670891009",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555246575779841",
                        "itemDate": "2023-02-20",
                        "startTime": "13:30",
                        "endTime": "14:30",
                        "userId": "1621840584536002561",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "6",
                        "createTime": "2023-02-19 08:27:12",
                        "appUser": {
                            "id": "1621840584536002561",
                            "userName": "微信用户",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132",
                            "unionId": "oz6cFwHb1wVLCUYmcMZBAvbNRH0M",
                            "ref": "1501781808466657282",
                            "createTime": "2023-02-04 19:58:22",
                            "updateTime": "2023-02-04 19:58:56",
                            "subscribe": "false",
                            "realName": "侯自有",
                            "mobileNo": "15886792133"
                        }
                    },
                    {
                        "id": "1627107229593444353",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555246575779841",
                        "itemDate": "2023-02-20",
                        "startTime": "13:30",
                        "endTime": "14:30",
                        "userId": "1505478649063862274",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "12",
                        "createTime": "2023-02-19 08:46:08"
                    },
                    {
                        "id": "1627228321271287810",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555246575779841",
                        "itemDate": "2023-02-20",
                        "startTime": "13:30",
                        "endTime": "14:30",
                        "userId": "1624304043471179777",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "5",
                        "createTime": "2023-02-19 16:47:18"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555296236339202",
                "configId": "1502554985560047617",
                "startTime": "14:30",
                "endTime": "15:30",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:01:13",
                "recordList": [
                    {
                        "id": "1627095649724080130",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555296236339202",
                        "itemDate": "2023-02-20",
                        "startTime": "14:30",
                        "endTime": "15:30",
                        "userId": "1533021237074903042",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "20",
                        "createTime": "2023-02-19 08:00:07",
                        "appUser": {
                            "id": "1533021237074903042",
                            "userName": "飘.",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83epicKBEmiarYlcUvpZTec1FnIac4WYrdHcBQomf1rm8ZBPWwV029Xd1AA8UAAXRcD9sGQlWvIjP77JA/132",
                            "unionId": "oz6cFwBDtt4TeluCW_aAILL9RbII",
                            "ref": "1501781808466657282",
                            "createTime": "2022-06-04 17:41:59",
                            "updateTime": "2022-06-04 17:42:26",
                            "subscribe": "false",
                            "realName": "郭文静",
                            "mobileNo": "19937870097"
                        }
                    },
                    {
                        "id": "1627171647324889090",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555296236339202",
                        "itemDate": "2023-02-20",
                        "startTime": "14:30",
                        "endTime": "15:30",
                        "userId": "1570754679529431042",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "9",
                        "createTime": "2023-02-19 13:02:06"
                    },
                    {
                        "id": "1627177400743006210",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555296236339202",
                        "itemDate": "2023-02-20",
                        "startTime": "14:30",
                        "endTime": "15:30",
                        "userId": "1559066090103574529",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "14",
                        "createTime": "2023-02-19 13:24:58"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555349250891777",
                "configId": "1502554985560047617",
                "startTime": "15:30",
                "endTime": "16:30",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:01:26",
                "recordList": [
                    {
                        "id": "1627095735053000706",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555349250891777",
                        "itemDate": "2023-02-20",
                        "startTime": "15:30",
                        "endTime": "16:30",
                        "userId": "1619698520906997761",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "10",
                        "createTime": "2023-02-19 08:00:27",
                        "appUser": {
                            "id": "1619698520906997761",
                            "userName": "微信用户",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132",
                            "unionId": "oz6cFwC6P334V1A3XEv-1FkSTtk8",
                            "ref": "1501781808466657282",
                            "createTime": "2023-01-29 22:06:34",
                            "updateTime": "2023-01-29 22:06:53",
                            "subscribe": "false",
                            "realName": "孟云飞",
                            "mobileNo": "18638922907"
                        }
                    },
                    {
                        "id": "1627096080361660417",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555349250891777",
                        "itemDate": "2023-02-20",
                        "startTime": "15:30",
                        "endTime": "16:30",
                        "userId": "1624654292257640449",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "1",
                        "createTime": "2023-02-19 08:01:50"
                    },
                    {
                        "id": "1627110875441864706",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555349250891777",
                        "itemDate": "2023-02-20",
                        "startTime": "15:30",
                        "endTime": "16:30",
                        "userId": "1619511995279810561",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "12",
                        "createTime": "2023-02-19 09:00:37"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            },
            {
                "id": "1502555393879736322",
                "configId": "1502554985560047617",
                "startTime": "16:30",
                "endTime": "17:30",
                "maxPerson": "3",
                "price": "",
                "remark": "",
                "createTime": "2022-03-12 16:01:36",
                "recordList": [
                    {
                        "id": "1627096444778614785",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555393879736322",
                        "itemDate": "2023-02-20",
                        "startTime": "16:30",
                        "endTime": "17:30",
                        "userId": "1575838202042454018",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "5",
                        "createTime": "2023-02-19 08:03:17",
                        "appUser": {
                            "id": "1575838202042454018",
                            "userName": "粟裕",
                            "userPic": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eobgOdDzqTWZ791lEIs0tjboEWdeh1P7dA3xYmPOmeFibPosNBSIR4QIOyQ0msjyXN3faicZu1flFicw/132",
                            "unionId": "oz6cFwEI85qBiVfCqY_w-qieJcog",
                            "ref": "1501777218906775554",
                            "createTime": "2022-09-30 21:21:19",
                            "updateTime": "2022-09-30 21:21:50",
                            "subscribe": "false",
                            "realName": "张成栋",
                            "mobileNo": "18837142713"
                        }
                    },
                    {
                        "id": "1627100661685719042",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555393879736322",
                        "itemDate": "2023-02-20",
                        "startTime": "16:30",
                        "endTime": "17:30",
                        "userId": "1573703087244337153",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "15",
                        "createTime": "2023-02-19 08:20:02"
                    },
                    {
                        "id": "1627111920150716418",
                        "appointId": "1501824148991008769",
                        "itemId": "1502555393879736322",
                        "itemDate": "2023-02-20",
                        "startTime": "16:30",
                        "endTime": "17:30",
                        "userId": "1601099088304312321",
                        "price": "",
                        "carManagerId": "1503315595447656449",
                        "remark": "",
                        "appointNum": "9",
                        "createTime": "2023-02-19 09:04:46"
                    }
                ],
                "join": false,
                "timeOut": false,
                "status": "open"
            }
        ],
        "config": {
            "id": "1502929669567438850",
            "appointId": "1501824148991008769", 
            "groupName": "卢教练夜班",
            "beforeHour": "16",
            "beforeHourStop": "3",
            "stopType": "again",
            "isMulti": "false",
            "maxSize": "1",
            "appointNum": "7",
            "customNum": "1-1",
            "carManagerIds": "1503315595447656449",
            "createTime": "2022-03-13 16:48:50",
            "updateTime": "2022-03-14 18:23:00",
            "joinTime": "2023-02-19 08:00:00",
            "join": true
        }
    }
}
```
### 取消预约接口
- 请求
```
url: 
    https://api.ccore.cc/record/delete?id=1627280038658609153 HTTP/1.1 GET
```
### 预约
- 请求 （可重复提交 只试了有名额的）
```
url:
https://api.ccore.cc/record/v2/saveOrUpdate POST
header:
    acces_token
form:
itemId=1502555129412091906&itemDate=2023-02-20&appointId=1501824148991008769&carManagerId=1503315595447656449&userId=
itemId 是greoup_list里的id
```
- 响应 01
```json
{"success":true,
"content":{
  "id":"1627271397554462722","appointId":"1501824148991008769","itemId":"1502555129412091906",
  "itemDate":"2023-02-20","startTime":"11:00","endTime":"12:00","userId":"1570937481086046209",
  "price":"","carManagerId":"1503315595447656449","remark":"","appointNum":"39","createTime":"2023-02-19 19:38:29"}}
```
- 响应02
```json
{
    "success": true,
    "content": {
        "?id": "删除时候的id",
        "id": "1627280038658609153", 
        "appointId": "1501824148991008769",
        "itemId": "1502555129412091906",
        "itemDate": "2023-02-20",
        "startTime": "11:00",
        "endTime": "12:00",
        "userId": "1570937481086046209",
        "price": "",
        "carManagerId": "1503315595447656449",
        "remark": "",
        "appointNum": "39",
        "createTime": "2023-02-19 20:12:49"
    }
}
```

