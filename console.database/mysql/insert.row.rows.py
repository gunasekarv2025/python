from mysql import connector

cn=connector.connect(host='localhost', port=3306, database='cmrdb', user='root', password='')

cr=cn.cursor()

qry1="""insert into ertbl(sname,m1,m2)values('x5',56.5,63)"""
qry2="""
insert into ertbl
(sname,m1,m2)
values
('x3',45.5,52),
('x1',36.5,43),
('x2',98,20),
('x4',61,63.5)
"""

try:
    cr.execute(qry1)
    print("\nOne row affected")
except Exception as e:
    print("\nError:",e)

try:
    cr.execute(qry2)
    cn.commit()
    print("\nAffected rows:",Cr.rowcount)
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

Error: name 'Cr' is not defined

Disconnect MySQL
'''
