import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp16/weights/best.pt')
    model.val(data='dataset/my_data.yaml',
              split='test',
              imgsz=640,
              batch=4,
              project='runs/val',
              name='exp',
              )
