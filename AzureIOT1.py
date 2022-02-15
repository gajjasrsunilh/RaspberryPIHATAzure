import time  
from azure.iot.device import IoTHubDeviceClient, Message
from sense_hat import SenseHat
from datetime import datetime
  
Change Connection String
CONNECTION_STRING = "HostName=SunilIOTTryHub.azure-devices.net;DeviceId=SunilIOTTryRaspberryPI4;SharedAccessKey=+SwmR7128NwKtZQ="  
  
sense = SenseHat()
sense.clear()
now = datetime.now()
pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity = sense.get_humidity()
MSG_TXT = '{{"TimeStamp": {now}, Temperature": {temp},"Humidity": {humidity},"Pressure": {pressure}}}'  
  
def SendAzureTelemetryDataInit():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def SendAzureTelemetryData():  
  
    try:  
        client = SendAzureTelemetryDataInit()  
        
        while True:  
            now = datetime.now()
            pressure = sense.get_pressure()
            temp = sense.get_temperature()
            humidity = sense.get_humidity()
            
            msg_txt_formatted = MSG_TXT.format(now=now,temp=temp, humidity=humidity, pressure = pressure)  
            message = Message(msg_txt_formatted)  
  
            if temp > 30:  
              message.custom_properties["temperatureAlert"] = "true"  
            else:  
              message.custom_properties["temperatureAlert"] = "false"  
  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(5)  
  
    except KeyboardInterrupt:  
        print ( "Stopped..." )
        
        
print ( "SunilGajjarIOTTry - Let's learn new skill" )  
print ( "Press Ctrl-C to exit" )  
SendAzureTelemetryData()
    
    
