import torch
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# 加载模型
model = torch.hub.load('ultralytics/yolov8', 'yolov8n', pretrained=True)

# 打开图像文件
img_path = './pic.png'
img = Image.open(img_path)

# 进行预测
results = model(img)

# 绘制结果
results.show()

# 保存带有检测框的图像
# results.save(save_dir='./')
