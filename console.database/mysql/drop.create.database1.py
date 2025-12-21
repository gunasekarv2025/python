from mysql import connector

cn=connector.connect(host='localhost', port=3306, database='',user='root', password='')
cr=cn.cursor()

try:
    cr.execute(""" drop database if exists cmrdb""")
    cr.execute("""create database if not exists cmrdb""")
    print('\nCreated new database')
except Exception as e:
    print('Error:',e)

cr.close()
cn.close()

'''
output
Created new database
'''
