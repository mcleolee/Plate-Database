import random
from venv import create
import mysql.connector

# def init():
    
    

def create(connection):
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE `ETC_CARS`;")
    cursor.execute("USE `ETC_CARS`;")

    cursor.execute("CREATE TABLE all_cars(  \
        `ic`		VARCHAR(128),           \
        `plate`		VARCHAR(30) UNIQUE,     \
        `balance`	INT,                    \
        PRIMARY KEY (`plate`)               \
    );                                      \
    ")

    cursor.close()
    connection.close()

def execute(connection):
    cursor = connection.cursor()

    for i in range(0, len(license_plates)):
        cursor.execute('insert into `all_cars` (plate, balance) values (%s,%s)',(license_plates[i],random_num_list[i]))

    cursor.close()
    connection.commit() 
    connection.close()


def license_plate(s):
    '''车辆号牌随机'''
    plate = [] #号码字符结构列表
    #号牌字头字母选择字符串
    s0 = 'ABDEFGH'
    #第2～5位选择字符串
    s25 = '0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
    #生成号牌字头
    plate.append(f'{s}{random.choice(s0)}-')
    #第一位数字
    plate.append(str(random.randint(0, 9)))
    #生成号牌第2～5位字符
    plate.append(''.join([random.choice(s25) for i in range(5)]))
    return ''.join(plate)

def select(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM `all_cars`;")
    records = cursor.fetchall()
    for r in records:
        print(r)


    cursor.close()
    connection.close()

if __name__=='__main__':
    # init()
    connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='TstwTdtct42',
                                     # database='ETC_CARS'
                                     )
    create(connection)
    city = '川' #更改城市
    license_plates = [] #用来存储车牌号 这一行和下一行用set()来避免重复，但是不能用append()，要add()
    random_num_list = [] #用来存储钱
    for i in range(5000):
        # s = f'{(i+1):3d}. {license_plate(city)}'
        random_num = random.randint(10,10000)
        s = license_plate(city)
        license_plates.append(s)
        random_num_list.append(random_num)
        '''车牌号输出'''
        # s = f'{s}' + '\', '
        # front = '  INSERT INTO `all_cars` (plate, balance) VALUES (\'' + f'{s}' + str(random_num) + ');'
        # print(front)
    execute(connection)
    select(connection)


    