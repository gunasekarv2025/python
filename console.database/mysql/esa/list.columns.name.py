from mysql import connector

cn=connector.connect(host='127.0.0.1',port=3306,database='cmrdb',user='root',password='')
cr=cn.cursor()

qry="""select column_name from information_schema.columns
where table_schema=database() and table_name='esatbl'"""

try:
    cr.execute(qry)
    rows=cr.fetchall()
    print('No.of columns:',len(rows[0]))
    print('No.of rows:',len(rows))
    print('\nFollowing rows values...)')

    for row in rows:
        print()
        for col in row:
            print(col)

except Exception as e:
    print('\nError.:',e)


try:
    cr.close()
    cn.close()
    print('\nDisconnect MySQL')
except Exception as e:
    print('\nError.:')

'''
output
No.of columns: 1
No.of rows: 8

Following rows values...)

eid

ename

salary

hra

da

pf

gp

np

Disconnect MySQL
'''
