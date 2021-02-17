import mysql.connector
cnx = mysql.connector.MySQLConnection(user='Mark', password='abc@1234', host='127.0.0.1', database='test')

cnx.close()