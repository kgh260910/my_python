from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

slow = [800, 800, 800]
fast = [100, 100, 100, 100, 100, 100]

def run_pattern(pin_obj, pattern_list, on=1):
    for ms in pattern_list:
        pin_obj.value(on)
        time.sleep_ms(ms)
        pin_obj.value(1 - on)
        time.sleep_ms(200)
        
run_pattern(flash, slow)
run_pattern(red, slow, 0)