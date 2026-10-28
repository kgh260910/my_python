from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)
counter = 0

while True :
    flash.value(1)
    time.sleep_ms(1)
    flash.value(0)
    time.sleep_ms(25)
    counter += 1
    
    if counter == 100 :
        flash.value(0)
        time.sleep_ms(200)
        counter = 0
        flash.value(1)
        red.value(0)
        time.sleep_ms(1000)
        flash.value(0)
        red.value(1)
    
