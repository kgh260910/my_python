import os
import cv2
from ultralytics import YOLO

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
NUMBER = 1              # 사진을 하나만 사용한다.
PHOTO_DIR = "test_images"
if not os.path.isdir(PHOTO_DIR):
    raise FileNotFoundError("test_images 폴더가 없습니다.")
photo_names = sorted(name for name in os.listdir(PHOTO_DIR)
                     if name.lower().endswith((".jpg", ".jpeg", ".png")))  # 해당 확장자를 읽을수 있게
if not photo_names:
    raise FileNotFoundError("test_images 폴더에 JPG, JPEG, PNG 사진이 없습니다.")
if not 1 <= NUMBER <= len(photo_names):
    raise ValueError(f"NUMBER는 1부터 {len(photo_names)} 사이여야 합니다.")
PHOTO = os.path.join(PHOTO_DIR, photo_names[NUMBER - 1])    # 두개를 붙입니다(join)
WEIGHT = "best.pt"
model = YOLO(WEIGHT)
result = model.predict(PHOTO, conf=0.25, verbose=False)[0]  # predict : 예측하다 , verbose=False : 추론 중 콘솔에 찍히는걸 끕니다.
print("사진 번호:", NUMBER, "/", len(photo_names), photo_names[NUMBER - 1]) # 사진 번호: 1 / 29 (사진이름) 형식으로 출력됩니다.
for box in result.boxes:
    print(model.names[int(box.cls)], f"점수 {float(box.conf):.2f}")
os.makedirs("results", exist_ok=True)           # "results" 디렉터리를 만듭니다. / exist_ok=True : 존재하더라도 실행합니다.
prefix = "base" if WEIGHT == "yolo26n.pt" else "mine"  # yolo26n.pt면 접두사로 "base"를 넣고 아니면 "mine"을 넣습니다.
output = os.path.join("results", f"{prefix}_{NUMBER}.jpg") # results/base_1.jpg 또는 results/mine_1.jpg 형태의 저장 경로 문자열을 완성합니다.

if not cv2.imwrite(output, result.plot()):
    raise OSError("결과 그림을 저장하지 못했습니다: " + output)
print("저장:", output)
