import cv2
import torch

# 加载预训练的YOLOv5模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 打开MP4视频文件
video_path = 'videoplayback.mp4'
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧转换为模型输入所需的格式，并进行预测
    results = model(frame)

    # 渲染检测结果回到帧上
    frame = results.render()[0]

    # 显示带有检测结果的帧
    cv2.imshow('YOLO Real-Time Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按'q'键退出
        break

cap.release()
cv2.destroyAllWindows()
