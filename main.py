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


print(w_max_average, h_max_average, w_min, h_min)
# lấy tọa độ điểm để, cắt ảnh
sbd = box_rect[2][0], box_rect[2][1], box_rect[5][0], box_rect[5][1]
ma_de = box_rect[3][0], box_rect[3][1], box_rect[0][0], box_rect[5][1]
cau_1_den_10 = box_rect[8][0], box_rect[8][1], box_rect[13][0], box_rect[13][1]
cau_11_den_20 = box_rect[12][0], box_rect[12][1], box_rect[17][0], box_rect[17][1]
cau_21_den_30 = box_rect[16][0], box_rect[16][1], box_rect[23][0], box_rect[23][1]
cau_31_den_40 = box_rect[9][0], box_rect[9][1], box_rect[11][0], box_rect[12][1]
cau_41_den_50 = box_rect[13][0], box_rect[13][1], box_rect[15][0], box_rect[15][1]
cau_51_den_60 = box_rect[17][0], box_rect[17][1], box_rect[21][0], box_rect[21][1]
cau_61_den_70 = box_rect[7][0], box_rect[7][1], box_rect[10][0], box_rect[10][1]
cau_71_den_80 = box_rect[11][0], box_rect[11][1], box_rect[14][0], box_rect[14][1]
cau_81_den_90 = box_rect[15][0], box_rect[15][1], box_rect[20][0], box_rect[20][1]
cau_91_den_100 = box_rect[6][0], box_rect[6][1], box_rect[0][0], box_rect[10][1]
cau_101_den_110 = box_rect[10][0], box_rect[10][1], box_rect[0][0], box_rect[14][1]
cau_111_den_120 = box_rect[14][0], box_rect[14][1], box_rect[0][0], box_rect[20][1]
# cắt ảnh
x1, y1, x2, y2 = sbd
cv2.imwrite('extra/sbd.png', image[y1 + h_min:y2, x1 + int(w_min * 1.4):x2 - int(w_min * 1.8)])
x1, y1, x2, y2 = ma_de
cv2.imwrite('extra/ma_de.png', image[y1 + h_min:y2, x1 + int(w_min * 1.4):x2 - int(w_max_average * 1.4)])
x1, y1, x2, y2 = cau_1_den_10
cv2.imwrite('extra/cau_1_den_10.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_11_den_20
cv2.imwrite('extra/cau_11_den_20.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_21_den_30
cv2.imwrite('extra/cau_21_den_30.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_31_den_40
cv2.imwrite('extra/cau_31_den_40.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_41_den_50
cv2.imwrite('extra/cau_41_den_50.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_51_den_60
cv2.imwrite('extra/cau_51_den_60.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_61_den_70
cv2.imwrite('extra/cau_61_den_70.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_71_den_80
cv2.imwrite('extra/cau_71_den_80.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_81_den_90
cv2.imwrite('extra/cau_81_den_90.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 1.9)])
x1, y1, x2, y2 = cau_91_den_100
cv2.imwrite('extra/cau_91_den_100.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 2.9)])
x1, y1, x2, y2 = cau_101_den_110
cv2.imwrite('extra/cau_101_den_110.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 2.9)])
x1, y1, x2, y2 = cau_111_den_120
cv2.imwrite('extra/cau_111_den_120.png', image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
            : x2 - int(w_min * 2.9)])

# cv2.imshow('dap an2',image[y1:y2, x1:x2])

for idx, box in enumerate(box_rect):
    x, y, w, h = box
    cv2.putText(blank_image, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.4, (0, 0, 255),
                1)
cv2.imshow('blank_image', blank_image)
cv2.waitKey()
