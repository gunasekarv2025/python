'''
Title: How to develop mysql using python console application?
'''

from mysql import connector

cn=connector.connect(host='127.0.0.1',port=3306,database='',user='root',password='')
cr=cn.cursor()

cr.execute("""show databases""")

for dn in cr:
    print(dn[0])


cn.close()


'''
output
cmrdb
information_schema
mysql
performance_schema
phpmyadmin
test
'''
