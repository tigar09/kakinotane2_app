# 必要なモジュールのインポート
from ultralytics import YOLO

#自作データーセットを利用して学習したデータ
model = YOLO('./detection_yolov5n.pt')