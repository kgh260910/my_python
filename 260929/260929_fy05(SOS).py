from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

UNIT = 150
I = [1, 1]
L = [1, 3, 1, 1]
O = [3, 3, 3]
V = [1, 1, 1, 3]
E = [1]
Y = [3, 1, 3, 3]
O = [3, 3, 3]
U = [1, 1, 3]

def send_morse(pin_obj, signals, unit):
    for s in signals:
        pin_obj.value(1)
        time.sleep_ms(s * unit)
        pin_obj.value(0)
        time.sleep_ms(unit)
        
send_morse(flash, I, UNIT)
time.sleep_ms(600)
send_morse(flash, L, UNIT)
time.sleep_ms(300)
send_morse(flash, O, UNIT)
time.sleep_ms(300)
send_morse(flash, V, UNIT)
time.sleep_ms(300)
send_morse(flash, E, UNIT)
time.sleep_ms(600)
send_morse(flash, Y, UNIT)
time.sleep_ms(300)
send_morse(flash, O, UNIT)
time.sleep_ms(300)
send_morse(flash, U, UNIT)
print("I love you 전송 완료")
        
        