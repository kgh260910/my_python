"""
def add(a, b):
    return a+b
answer = add(1, 3)
print(answer)               # 4


FPS = 24

def to_frames(sec):
    a = sec * FPS   # 48
    b = sec * 5     # 10
    return a , b

result, x = to_frames(2)
print(result)
print(x)
"""
# 심화과정

def calculate(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

add, sub, mul, div = calculate(5, 2)
print("합: ", add)
print("빼기: ", sub)
print("곱: ", mul)
print("나누기: ", div)
print("나누기: ", int(div))
# print("나누기: ", round(1,div))  에러발생
print("나누기: ", round(div,0))

print(add, sub, mul, div)

