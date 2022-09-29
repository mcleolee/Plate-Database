import os,os.path
import string,base64

def main():
    f=open("insertData.sql",'w')
    i=1
    while i<10:
       strI=str(i)
    sql="insert into t_admin values\
    ('"+strI+"',            \
    "+"'username"+strI+"',  \
    "+"'password"+strI+"',  \
    "+"'name"+strI+"',      \
    '"+"1',                 \
    "+"'introduce"+strI+"');"
f.write(sql +"\n")
print(sql)
i=i+1
f.close()

if __name__=='__main__':
    main()

# sql
SELECT * FROM all_cars;
USE ETC_CARS;
SHOW DATABASES;
USE ETC_CARS;
SELECT * FROM `all_cars`;
/*循环插入*/
DELIMITER //
CREATE PROCEDURE callback()
BEGIN
  DECLARE num INT;
  SET num = 100;
  WHILE
    num < 150 DO INSERT INTO all_cars(balance)
    VALUES(RAND() * 10000);
    SET num = num + 1;
  END WHILE;
END; 
//

DROP table all_cars;
# DESCRIBE `all_cars`;
# INSERT INTO `all_cars` (balance) VALUES (1000*rand(),0);

(select concat((select(
	CASE
		WHEN
			 ceiling(rand()*25) % 2 = 0
			THEN ceiling(rand()*9)
			ELSE
(select(
 CASE
		WHEN
			(65+ceiling(rand()*25)) < 73
			THEN char(65+abs(ceiling(rand()*9)-2))
		WHEN
			(65+ceiling(rand()*25)) > 73 AND (65+ceiling(rand()*25)) < 79
			THEN char(73+abs(ceiling(rand()*9)-4))
		ELSE
			char(79+ceiling(rand()*11))
		END))
			END)),(select(
	CASE
		WHEN
			 ceiling(rand()*25) % 2 = 0
			THEN ceiling(rand()*9)
			ELSE
(select(
 CASE
		WHEN
			(65+ceiling(rand()*25)) < 73
			THEN char(65+abs(ceiling(rand()*9)-2))
		WHEN
			(65+ceiling(rand()*25)) > 73 AND (65+ceiling(rand()*25)) < 79
			THEN char(73+abs(ceiling(rand()*9)-4))
		ELSE
			char(79+ceiling(rand()*11))
		END))
			END)),(select(
	CASE
		WHEN
			 ceiling(rand()*25) % 2 = 0
			THEN ceiling(rand()*9)
			ELSE
(select(
 CASE
		WHEN
			(65+ceiling(rand()*25)) < 73
			THEN char(65+abs(ceiling(rand()*9)-2))
		WHEN
			(65+ceiling(rand()*25)) > 73 AND (65+ceiling(rand()*25)) < 79
			THEN char(73+abs(ceiling(rand()*9)-4))
		ELSE
			char(79+ceiling(rand()*11))
		END))
			END)),(select(
	CASE
		WHEN
			 ceiling(rand()*25) % 2 = 0
			THEN ceiling(rand()*9)
			ELSE
(select(
 CASE
		WHEN
			(65+ceiling(rand()*25)) < 73
			THEN char(65+abs(ceiling(rand()*9)-2))
		WHEN
			(65+ceiling(rand()*25)) > 73 AND (65+ceiling(rand()*25)) < 79
			THEN char(73+abs(ceiling(rand()*9)-4))
		ELSE
			char(79+ceiling(rand()*11))
		END))
			END)),(select(
	CASE
		WHEN
			 ceiling(rand()*25) % 2 = 0
			THEN ceiling(rand()*9)
			ELSE
(select(
 CASE
		WHEN
			(65+ceiling(rand()*25)) < 73
			THEN char(65+abs(ceiling(rand()*9)-2))
		WHEN
			(65+ceiling(rand()*25)) > 73 AND (65+ceiling(rand()*25)) < 79
			THEN char(73+abs(ceiling(rand()*9)-4))
		ELSE
			char(79+ceiling(rand()*11))
		END))
			END))))





