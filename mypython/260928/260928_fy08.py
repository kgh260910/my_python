from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

leds = [flash, red]
print(len(leds))

leds[0].value(1)
leds[1].value(0)
time.sleep_ms(200)
leds[0].value(0)
leds[1].value(1)

