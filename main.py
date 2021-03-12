import cv2
import numpy as np

width = 720
height = 1018
min_area = width / 10

image = cv2.imread('template_use.png', 0)
image = cv2.resize(image, (width, height))
blank_image = np.zeros((height, width, 3), np.uint8)
contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
box_rect = []
for idx, con in enumerate(contours):
    area = cv2.contourArea(con)
    x, y, w, h = cv2.boundingRect(con)
    if min_area < area < width and int(w / h) < 3:
        if w * h - (h * 2.5) < area:
            box_rect.append((x, y, w, h))
            cv2.drawContours(blank_image, contours, idx, (255, 255, 255), thickness=1)


def sort_box(box):
    return box[2] * box[3]


box_rect = sorted(box_rect, key=sort_box)
four_max_box = box_rect[-4:]
w_max_average = int(np.average(list(map(lambda box: box[2], four_max_box))))
h_max_average = int(np.average(list(map(lambda box: box[3], four_max_box))))
box_rect = sorted(box_rect, key=lambda box: box[1])
_, _, w_min, h_min = list(sorted(box_rect, key=lambda box: box[2]))[0]

for idx, box in enumerate(box_rect):
    x, y, w, h = box
    cv2.putText(blank_image, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.4, (0, 0, 255),
                1)
print(w_max_average, h_max_average, w_min, h_min)
sbd = box_rect[2][0], box_rect[2][1], box_rect[5][0], box_rect[5][1]
ma_de = box_rect[3][0], box_rect[3][1], box_rect[0][0], box_rect[5][1]
cv2.imshow('blank_image', blank_image)
x1, y1, x2, y2 = sbd
cv2.imwrite('extra/sbd.png', image[y1 + h_min:y2, x1 + int(w_min * 1.4):x2 - int(w_min * 1.8)])
x1, y1, x2, y2 = ma_de
cv2.imwrite('extra/ma_de.png', image[y1 + h_min:y2, x1 + int(w_min * 1.4):x2 - int(w_max_average * 1.4)])
cv2.waitKey()
