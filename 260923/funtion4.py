from machine import Pin
import time

flashR = Pin(33, Pin.OUT, value=1)
R_ON = 0
R_OFF = 1

flashW = Pin(4, Pin.OUT, value=0)
W_ON = 1
W_OFF = 0

def blink_together(times, ms_on, ms_off):
    for i in range(times):
        flashR.value(R_ON)
        flashW.value(W_ON)
        time.sleep_ms(ms_on)
        flashR.value(R_OFF)
        flashW.value(W_OFF)
        time.sleep_ms(ms_off)

blink_together(3, 500, 100)