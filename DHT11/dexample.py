import RPi.GPIO as GPIO
import dht11
import time
import datetime
from databaseex.py import *

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

conn = sqlite3.connect('/home/thecsr/Documents/Shubham/DHT11/raspdata.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE raspdata(dati DATETIME , Temperature int , Humidity int)''')


# read data using pin 14
instance = dht11.DHT11(pin=14)

for i in range(10):
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        c.execute("INSERT INTO raspdata(dati , Temperature , Humidity) values(?,?,?)",(datetime.datetime.now(),result.temperature,result.humudity))
        conn.commit()
        


    time.sleep(2)
conn.close()
