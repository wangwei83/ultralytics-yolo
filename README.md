# ultralytics-yolov8


conda create -n ultralytics

conda activate ultralytics

# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics

# 训练
yolo train data=coco8.yaml model=yolov8n.pt epochs=10 lr0=0.01

