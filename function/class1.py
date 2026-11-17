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
    def center_x(self):
        return (self.x1 + self.x2) / 2

b1 = Box()   # 객체 생성
b1.x1 = 500   #b1의 x1속성에 500을 할당시킨다.
b1.x2 = 700   #attribute

print(b1.center_x())
print(Box.center_x(b1))

# b1 = Box()  # 속성이있던b1객체를 새로만든 속성없는 b1객체가 덮어씌워버립니다.
# b2 = Box()
# b2.x1 = 0
# b2.x2 = 200

# print(b1.x1)
# print(b2.x1)
# print(b1.x3)


# 복습 1>
class Box2:
    def center_x(self):
        print((self.x1 + self.x2) / 2)

b5 = Box2()
b5.x1 = 100
b5.x2 = 500
# print(b5.center_x())
b5.center_x()

# 복습 2>
class Box3:
    def center_x(self):
        return (self.x1 + self.x2) / 2
b7 = Box3()
b7.x1 = 200
b7.x2 = 600
print(b7.center_x(b7))
# #TypeError: Box3.center_x() takes 1 positional argument but 2 were given

