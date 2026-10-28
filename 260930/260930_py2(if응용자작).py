from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)


def blink_together(pin_obj, count):
    if pin_obj == red:
        ON = 0
        f = 1
    else:
        ON = 1
        f = 2
    while True:     
        pin_obj.value(ON)
        time.sleep_ms(250 * f)
        pin_obj.value(ON - 1)
        time.sleep_ms(250 * f)
        count += 1
        if count == 3 and pin_obj == flash:
            count = 0
            blink_together(red, 0)
        elif count == 3 and pin_obj == red:
            count = 0
            blink_together(flash, 0)
            
        

blink_together(flash, 0)
        
    
    