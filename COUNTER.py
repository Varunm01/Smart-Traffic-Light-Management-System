from ultralytics import YOLO
from TRAFFIC_TIMING import traffic_light
import cv2
import cvzone
import math

model = YOLO('Yolo-Weights/yolov8n.pt')

img1 = cv2.imread("IMAGES/4.jpg")
img2 = cv2.imread("IMAGES/3.jpg")
img3 = cv2.imread("IMAGES/1.jpg") 


def bounding_boxes(result, img):

    count = 0
    classnames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                  "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                  "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                  "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                  "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                  "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                  "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                  "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                  "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                  "teddy bear", "hair drier", "toothbrush"
                  ]
    for r in result:
        boxes = r.boxes
        for box in boxes:
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentclass = classnames[cls]
            if (currentclass == "car" or currentclass == "truck" or currentclass == "bus" or currentclass == "motorbike")\
                    and conf > 0.3:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                cvzone.putTextRect(img, f'{conf}', (max(0, x1), max(35, y1)),
                                    scale=0.7, thickness=1, offset=1)
                cvzone.cornerRect(img, (x1, y1, w, h), l=4, t=2, rt=1, colorR=(55, 255, 0), colorC=(255, 255, 0))
                count += 1
    return count


results = model(img1, stream=True)
count1 = bounding_boxes(results, img1)
print('Count 1 :', count1)

results = model(img2, stream=True)
count2 = bounding_boxes(results, img2)
print('Count 2 :', count2)

results = model(img3, stream=True)
count3 = bounding_boxes(results, img3)
print('Count 3 :', count3)


traffic_light(count1, count2, count3)


cv2.imshow('ImageRegion', img1)
cv2.waitKey(0)

cv2.imshow('ImageRegion', img2)
cv2.waitKey(0)

cv2.imshow('ImageRegion', img3)
cv2.waitKey(0)
