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

cursor.execute(" ")


cursor.close()
connection.commit() 
connection.close()
