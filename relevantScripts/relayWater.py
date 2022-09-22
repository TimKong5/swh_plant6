from machine import Pin
from time import sleep

relay = Pin(14, Pin.OUT) #ist D5 beim esp8266
#schwarz in G
#braun in D5
#weiß in VU

#test if 0 or 1 is openning the relay
#bei 0 fließt dieses Wasser
def openRelay(x):
    relay.value(0)
    print(x)
    print("relay geöffnet")
    sleep(x)
    closeRelay(); 
    
def closeRelay():
    relay.value(1)
    print("relay geschlossen")
