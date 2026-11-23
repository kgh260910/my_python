import os
import cv2
from ultralytics import YOLO

HERE = os.path.dirname(os.path.abspath(__file__))  #file을 여는 기본 문법
os.chdir(HERE)  # 디렉토리에서 사용할 수 있게 넣어줍니다.

PHOTO = "sample_photos/plate_03.jpg"

car_model = YOLO("yolo26n.pt")       # 객체 생성
plate_model = YOLO("plate_best.pt")  # 객체 생성

car_result = car_model(PHOTO)[0]
plate_result = plate_model(PHOTO)[0]

picture = car_result.plot()             # 이미지를 만듭니다.
picture = plate_result.plot(img=picture)

cv2.imwrite("result.jpg", picture)
cv2.imshow("result", picture)
cv2.waitKey(0)     # 키보드 입력이 있을 때까지 프로그램 실행을 무한정 대기시키는 함수입니다.


