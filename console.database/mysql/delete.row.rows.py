from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry1="""delete from ertbl where rno=1003"""
qry2="""delete from ertbl"""

try:
    cr.execute(qry1)
    print("\nError.:",e)
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
    print("\nErro.:",e)

'''
output

Erased One row

Erased 0 Row(s)

Disconnect MySQL
'''
    
