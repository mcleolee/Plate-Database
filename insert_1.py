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