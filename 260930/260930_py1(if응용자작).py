from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

flash_step = [900, 800, 700, 600, 500]
red_step = [600, 400, 600, 400]

def blink_together(pin_obj, pattern_list):
    if pin_obj == red:
        ON = 0       
    else:
        ON = 1
        
    for ms in pattern_list:
        pin_obj.value(ON)
        time.sleep_ms(1000 - ms)
        pin_obj.value(ON - 1)
        time.sleep_ms(200)
    if pin_obj == flash:
        blink_together(red, red_step)
    else:
        blink_together(flash, flash_step)
        

blink_together(flash, flash_step)
        