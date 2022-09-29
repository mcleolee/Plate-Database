import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='TstwTdtct42',
                                     database='ETC_CARS'
                                     )

cursor = connection.cursor()

cursor.execute("select plate from all_cars where balance < 200;")

records = cursor.fetchall()
for r in records:
    print(r)


cursor.close()
connection.close()
