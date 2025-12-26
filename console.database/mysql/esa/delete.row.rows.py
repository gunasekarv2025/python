from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry1="""delete from esatbl where eid=1003"""
qry2="""delete from esatbl"""

try:
    cr.execute(qry1)
    print('\nErased one row')
except Exception as e:
    print("\nError.:",e)

try:
    cr.execute(qry2)
    cn.commit()
    print("\nErased",cr.rowcount,'Row(s)')
except Exception as e:
    print("\nError.:",e)

try:
    cr.close()
    cn.close()
    print("\nDisconnect MySQL")
except Exception as e:
    print("\nError.:",e)

'''
output
Erased one row

Erased 4 Row(s)

Disconnect MySQL
'''

    
