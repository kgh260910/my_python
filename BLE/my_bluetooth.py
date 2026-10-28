import bluetooth, time, bluetooth,ble_simple_peripheral
from machine import Pin, PWM, Timer

NAME = "DW502-김건희"           # ★ 내 이름으로 바꾼다 (예: CAM-DW502-홍길동, 한글 5글자까지)
btn = Pin(0, Pin.IN, Pin.PULL_UP)               # 누르면 0
                                 # 약한 밝기
M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)
M2_motor = PWM(Pin(5), freq = 10000 ,duty=0)
M3_motor = PWM(Pin(40), freq = 10000 ,duty=0)
M4_motor = PWM(Pin(41), freq = 10000 ,duty=0)

# ── 블루투스: 보드→폰(TX) 통로와 폰→보드(RX) 통로를 둘 다 만든다 ──
UART = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
TX = (bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_NOTIFY)
RX = (bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"),
      bluetooth.FLAG_WRITE | bluetooth.FLAG_WRITE_NO_RESPONSE)
SERVICE = (UART, (TX, RX))

ble = bluetooth.BLE()
ble.active(True)
((tx_handle, rx_handle),) = ble.gatts_register_services((SERVICE,))


conn = None
command = ""                                    # 폰이 보낸 글자를 적어 두는 포스트잇
flag_10ms = False
isr_cnt = 0

def on_rx(read):
    print("RX", read)
    M1_motor.duty(read)
    M2_motor.duty(read)
    M3_motor.duty(read)
    M4_motor.duty(read)

def make_payload(name):
    n = name.encode()
    return bytes([2, 0x01, 0x06]) + bytes([len(n) + 1, 0x09]) + n

def advertise():
    ble.gap_advertise(100_000, adv_data=make_payload(NAME))

def ble_irq(event, data):
    global conn, command
    if event == 1:                              # 폰이 연결됨
        conn = data[0]
        print("연결됨")
    elif event == 2:                            # 연결이 끊김
        conn = None
        print("끊김 → 다시 이름 알리기")
        advertise()
    elif event == 3:                            # 3 = 폰이 RX 에 글자를 써 넣음
        command = ble.gatts_read(rx_handle).decode().strip()   # 읽어서 포스트잇에 적어 둔다

ble.irq(ble_irq)

def send(msg):
    print(msg)
    if conn is not None:
        ble.gatts_notify(conn, tx_handle, msg.encode())

def timer_isr(t):
    global isr_cnt, flag_10ms
    isr_cnt += 1
    if isr_cnt % 10 == 0:
        flag_10ms = True
    if isr_cnt >= 1000:
        isr_cnt = 0

def task_10ms():
    global command
    if command:                                 # 폰에서 온 명령이 있으면 처리한다
        if command == "1":
            on_rx(20)
            send("모터 속도 1단계-20ms")
        elif command == "2":
            on_rx(40)
            send("모터 속도 2단계-40ms")
        elif command == "3":
            on_rx(60)
            send("모터 속도 3단계-60ms")
        elif command == "4":
            on_rx(80)
            send("모터 속도 4단계-80ms")
        elif command == "5":
            on_rx(100)
            send("모터 속도 5단계-100ms")
        else:
            on_rx(0)
            send("할당되지 않은 속도입니다.")
        command = ""                            # 처리했으니 포스트잇을 뗀다

tmr = Timer(0)
tmr.init(period=1, mode=Timer.PERIODIC, callback=timer_isr)
advertise()
print("이름 알리는 중:", NAME)

try:
    while True:
        if flag_10ms:
            flag_10ms = False
            task_10ms()
except KeyboardInterrupt:
    tmr.deinit()
    ble.gap_advertise(None)
    ble.active(False)
    M1_motor.deinit()
    M2_motor.deinit()
    M3_motor.deinit()
    M4_motor.deinit()
    print("정지")