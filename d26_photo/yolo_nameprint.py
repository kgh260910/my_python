from ultralytics import YOLO

model = YOLO("yolo26n.pt")

print("YOLO가 아는 이름: ", len(model.names), "가지")

for number in model.names:
    print(number, model.names[number])
