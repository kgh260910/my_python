from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

b = 0
flag_red = 0

while True :
    flash.value(1)       # 4번 핀에 HIGH(1) Signal을 보내 LED를 켭니다.
    if flag_red == 1:
        red.value(0)
    time.sleep_ms(100)
    
    flash.value(0)       # 4번 핀에 LOW(0) Signal을 보내 LED를 켭니다.
    if flag_red == 1:
        red.value(1)
        flag_red = 0
    time.sleep_ms(100)
    
    b += 1
    if(b % 3 == 0):
        flag_red = 1
    
