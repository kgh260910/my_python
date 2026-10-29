from machine import Pin, PWM, Timer
import time

melody_buzzer = PWM(Pin(6, Pin.OUT), freq=100, duty=0)
melody_buzzer.duty(0)
ms_flag = False
time_cnt = 0

dutysound = 5    # 부저 소리 크기 
DO = 261
RE = 293
MI = 329
PA = 349
SOL = 392
RA = 440
SI = 493
DO_HIGH = 523

frequency_list = [DO, RE, MI, PA, SOL, RA, SI, DO_HIGH]
note_index = 0   # 몇 번째 음을 연주할지 지정하는 인덱스

def timer_callback(t):
    global ms_flag
    ms_flag = True

tmr = Timer(0)
tmr.init(period=1, mode=Timer.PERIODIC, callback=timer_callback)

try:
    while True:
        if ms_flag:
            ms_flag = False
            time_cnt += 1
            
            if time_cnt % 200 == 0:
                frequency = frequency_list[note_index]
                melody_buzzer.duty(dutysound) 
                melody_buzzer.freq(int(frequency))
                
                note_index += 1
                if note_index >= len(frequency_list):
                    note_index = 0
                    
            if time_cnt % 1000 == 0:
                time_cnt = 0


except:
    melody_buzzer.duty(0) 