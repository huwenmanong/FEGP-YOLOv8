import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO



if __name__ == '__main__':

    model = YOLO('ultralytics/cfg/models/v8/yolov8.yaml')
    model.train(data='dataset/my_data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16,
                close_mosaic=Last 10 ,
                workers=0,
                device='0',
                optimizer='SGD', # using SGD
                # patience=0, # close earlystop
                resume=True,
                project='runs/train',
                name='exp',
                )