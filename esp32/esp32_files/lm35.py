from microWebSrv import MicroWebSrv
from machine import Pin
from machine import ADC

#Setup analog pin for reading sensor data
sensor = ADC(Pin(36))

@MicroWebSrv.route('/temp','GET')
def _httpHandlerTEMPGet(httpClient, httpResponse):
    try:
        temp = sensor.read()
        temp_data = (temp/1400)*5000
        actual_temp = temp_data - 14
        data = actual_temp
    except:
        data = 'Attempting to read Sensor...'

    httpResponse.WriteResponseOk(
            headers = ({'Cache-Control': 'no-cache'}),
            contentType = 'text/event-stream',
            contentCharset = 'UTF-8',
            content = 'data: {0}\n\n'.format(data))
    
srv = MicroWebSrv(webPath='/www/')
srv.Start(threaded=False)
