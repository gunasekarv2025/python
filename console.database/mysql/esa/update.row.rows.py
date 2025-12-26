from mysql import connector

cn=connector.connect(host='localhost', port=3306, database='cmrdb', user='root', password='')
cr=cn.cursor()

qry1="""update esatbl set salary=(salary-300000) where eid=1004"""
qry2="""
update esatbl set salary=(salary+500000)"""

try:
    cr.execute(qry1)
    print("\nOne row affected")
except Exception as e:
    print("\nError.:",e)

try:
    cr.execute(qry2)
    cn.commit()
    print("\nAffected rows:",cr.rowcount)
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
One row affected

Affected rows: 5

Disconnect MySQL
'''
