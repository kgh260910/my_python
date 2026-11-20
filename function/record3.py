class Box:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class LabelBox(Box):
    def __init__(self, x1, y1, x2, y2, label):
        super().__init__(x1, y1, x2, y2)   # 부모클래스인 Box.__init__(...)을 사용한다.
        self.label = label

    def to_dict(self):
        return {"x1": self.x1, "label": self.label}

b3 = LabelBox(0, 400, 200, 600, "car")
b4 = LabelBox(0, 400, 200, 600, "person")

# record = b3.to_dict()
# record2 = b4.to_dict()

records = []
records.append(b3.to_dict())
records.append(b4.to_dict())
# records.append(record)
# records.append(record2)

# print(record["label"])
# print(record["x1"])
# print("**********************")
# print(records)
for record in records:
    for key, value in record.items():
        print(key, value)