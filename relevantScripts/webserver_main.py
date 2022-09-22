# For more details and step by step guide visit: Microcontrollerslab.com
try:
  import usocket as socket
except:
  import socket
  
from machine import Pin, I2C, ADC
from time import sleep
from bme680 import *

import test_pythonScript


####
# import all the necessary scripts for the components
####
import soilMoisture
from soilMoisture import soilmoisturepercent
soilMoisturePercent = soilMoisture.soilmoisturepercent;

import bmeInit
import relayWater


led_state = "OFF"
led = Pin(2, Pin.OUT)


def web_page():
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }
        
        .switch{
            position:relative;
            display:inline-block;
            width:120px;
            height:68px
        }
        .switch input{
            display:none
        }
        .slider{
            position:absolute;
            top:0;
            left:0;
            right:0;
            bottom:0;
            background-color: #ccc;
            border-radius:34px
        }
        .slider:before{
            position:absolute;
            content:"";
            height:52px;
            width:52px;
            left:8px;
            bottom:8px;
            background-color:#fff;
            -webkit-transition:.4s;
            transition:.4s;
            border-radius:68px
        }
        input:checked+.slider{
            background-color:#2196F3
        }
        input:checked+.slider:before{
            -webkit-transform:translateX(52px);
            -ms-transform:translateX(52px);
            transform:translateX(52px)
        }
        
    </style>
</head>

<script>

    function toggleCheckbox(element) {
        var xhr = new XMLHttpRequest(); 
        if(element.checked){
            xhr.open("GET", "/?led_2_off", true);
        }
        else {
            xhr.open("GET", "/?led_2_on", true);
        }
        xhr.send();
    }
    
    function toggleSwitch(element) {
        var xhr = new XMLHttpRequest(); 
        if(element.checked){
            xhr.open("GET", "/?relay=on", true);
        }
        else {
            xhr.open("GET", "/?relay=off", true);
        }
        xhr.send();
    }
</script>

<body>
    <h2>Plant6 - Web Server</h2>
    <h3>To check the connection</h3>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"?led_2_on\"><button class="button">LED ON</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"?led_2_off\"><button class="button button1">LED OFF</button></a>
    </p>

    <p>Turn On/Off the Light</p>
    <label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" %s><span
         class="slider">
    
    
    <p>
        <i class="fa-thin fa-droplet-percent"></i>
        Soil Moisture: <strong>""" + str(soilMoisturePercent) + "%" + """</strong>
    </p>
    
    
    <p>
        <i class="fa-light fa-temperature-list"></i>
         Humidity: <strong><i>""" + str(bmeInit.hum) + """</i></strong>
    </p>
    
    <p>
        <i class="fa-light fa-temperature-list"></i>
        Temperature: <strong><i>""" + str(bmeInit.temp) + """</i></strong>
    </p>
    
    <p>Pressure: <strong><i>""" + str(bmeInit.pres) + """</i></strong></p>
    
    <p>Gas: <strong>""" + str(bmeInit.gas) + """</strong></p>
</body>

</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def startMeassuring():
    #hier dann noch den ganzen anderen code aus der while True schleife
    hi = "hi"
        
        
        
def checkSoilMeassure():
    print("HIER DRINNEN")
    soilMoistureNUM = soilMoisture.calcSoilMoistureValue()
    if(40 <= soilMoistureNUM < 50):
        print("ist unter 50%")
        relayWater.openRelay(10)
        
    elif(30 <= soilMoistureNUM < 40):
        print("ist unter 40%")
        relayWater.openRelay(20)
    
    elif(20 <= soilMoistureNUM < 30):
        print("ist unter 30%")
        relayWater.openRelay(30)
    
    elif(soilMoistureNUM < 20):
        print("ist unter 20%")
        relayWater.openRelay(5)
    
    else:
        print("Die Bodenfeuchtigkeit ist gut!") 
    

def switchLightState():
    print("Hier drin") 



while True:
    startMeassuring();
    #test_pythonScript.doSomething();
        
    ######
    # Below is everything related to the soil Moisture
    ######
    #print("Soil Moisture Values:")
    
    soilMoisturePercent = str(soilMoisture.calcSoilMoistureValue())
    
    #print("--- Soil Moisture End ---")
        
    ######
    # Below is everything related to the BME
    ######
    print("BME Values:")
    bmeInit.calcBMEvalues()

    print("Humidity: " + str(bmeInit.hum))
    print("Pressure: " + str(bmeInit.pres))
    print("Gas: " + str(bmeInit.gas))
    print("Temperature: " + str(bmeInit.temp))
    
    print("--- BME End ---")
        
    ######
    # Below is everything related to the LED
    ######
    print("Hier der stuff für die LEDS")
    
    ##### LOGIC - START #####
    
    #check if the meassurement of the soil is too low and based on this open the relay
    soilMoistureNUM = soilMoisture.calcSoilMoistureValue();
    #checkSoilMeassure();
    
    #call to turn on/off the lights
    switchLightState();
    
    ##### LOGIC - END #####
    
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        
        #this one for the relay with the LED
        #get called by the function toggleSwitch in the script-tag of the html
        """
        relay_on = request.find('/?relay=on')
        relay_off = request.find('/?relay=off')
        if relay_on == 6:
          print('RELAY ON')
          #Hier dann die relay-Funktion aufrufen
          relay.value(0)
        if relay_off == 6:
          #Hier dann die relay-Funktion aufrufen
          print('RELAY OFF')
          relay.value(1)
        """
        
        #this one to test the led on the esp
        #get called by the function toggleCheckbox in the script tag of the html => gets replaced by the one above
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        if led_on == 6:
            print('LED ON -> GPIO2')
            led_state = "ON"
            led.on()
        if led_off == 6:
            print('LED OFF -> GPIO2')
            led_state = "OFF"
            led.off()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
        
        sleep(5) 
        
    except OSError as e:
        conn.close()
        print('Connection closed')
        