import torch
import os
import cv2
from pathlib import Path

device = "cpu"
print(f"Device set to use {device}")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', device=device)
model.eval()

VALID_IMAGE_EXTS = ('.jpg', '.jpeg', '.png')
VALID_VIDEO_EXTS = ('.mp4', '.avi', '.mov')

def analyze_media(media_paths):
    results = []

    for file_path in media_paths:
        ext = Path(file_path).suffix.lower()

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"\nAnalyzing: {os.path.basename(file_path)}")

        # Handle images
        if ext in VALID_IMAGE_EXTS:
            detection = model(str(file_path))
            detections = detection.pandas().xyxy[0]
            labels = detections['name'].tolist()
            results.append({
                "file": file_path,
                "label": labels if labels else ["No detections"],
                "detection": detection
            })

        # Handle videos frame-by-frame
        elif ext in VALID_VIDEO_EXTS:
            cap = cv2.VideoCapture(file_path)
            frame_count = 0
            frame_labels = set()

            while True:
                ret, frame = cap.read()
                if not ret or frame_count >= 20:  # Limit to first 20 frames
                    break

                # Convert to RGB and run detection
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results_frame = model(rgb_frame)
                labels = results_frame.pandas().xyxy[0]['name'].tolist()
                frame_labels.update(labels)
                frame_count += 1

            cap.release()
            results.append({
                "file": file_path,
                "label": list(frame_labels) if frame_labels else ["No detections"],
                "detection": None  # Can store results_frame if needed
            })

        else:
            print(f"Unsupported file type: {file_path}")

    return results
