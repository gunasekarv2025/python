from mysql import connector

cn=connector.connect(host='localhost',port=3306,database='cmrdb', user='root', password='')
cr=cn.cursor()

qry=""" select * from ertbl"""

try:
    cr.execute(qry)
    rows=cr.fetchall()
    print('NO.of columns:',len(rows[0]))
    print('No.of rows:',len(rows))
    print('\nFollowing row values...\n')

    for row in rows:
        print()
        for col in row:
            print(f'{col:<{10}}',end='')
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
NO.of columns: 7
No.of rows: 5

Following row values...


1001      x5        56.50     68.00     124.50    62.25     Pass      
1002      x3        45.50     57.00     102.50    51.25     Pass      
1003      x1        36.50     48.00     84.50     42.25     Pass      
1004      x2        59.00     75.00     134.00    67.00     Pass      
1005      x4        61.00     68.50     129.50    64.75     Pass
'''
