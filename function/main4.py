ZX1 = 300
ZX2 = 900
ZY1 = 300
ZY2 = 700

FPS = 24
"""
def to_frames(seconds):
    return seconds * FPS

def is_inside(cx, cy):
    if ZX1 <= cx <= ZX2 and ZY1 <= cy <= ZY2:
        return True
    return False

print(is_inside(600, 500))
print(is_inside(100, 500))
print(is_inside(300, 500))

print(to_frames(2))
"""

# Q2) n이 100 이상이면 True, 아니면 False를 돌려주는 is_big함수를 만드세요.
def is_big(n):
    if n>=100:
        return True
    return False
print(is_big(101))

# Q3)
def is_inside(cx, cy):
    if 300 <= cx <= 900 and 300 <= cy <= 700:
        return True
    return False
print(is_inside(300, 300))         # True
print(is_inside(299, 500))         # False
print(is_inside(900, 701))         # False

# Q4 ) pass를 지우고 if와 return으로 채우세요.
# 힌트: cx가 600 보다 작은 경우를 생각합니다.
def is_left(cx):
    # pass
    if cx <= 600:
        return "left"
    return "right"
print(is_left(100))     # "left"(True)
print(is_left(600))     # "left"(True)
print(is_left(800))     # "right"(False)