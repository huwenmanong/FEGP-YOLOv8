# One-command inference: input folder (images), output folder (results), pre-trained weight
python tools/infer.py \
  --source data/val_images  # Path to DUT-Anti-UAV validation images (640×640)
  --weights weights/FEGP-YOLOv8_best.pt  # Path to released pre-trained weight
  --output results/infer_output  # Path to save detection results (bbox + confidence)
  --img-size 640  # Inference size (consistent with Section 4.2)
  --device 0  # Use NVIDIA RTX 3080 Ti (GPU 0, consistent with experimental hardware)
