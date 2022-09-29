import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='TstwTdtct42'
                                     )

cursor = connection.cursor()

cursor.execute("DROP DATABASE `ETC_CARS`;")

cursor.close()
connection.close()
