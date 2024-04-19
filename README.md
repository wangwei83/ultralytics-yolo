# ultralytics-yolov8

# https://docs.ultralytics.com/quickstart/#use-ultralytics-with-python  主要参考文档来源
# https://github.com/ultralytics/ultralytics

# 论文
# Simon, M., Milz, S., Amende, K., & Gross, H.-M. (2018). Complex-YOLO: Real-time 3D Object Detection on Point Clouds. In arXiv [cs.CV]. arXiv. http://arxiv.org/abs/1803.06199
# Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-Time Open-Vocabulary Object Detection. In arXiv [cs.CV]. arXiv. http://arxiv.org/abs/2401.17270#

# https://docs.ultralytics.com/models/yolo-world/                        CVPR2024，上可通天；
# https://www.ultralytics.com/zh/solutions/ai-in-self-driving            自动驾驶，下可达地。

conda create -n ultralytics

conda activate ultralytics

# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics

# 训练
yolo train data=coco8.yaml model=yolov8n.pt epochs=10 lr0=0.01

# 推理预测
yolo predict model=yolov8n-seg.pt source='.\pic.png'  imgsz=320