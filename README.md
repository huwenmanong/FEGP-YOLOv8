FEGP-YOLOv8
This project is directly related to the manuscript in The AIP: "Enhanced Feature Learning and Model Lightweighting for Real-Time UAV Detection Using FEGP-YOLOv8". We kindly request that when using this project, you cite the aforementioned manuscript from the journal.

This project uses the self-developed lightweight model, FEGP-YOLOv8, to achieve real-time UAV target detection. Both the accuracy and real-time performance have been significantly improved.

This project provides a pre-trained weight file, best.pt, on its homepage, along with scripts for training, testing, validation, calculating FPS, and generating heatmaps.

1. Datasets
The following official datasets are used in this study. Please download the exact versions via the links below for experiment reproducibility:

| Dataset Name | Official Link | Key Details (Consistent with Manuscript) | |--------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| DUT-Anti-UAV | https://github.com/wangdongdut/DUT-Anti-UAV | 10k images with 10k+ UAV targets; split into 8:1:1 (train/val/test) using random seed=42 | 
| Det-Fly | https://github.com/Jake-WU/Det-Fly | 13,271 images with diverse backgrounds/occlusion for robustness testing |
| VisDrone2019 | https://github.com/VisDrone/VisDrone-Dataset | Focus on small UAV targets; use "VisDrone2019-DET" subset for small-object validation |

2. One-Command Inference
The usage follows official YOLOv8 conventions with specific parameters as used in the manuscript:

2.1 Inference on Imagespython detect.py \
--source /path/to/your/image.jpg \ # Replace with dataset path (e.g., DUT-Anti-UAV/val/images) --weights best.pt \ # Pre-trained weights (see Section 3) --img 640 \ # Input size consistent with experiments --conf 0.25 \ # Confidence threshold used in all evaluations --save-img # Save visualized results

2.2 Inference on Videospython detect.py \
--source /path/to/your/video.mp4
--weights best.pt
--img 640
--conf 0.25
--save-video

3. Pretrained Weights
Pre-trained weights (trained on DUT-Anti-UAV training set) are available for direct use:

| Weight File | Performance on DUT-Anti-UAV Validation Set | Download Link | |--------------------|--------------------------------------------|--------------------------------------------------------------------------------| | best.pt| mAP50=95.4%, FPS=107.9±2.3, Size=3.4MB |On the project homepage|

4. Environment Setup
To ensure exact reproduction of results, install the following dependencies:

4.1 Required Libraries
Create requirements.txt with:torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 opencv-python==4.1.1 numpy==1.23.5 pycocotools==2.0.6 thop==0.1.1 # For GFLOPs calculation scikit-learn==1.0.2 # For statistical analysis tqdm==4.65.0 matplotlib==3.7.1

4.2 Installation Commandpip install -r requirements.txt
Notes
The project usage is consistent with official YOLOv8. For additional details, refer to the manuscript.
Third-party datasets/models are provided via official links. For access issues, contact the original authors.
We apologize for any inconvenience and appreciate your understanding regarding data access constraints.
