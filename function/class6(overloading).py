from function.class2 import b2

"""""""""
class Box:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def center_x(self):
        return (self.x1 + self.x2) / 2

b0 = Box()          #호출 시 값을 생략하면 자동으로 0이 할당됩니다.
b1 = Box(10,20)    # 앞의 x1,y1에만 인자가 들어가고 나머지는 0이 할당됩니다.
b2 = Box(x2 = 50)      # 매개변수 x2에만 50을 할당하고 나머지는 0이 할당됩니다.
b3 = Box(500, 400, 700, 600)

print(b0.center_x())
print(b1.center_x())
print(b2.center_x())
print(b3.center_x())
"""""""""

class Box:
    def __init__(self, x1 = 100, y1 = 0, x2 = 0, y2 = 0, y3 = 300):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def center_x(self):
        return (self.x1 + self.x2) / 2
b0 = Box()
b1 = Box(500, 400, 700, 600, 100)
# b2 = Box(500, 400, 700, 600, "문자100")

print(b0.center_x())
print(b1.center_x())
# print(b2.center_x())
print(b1.y3)