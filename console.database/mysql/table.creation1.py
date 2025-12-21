from mysql import connector

cn=connector.connect(host='localhost', port=3306, database='cmrdb', user='root', password='')
cr=cn.cursor()

qry1=""" drop table if exists ertbl"""
qry2="""
create table if not exists ertbl
(
rno int primary key auto_increment,
sname varchar(5) not null,
m1 decimal(5,2) unsigned default 0,
m2 decimal(5,2) unsigned default 0,
total decimal(6,2) as (m1+m2),
average decimal(5,2) as (total/2),
result varchar(4) as (if(m1>34.4 and m2>34.4, 'Pass','Fail'))
)
auto_increment=1001
"""

try:
    cr.execute(qry1)
    print("\nErased 'ertbl' table")
except Exception as e:
    print("\nError:",e)

try:
    cr.execute(qry2)
    print("\nCreated 'ertbl' table")
except Exception as e:
    print("\nError:",e)

try:
    cr.close()
    cn.close()
    print('\nDisconnect Mysql')
except Exception as e:
    print("\nError:", e)
    
    
'''
output
Erased 'ertbl' table

Created 'ertbl' table

Disconnect Mysql
'''
