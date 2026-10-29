from machine import Pin
import time

flashW = Pin(4, Pin.OUT, value=0)
flashR = Pin(33, Pin.OUT, value=1)

def blink_together(good):
    flashW.value(1)
    flashR.value(0)
    time.sleep_ms(good)
    flashW.value(0)
    flashR.value(1)
    time.sleep_ms(good)
    
for i in range(3):
    blink_together(500)
    blink_together(100)