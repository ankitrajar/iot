import urllib
import time
import string

url = "http://192.168.0.112/temp"

while True:
    try:
     opener = urllib.urlopen(url)
     data = opener.read()
     new_data = string.split(data," ")[-1]
     if( new_data < "20"):
         print "Temperature is cool! Temp : {}".format(new_data)
     elif((new_data >= "20") and (new_data <= "25")):
         print "Temperature is moderate! Temp : {}".format(new_data)
     else:
         print "Temperature is too high! Temp : {}".format(new_data)
     time.sleep(1)
    except:
     print "Press Ctrl+\ to Quit!"
