import  mysql.connector

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456"   # 数据库密码
)

# print(mydb)

mycusor=  mydb.cursor()
# mycusor.execute('create database python_test')


mycusor.execute('show databases')

for x in mycusor:
    print(x)

print("OK!")
