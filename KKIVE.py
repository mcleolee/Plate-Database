import os
import random
from concurrent.futures import ThreadPoolExecutor
import mysql.connector

city = '川'  # 更改城市
license_plates_list = set()  # 用来存储车牌号
random_num_list = set()  # 用来存储钱
car_num = 5000  # 用来存储多少量车


# 车辆号牌随机
def random_license_plate(c=city):
    plate = []
    s0 = 'ABDEFGH'
    s25 = '0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
    plate.append(f'{c}{random.choice(s0)}-')
    plate.append(str(random.randint(0, 9)))
    # 生成号牌第2～5位字符
    plate.append(''.join([random.choice(s25) for __i__ in range(5)]))
    return "".join(plate)


def random_num(star=10, to=10000):
    return random.randint(star, to)


def multiExecute(i):
    cursor.execute('insert into `all_cars` (plate, balance) values (%s,%s)',
                   (license_plates_list[i], random_num_list[i]))


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=os.cpu_count())
    license_plates_list = set(executor.submit(random_license_plate, city) for i in range(car_num))
    random_num_list = set(executor.submit(random_num) for i in range(car_num))

    '''检查长度是否合格'''
    if len(license_plates_list) < car_num:
        for i in range(car_num - len(license_plates_list)):
            license_plates_list.add(random_license_plate(city))
    if len(random_num_list) < car_num:
        for i in range(car_num - len(random_num_list)):
            random_num_list.add(random.randint(10, 10000))

    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         user='root',
                                         password='TstwTdtct42',
                                         database='ETC_CARS'
                                         )

    cursor = connection.cursor()
    
    for i in range(car_num):
        executor.submit(multiExecute, i)

    cursor.close()
    connection.commit()
    connection.close()