# Plate-Database

## 看这里！如何使用这玩意
1. 安装MySQL
2. 创建一个 MYSQL 链接，参数最好是：
   1. `host: localhost`
   2. `user: root `
   3. `port: 3306`
3. 密码记好，要用
4. 配置代码我贴心的写在了每个程序前面，按你的配置填进去
5. 运行 `Init_database.py` 以初始化
6. 运行 `plate_generator.py` 以插入车牌
7. 运行 `Select_data.py` 以查看车牌数据
8. 运行 `Show_database.py` 以检查所有 DATABASE
9. 表里会生成 5000 条四川的车牌和余额，ic 的所有数据为 NULL
10. 如果要删除所有 DATABASE 和 TABLE ,
    那么运行 `DELETE.py`
    
如果要在 C 语言里使用 python 脚本，我很贴心的把所有依赖放进去了
记得加 `#include "Python.h"`
具体看这个链接：
[我是链接](https://blog.csdn.net/zhangdell/article/details/121661409?ops_request_misc=&request_id=&biz_id=102&utm_term=在%20c%20里调用python&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-121661409.142^v50^control,201^v3^control_2&spm=1018.2226.3001.4449)


