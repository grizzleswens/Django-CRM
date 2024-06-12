# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector, or mysql-connector-python


import mysql.connector

# Create a database connection
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Mashedpotatoes1!'
	)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All done creating database!")

