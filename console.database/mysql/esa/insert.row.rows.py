from mysql import connector

cn=connector.connect(host='localhost',port='3306', database='cmrdb', user='root', password='')
cr=cn.cursor()

qry1="""insert into esatbl(ename,salary)values('x5',1600000)"""
qry2="""
insert into esatbl
(ename, salary)
values
('x1',600000),
('x4',800000), 
('x3',400000),
('x2',200000)
"""

try:
    cr.execute(qry1)
    print("\nOne row affected")
except Exception as e:
    print("\nError:",e)

try:
    cr.execute(qry2)
    cn.commit()
    print("\nAffected rows:",cr.rowcount)
except Exception as e:
    print("\nError:",e)

try:
    cr.close()
    cn.close()
    print('\nDisconnect MySQL')
except Exception as e:
    print("\nnError:",e)

'''
output
One row affected

Affected rows: 4

Disconnect MySQL
'''




