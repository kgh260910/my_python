from ultralytics import YOLO

model26n = YOLO("yolo26n.pt")
modelv8n = YOLO("YOLOv8n-oiv7.pt")

# 내가 바꾸는 값
NAME = modelv8n


if (NAME == model26n):
    print("YOLO26n이 아는 이름: ", len(model26n.names), "가지")
    for number in model26n.names:
        print(number, model26n.names[number])
else:
    print("YOLOv8n-oiv7이 아는 이름: ", len(modelv8n.names), "가지")
    for number in modelv8n.names:
        print(number, modelv8n.names[number])

