from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb', user='root', password='')
cr=cn.cursor()

qry="""select *from esatbl"""

try:
    cr.execute(qry)
    rows=cr.fetchall()
    print('NO.of columns:',len(rows[0]))
    print('No.of rows:',len(rows))
    print('\nFollowing row values...\n')

    for row in rows:
        print()
        for col in row:
            print(f'{col:<{15}}',end='')
except Exception as e:
    print("\nError.:",e)

try:
    cr.close()
    cn.close()
    print('\nDisconnect MYSQL')
except Exception as e:
    print("\nError:",e)

'''
output
NO.of columns: 8
No.of rows: 5

Following row values...


1001           x5             2100000.00     315000         420000.00      735000.00      2835000.00     2100000.00     
1002           x1             1100000.00     165000         220000.00      385000.00      1485000.00     1100000.00     
1003           x4             1300000.00     195000         260000.00      455000.00      1755000.00     1300000.00     
1004           x3             600000.00      90000          120000.00      210000.00      810000.00      600000.00      
1005           x2             700000.00      105000         140000.00      245000.00      945000.00      700000.00      
Disconnect MYSQL
'''
