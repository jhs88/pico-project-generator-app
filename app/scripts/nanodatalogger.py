import machine
from machine import Pin
import time

adc_pin = machine.Pin(29) 
adc = machine.ADC(adc_pin)
led = Pin(6, Pin.OUT)
readings = 0

# create a file named "data.csv"
file=open("data.csv","w") 
file.write("data"+"\n")

while True:
    
    led.value(1)
    reading = adc.read_u16()     
    print("ADC: ",reading)
    
    time.sleep_ms(100)
    
    # convert and write the reading from the analog pin
    file.write(str(reading)+"\n")
    
    led.value(0)
    time.sleep_ms(100)
    readings += 1
    
    # if 25 readings are done, finish the program
    if readings >= 25:
        file.close()
        break