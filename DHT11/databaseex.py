import sqlite3


def dbcreation() :
	temp =50
	hum =5
	dati = '1453-05-06 12:02:15 AM'
	conn = sqlite3.connect('/home/thecsr/Documents/Shubham/DHT11/db.sqlite')
	c = conn.cursor()
	c.execute('''
		CREATE TABLE sample(dati DATETIME , Temperature int , Humidity int)
''')

	c.execute("INSERT INTO sample(dati , Temperature , Humidity) values(?,?,?)",(dati,temp,hum))
	conn.commit()
	conn.close()

dbcreation()