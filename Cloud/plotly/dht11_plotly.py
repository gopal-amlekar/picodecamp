import sys
sys.path.append('../../')   # Must follow the folder structure or else change the path
from devices.temperature_humidity_sensors import dht11

#Import other required modules
import plotly.plotly as myplot
import json
import time
import datetime

##### Read config.json #####
with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

myplot.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = myplot.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Temp Values')

print ("View your streaming graph here: {0}".format(url))

# open stream to write sensor values to given streaming token.
stream = myplot.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()


# Read DHT11 temperature data
DHT_SignalPin = 14      # GPIO 14 (BCM mode)
DHT11_Sensor = dht11.DHT11(pin = DHT_SignalPin)

#the main sensor reading and plotting loop
while True:
    result = DHT11_Sensor.read()
    temp_C = result.temperature
    print ("Temperature: {0} degrees".format(temp_C))

    # write the data to plotly
    stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(10)
