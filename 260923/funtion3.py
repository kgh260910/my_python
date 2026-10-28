from machine import Pin
import time

flashR = Pin(33, Pin.OUT, value=1)

ON = 0
OFF = 1

def blink_red(times, ms_on, ms_off):
    for i in range(times):
        flashR.value(ON)
        time.sleep_ms(ms_on)
        flashR.value(OFF)
        time.sleep_ms(ms_off)
        
blink_red(5, 1000, 100)