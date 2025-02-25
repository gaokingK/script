### 数据类型
- help create table 中data type中查看所有的
- 整型 bigint、int、mediumint、smallint 和 tinyint的取值范围
  - link: https://www.cnblogs.com/wayne173/p/3747477.html
  - 从小到大是 tinyint/smallint/mediumint/int/bight

- decimal
  - 据类型最多可存储 38 个数字，所有数字都能够放到小数点的右边。
  - decimal(10, 4) 一共能存10位数字，小数部分最多有4位。（多的化会四舍五入后把多出来的扔掉）
  - 定义了zerofill后，插入负数会报错
- datetime
  - 不能为空
    ``` 
    mysql> update autotest set kass_pro_date="" where id =3;
    ERROR 1292 (22007): Incorrect datetime value: '' for column 'kass_pro_date' at row 1
    ```
    - 不会发生时区转换
- timestamp
  - 存储范围是1970-01-01 00:00:01 UTC 到 2038-01-19 03:14:07 UTC。
  - 基于 UTC 存储的（即协调世界时间），它会根据当前系统时区进行转换。如果你输入的是一个时间字符串（比如 1970-01-01 08:00:00），MySQL 会自动将其转换为 UTC 时间并存储。
- varchar(128)可以存多少汉字
  - 4.0版本以下，varchar(50)，指的是50字节，如果存放UTF8汉字时，只能存16个（每个汉字3字节） 
  - 5.0版本以上，varchar(50)，指的是50字符，无论存放的是数字、字母还是UTF8汉字（每个汉字3字节），都可以存放50个

- TEXT 长文本字段，能存储64kb
- blob 长文本字段， 保存的是二进制，可以用来存储图片

### 
