import os
from ultralytics import YOLO

HERE = os.path.dirname(os.path.abspath(__file__))  #file을 여는 기본 문법
os.chdir(HERE)  # 디렉토리에서 사용할 수 있게 넣어줍니다.

PHOTO = "sample_photos/plate_03.jpg"


# model = YOLO("plate_best.pt")
model = YOLO("yolo26n.pt") 
result = model(PHOTO)[0]
result.show()            # 결과를 화면에 띄워줍니다.
print(model.names)

