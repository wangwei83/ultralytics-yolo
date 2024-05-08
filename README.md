# ultralytics-yolov8

## https://docs.ultralytics.com/quickstart/#use-ultralytics-with-python  主要参考文档来源
## https://github.com/ultralytics/ultralytics

# 论文
# 上可通天
## Simon, M., Milz, S., Amende, K., & Gross, H.-M. (2018). Complex-YOLO: Real-time 3D Object Detection on Point Clouds. In arXiv [cs.CV]. arXiv. http://arxiv.org/abs/1803.06199
## Wang, C.-Y., Bochkovskiy, A., & Liao, H.-Y. M. (2023). YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. https://github.com/WongKinYiu/yolov7 CVPR2023. 
## Glenn Jocher, Ayush Chaurasia, and Jing Qiu. Yolo by ultralytics, 2023. https://github.com/ultralytics/ultralytics. 也就是yolov8
## Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-Time Open-Vocabulary Object Detection. In arXiv [cs.CV]. arXiv. http://arxiv.org/abs/2401.17270   https://docs.ultralytics.com/models/yolo-world/                        CVPR2024；
# 下可达地

## https://www.ultralytics.com/zh/solutions/ai-in-self-driving            自动驾驶。

conda create -n ultralytics

conda activate ultralytics

# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics

# 训练
yolo train data=coco8.yaml model=yolov8n.pt epochs=10 lr0=0.01

# 推理预测
yolo predict model=yolov8n-seg.pt source='.\pic.png'  imgsz=320