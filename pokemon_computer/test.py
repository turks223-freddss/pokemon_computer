import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="turks2002",
    auth_plugin='mysql_native_password',
    database="Poke_computer")

mycursor = db.cursor()

