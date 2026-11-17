"""
a_x1 = 500
a_y1 = 400
a_x2 = 700
a_y2 = 600

b_x1 = 0
b_y1 = 400
b_x2 = 200
b_y2 = 600

a_center = (a_x1, a_x2) / 2
b_center = (b_x1, b_x2) / 2

print(a_center)
print(b_center)
"""

class Box:
    pass
b1 = Box()   # 객체 생성
b2 = Box()   # 객체 생성

b1.x1 = 500   #b1의 x1속성에 500을 할당시킨다.
b1.x2 = 700   #attribute

b2.x1 = 0
b2.x2 = 200

print(b1.x1)
print(b2.x1)
# print(b1.x3)