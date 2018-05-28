import MySQLdb
from faker import Faker

#connect to db
db = MySQLdb.connect("localhost","root","123456","myflaskapp" )
 
fake = Faker()

#setup cursor
cursor = db.cursor()
 
#insert to table
try:
	for x in range(11111):
		name = fake.name()
		email = fake.email()
		username = fake.last_name()
		password = fake.password()

		cursor.execute("INSERT INTO users2(name, email, username, password) VALUES(%s, %s, %s, %s) ", (name, email, username, password))

	db.commit()
except:     
	db.rollback()

db.close()
