# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='TstwTdtct42'
                                     # database='xxx'
                                     )

cursor = connection.cursor()
# cursor.execute("DROP DATABASE `test`;")
# CREATE  DATABASE `ETC_CARS`;
# USE `ETC_CARS`;
# CREATE TABLE all_cars(
# 	`ic`		VARCHAR(128),
#     `plate`		VARCHAR(30) UNIQUE,
#     `balance`	INT,
#     PRIMARY KEY (`plate`)
# );


cursor.close()
connection.close()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
