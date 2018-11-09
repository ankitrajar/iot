import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","Core Temperature : "))

while True:
        print(measure_temp())
        time.sleep(1)
#Sleep outside while will cause load average to increase significantly
