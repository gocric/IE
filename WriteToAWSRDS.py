import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host='database-1-instance-1.cm2ifkcsaq9w.us-east-2.rds.amazonaws.com',
                     database='IE',
                     user='admin',
                     password='gokul123')

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PDFData ( FILE, DATA ) VALUES ( 'g','G' ) ")
        conn.commit()
except Exception as e:
    print ("Print your error msg", e)
finally:
    #closing database connection.
    if(conn.is_connected()):
       cursor.close()
       conn.close()
