import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='TstwTdtct42',
                                     database='ETC_CARS'
                                     )

cursor = connection.cursor()

cursor.execute("SELECT * FROM `all_cars`;")

records = cursor.fetchall()
for r in records:
    print(r)

cursor.execute("\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A42853',320);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A42853',320);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A09568',536);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A235B3',76);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A23431',234);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川AER111',8753);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A66666',10);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川AAQ133',657);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A43000',8654);\
    INSERT INTO `all_cars` (plate, balance) VALUES ('川A54222',645);\
")



cursor.close()
connection.commit()
connection.close()
