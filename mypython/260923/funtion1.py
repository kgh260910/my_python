from machine import Pin
import time

flashW = Pin(4, Pin.OUT, value=0)
flashR = Pin(33, Pin.OUT, value=1)

def blink_red(msg):
    flashR.value(0)
    time.sleep_ms(msg)
    flashR.value(1)
    time.sleep_ms(msg)
def blink_white(hope):
    flashW.value(1)
    time.sleep_ms(hope)
    flashW.value(0)
    time.sleep_ms(hope)

for i in range(3):
    blink_red(1000)
    blink_white(1000)
    blink_red(100)
    blink_white(100)
