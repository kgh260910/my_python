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
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def center_x(self):
        return (self.x1 + self.x2) / 2
    def center_y(self):
        return (self.y1 + self.y2) / 2
    def in_zone(self):
        cx = self.center_x()
        cy = self.center_y()
        return is_inside(cx, cy)
    def __str__(self):              # str(...) : 문자열로 변환 합니다.
        return "Box center " + str(self.center_x()) + ", " + str(self.center_y())

class StrictBox(Box):   # 상속받은 StrictBox class
    def in_zone(self):  # 두개의 좌표가 is_inside()에 의해 둘다 안에 있으면 박스 전체가 완전히 구역 안에 있다.
        return is_inside(self.x1, self.y1) and is_inside(self.x2, self.y2)
    def __str__(self):
        return "StrictBox center (" + str(self.x1) + ", " + str(self.y1) + "), (" + str(self.x2) + ", " + str(self.y2) + ")"

class LabelBox(Box):
    def __init__(self, x1, y1, x2, y2, label):
        super().__init__(x1, y1, x2, y2)   # 부모클래스인 Box.__init__(...)을 사용한다.
        self.label = label
    def __str__(self):
        return self.label + " " + super().__str__()   #부모클래스의 __str__(self)를 사용한다.

b1 = Box(500, 400, 700, 600)
b2 = StrictBox(200, 400, 500, 600)
b3 = LabelBox(0, 400, 200, 600, "car")
boxes = [b1, b2, b3]
count = 0
for b in boxes:
    print(b, b.in_zone())
    # b, b.in_zone() 을 사용할 때, b1은 Box의객체여서 Box클래스 내부 in_zone()메서드를 사용하고
    # b2는 StrictBox클래스 내부 in_zone()메서드를 사용하고,
    # b3는 내부에 in_zone()메서드가 없어 부모클래스의 in_zone()메서드를 사용합니다.
    if b.in_zone():
        count += 1
print(count)
print(b1.x1, b1.y1, b1.x2, b1.y2)
print(b1.center_x(), b1.center_y())

