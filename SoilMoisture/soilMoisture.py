from machine import Pin, I2C, ADC
from time import sleep

AirValue = 664;   #you need to replace this value with Value_1
WaterValue = 435;  #you need to replace this value with Value_2

pot = ADC(0)
soilMoistureValue = 0
soilmoisturepercent = 0
 
def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
 
while True:
    
  soilMoistureValue = pot.read()
  #print(soilMoistureValue)
  sleep(0.1)
  
  soilmoisturepercent = map_range(soilMoistureValue, AirValue, WaterValue, 0, 100)
  
  if soilmoisturepercent > 100:
    print("100 %")
    sleep(2)
  
  elif soilmoisturepercent < 0:
    print("0 %")
  
  elif soilmoisturepercent >= 0 and soilmoisturepercent <= 100:
    print(soilmoisturepercent, "%")
    #print("%");
  
    sleep(2.5) 