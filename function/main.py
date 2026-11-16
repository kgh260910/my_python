# 덧셈 연산
def add(x, y):
    z = x + y
    return z
# 뺄셈 연산
def sub(x, y):
    z = x - y
    return z
# 곱셈 연산
def mul(x, y):
    z = x * y
    return z
# 나눗셈 연산
def div(x, y):
    z = x / y
    return z

def center(a, b):
    return (a + b) / 2
"""
print("======")
print("환영합니다")
print("======")

print("======")
print("환영합니다")
print("======")
"""

#Q0) 반복되는 print문을 함수로 만드세요.
def printWelcome():
    print("======")
    print("환영합니다")
    print("======")

# Q1) 가로w, 세로h를 받아 넓이를 print하는 함수를 만드세요.
def show_area(w, h):
    result = w * h
    print(result)

show_area(4, 5)
show_area(10, 3)
