import os
import pymysql

# Get username from workspace
# (modify this variable if running on another environemnt)

# username = os.getenv('C9_USER') (not needed in GitPod)

connection = pymysql.connect(host='localhost', user='', password='', db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()