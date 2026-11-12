import os
import cv2
from ultralytics import YOLO

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

# ---- 내가 바꾸는 값 ----
VIDEO = "kakaovideo.mp4"
CONF = 0.25
WANT = "car"

ZX1 = 0                               # 구역: 왼쪽 위 점
ZY1 = 350
ZX2 = 716                               # 구역: 오른쪽 아래 점
ZY2 = 700

from d31_video_output import make_video_path, get_video_fps, save_video_frame
OUTPUT_VIDEO = make_video_path("y9_track")
VIDEO_FPS = get_video_fps(VIDEO)
writer = None
model = YOLO("yolo26n.pt")
results = model.track(VIDEO, conf=CONF,
                      stream=True, verbose=False)

frame = 0
all_ids = []                # 지금까지 나온 번호
for result in results:
    ids = []                # 이 프레임의 번호
    inside = 0
    for box in result.boxes:
        name = result.names[int(box.cls[0])]
        if name == WANT:
            x1, y1, x2, y2 = box.xyxy[0]  # 각각의 사물에 대한 x1~y2
            cx = (float(x1) + float(x2)) / 2
            cy = (float(y1) + float(y2)) / 2
            if ZX1 <= cx <= ZX2 and ZY1 <= cy <= ZY2:
                inside = inside + 1
            if box.id is not None:
                num = int(box.id[0])
                ids.append(num)
                if num not in all_ids:
                    all_ids.append(num)
    ids.sort()
    writer = save_video_frame(writer, OUTPUT_VIDEO, result.plot(), VIDEO_FPS)
    frame = frame + 1
    print("프레임", frame, "번째: 자동차 ID", ids)

    # ---- 조각 3 : 구역을 그려 넣기 (y7 에서 가져옴) ----
    img = result.plot(labels=True)
    cv2.rectangle(img, (ZX1, ZY1), (ZX2, ZY2), (0, 255, 255), 2)
                                                 # B G R 값   #선 굵기
    # ---- 조각 4 : 구역 안 사람 수를 글자로 쓰기 (글자 준비 + putText) ----
    text = "inside Car" + str(inside)
    cv2.putText(img, text, (ZX1, ZY1 - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
    # ---- 조각 5 : 창에 보이기 ----
    writer = save_video_frame(writer, OUTPUT_VIDEO, img, VIDEO_FPS)
    cv2.imshow("zone", img)
    cv2.waitKey(1)

writer.release()
print("전체", frame, "프레임 / 서로 다른 자동차 ID", len(all_ids), "개")
print("동영상 저장:", OUTPUT_VIDEO)

cv2.destroyAllWindows()