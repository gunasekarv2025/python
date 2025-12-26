from mysql import connector

cn=connector.connect(host='127.0.0.1', port='3306', database='cmrdb', user='root',password='')
cr=cn.cursor()

qry1="""drop table if exists esatbl"""
qry2="""
create table if not exists esatbl
(
eid int primary key auto_increment,
ename varchar(5) not null,
salary decimal(12,2) unsigned not null,
hra decimal(10,0) as(salary*15/100),
da decimal(10,2) as(salary*20/100),
pf decimal(10,2) as(salary*35/100),
gp decimal(10,2) as(salary+hra+da),
np decimal(10,2) as(gp-pf)
)auto_increment=1001;
"""

try:
    cr.execute(qry1)
    print("\nErased 'esatbl' table")
except Exception as e:
    print('\nError:',e)

try:
    cr.execute(qry2)
    print("\nCreated 'esatbl' table")
except Exception as e:
    print('\nError:',e)

try:
    cr.close()
    cn.close()
    print("\nDisconnect mysql")
except Exception as e:
    print('\nError:',e)

'''
outpt
Erased 'esatbl' table

Created 'esatbl' table

Disconnect mysql
'''
