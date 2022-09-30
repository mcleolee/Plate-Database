# Plate-Database

## 看这里！如何使用这玩意
1. 安装MySQL
2. 创建一个 MYSQL 链接，参数最好是：
   1. `host: localhost`
   2. `user: root `
   3. `port: 3306`
3. 密码记好，要用
4. 配置代码我贴心的写在了每个程序前面，按你的配置填进去
5. 如果要运行多个文件要给权限，有点麻烦，运行 AUTOPILOT.py 进行一键配置
6. 如果你需要自己调试，参考下面的步骤
   1. 运行 `Init_database.py` 以初始化
   2. 运行 `plate_generator.py` 以插入车牌
   3. 运行 `Select_data.py` 以查看车牌数据
   4. 运行 `Show_database.py` 以检查所有 DATABASE
   5. 运行 `get_poor_people.py` 以获取余额低于 200 元的车辆
   6. 如果要删除所有 DATABASE 和 TABLE, 那么运行 `DELETE.py`
7.  表里会生成 5000 条四川的车牌和余额，ic 的所有数据为 NULL


如果要在 C 语言里使用 python 脚本，我很贴心的把所有依赖放进去了
记得加 `#include "Python.h"`
具体看这个链接：
[我是链接](https://blog.csdn.net/zhangdell/article/details/121661409?ops_request_misc=&request_id=&biz_id=102&utm_term=在%20c%20里调用python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-121661409.142^v50^control,201^v3^control_2&spm=1018.2226.3001.4449)

1. 把群里的 CSV 文件下载到板子上，或者点这里下载
2. 安装好 mysql 后：
3. 进入：mysql -u root -p

[all_cars.csv](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca96295d-7cb3-473e-b7c4-a6bade7c454b/all_cars.csv)

以下为 MySQL 语句：

1. `CREATE DATABASE ETC_CARS;`
2. `USE ETC_CARS;`
3. 如下
    
    ```
    CREATE TABLE all_cars(
            `ic`		VARCHAR(128),
            `plate`		VARCHAR(30) UNIQUE,
            `balance`	INT,
            PRIMARY KEY (`plate`)
        );
    ```
    
4. 加载 CSV 文件
    
    ```sql
    # 写板子里的路径！
    LOAD DATA INFILE '/home/test/ip_location.csv'
    INTO TABLE all_cars
    CHARACTER SET utf8
    FIELDS TERMINATED BY ',' ENCLOSED BY '';
    
    # 这是一个语句！
    ```
    
5. 用 `select * from all_cars;` 检查有没有数据