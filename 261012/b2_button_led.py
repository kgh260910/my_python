from machine import Pin
import time

btn = Pin(0, Pin.IN, Pin.PULL_UP)       # 누르면 0  기본상태High
flash = Pin(4, Pin.OUT, value=0)        # 플래시 LED: 1 이 켜짐 (매우 밝다, 직시 금지)

try:
    while True:
        flash.value(1 - btn.value())  # 누르면 0 → 1(켜짐), 떼면 1 → 0(꺼짐)
        time.sleep_ms(10)             # 바운스가 생기기 때문에 넣어준다.
except KeyboardInterrupt:
    flash.value(0)
    print("종료")
