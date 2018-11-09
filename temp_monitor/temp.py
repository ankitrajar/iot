import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","Pi Tempearture : "))

while True:
        print(measure_temp())
time.sleep(0.5)
