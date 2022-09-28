# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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


cursor.close()
connection.close()
