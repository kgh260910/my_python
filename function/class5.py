""" 복습
class Box:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def center_x(self):
        return (self.x1 + self.x2) / 2

b = Box(500, 700)
print(b.center_x())
"""


ZX1 = 300
ZY1 = 300
ZX2 = 900
ZY2 = 700

def is_inside(cx, cy):
    if ZX1 <= cx <= ZX2 and ZY1 <= cy <= ZY2:
        return True
    return False

class Box:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def center_x(self):
        return (self.x1 + self.x2) / 2
    def center_y(self):
        return (self.y1 + self.y2) / 2
    def in_zone(self):
        cx = self.center_x()
        cy = self.center_y()
        return is_inside(cx, cy)  # 밖에 있는 함수를 호출합니다.

b1 = Box(500, 400, 700, 600)
b2 = Box(0, 400, 200, 600)

a1 = is_inside(b1.center_x(), b1.center_y()) # 인자를 메서드로 넣었다.
a2 = b1.in_zone()                            # => 반환값이 있는 메서드
print(a1)          # True
print(a2)          # True

print(b1.in_zone())  # True
print(b2.in_zone())  # False



