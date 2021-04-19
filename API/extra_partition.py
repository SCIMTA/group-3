import cv2
import numpy as np

from orc import extra_question, extra_info
from utils import on_fail, on_success


def extra_partition(img):
    width = 720
    height = 1018
    min_area = width / 10
    ret, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    image = cv2.resize(thresh, (width, height))

    blank_image = np.zeros((height, width, 3), np.uint8)
    contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    box_rect = []
    for idx, con in enumerate(contours):
        area = cv2.contourArea(con)

        x, y, w, h = cv2.boundingRect(con)
        if min_area < area < width and int(w / h) < 3:
            if w * h - area < w * h * 0.23:
                box_rect.append((x, y, w, h))

                # cv2.drawContours(blank_image, contours, idx, (255, 255, 255), thickness=1)

    box_rect = sorted(box_rect, key=lambda box: box[0])
    box_rect = sorted(box_rect, key=lambda box: box[1])
    for box in box_rect:
        x, y, w, h = box
        cv2.rectangle(blank_image, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)
        cv2.imshow("blank_image", blank_image)
        cv2.waitKey()

    _, _, w_min, h_min = list(sorted(box_rect, key=lambda box: box[2]))[0]

    # print(w_max_average, h_max_average, w_min, h_min)
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
    img_sbd = image[y1 + 30:y2, x2:x1 - 10]

    x1, y1, x2, y2 = ma_de
    img_ma_de = image[y1:y2, x1:x2]
    print(ma_de)
    # cv2.imshow('', img_ma_de)
    # cv2.waitKey()
    x1, y1, x2, y2 = cau_1_den_10
    img_cau_1_den_10 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                          : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_11_den_20

    img_cau_11_den_20 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4): x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_21_den_30
    img_cau_21_den_30 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_31_den_40
    img_cau_31_den_40 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_41_den_50
    img_cau_41_den_50 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_51_den_60
    img_cau_51_den_60 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_61_den_70
    img_cau_61_den_70 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_71_den_80

    img_cau_71_den_80 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_81_den_90
    img_cau_81_den_90 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                           : x2 - int(w_min * 1.9)]
    x1, y1, x2, y2 = cau_91_den_100
    img_cau_91_den_100 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                            : x2 - int(w_min * 2.9)]
    x1, y1, x2, y2 = cau_101_den_110
    img_cau_101_den_110 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3),
                          x1 + int(w_min * 1.4): x2 - int(w_min * 2.9)]
    x1, y1, x2, y2 = cau_111_den_120
    img_cau_111_den_120 = image[y1 + int(h_min * 1.3):y2 - int(h_min * 0.3), x1 + int(w_min * 1.4)
                                                                             : x2 - int(
        w_min * 2.9)]
    return img_sbd, img_ma_de, img_cau_1_den_10, img_cau_11_den_20, img_cau_21_den_30, img_cau_31_den_40, img_cau_41_den_50, img_cau_51_den_60, img_cau_61_den_70, img_cau_71_den_80, img_cau_81_den_90, img_cau_91_den_100, img_cau_101_den_110, img_cau_111_den_120


def predict(img, answer):
    # try:
    len_answer = len(answer)

    if len_answer == 0:
        return on_fail("Câu trả lời không hợp lệ")

    img_sbd, img_made, img_cau_1_den_10, img_cau_11_den_20, img_cau_21_den_30, img_cau_31_den_40, img_cau_41_den_50, img_cau_51_den_60, img_cau_61_den_70, img_cau_71_den_80, img_cau_81_den_90, img_cau_91_den_100, img_cau_101_den_110, img_cau_111_den_120 = extra_partition(
        img)

    data = {}
    sbd = extra_info(img_sbd, 10, 6)
    ma_de = extra_info(img_made, 10, 3)
    data.update(extra_question(img_cau_1_den_10))
    if len_answer > 10:
        data.update(extra_question(img_cau_11_den_20, start_question=11))
    if len_answer > 20:
        data.update(extra_question(img_cau_21_den_30, start_question=21))
    if len_answer > 30:
        data.update(extra_question(img_cau_31_den_40, start_question=31))
    if len_answer > 40:
        data.update(extra_question(img_cau_41_den_50, start_question=41))
    if len_answer > 50:
        data.update(extra_question(img_cau_51_den_60, start_question=51))
    if len_answer > 60:
        data.update(extra_question(img_cau_61_den_70, start_question=61))
    if len_answer > 70:
        data.update(extra_question(img_cau_71_den_80, start_question=71))
    if len_answer > 80:
        data.update(extra_question(img_cau_81_den_90, start_question=81))
    if len_answer > 90:
        data.update(extra_question(img_cau_91_den_100, start_question=91))
    if len_answer > 100:
        data.update(extra_question(img_cau_101_den_110, start_question=101))
    if len_answer > 110:
        data.update(extra_question(img_cau_111_den_120, start_question=111))

    values = list(data.values())
    point = 0
    wrong = {}
    for index in range(len_answer):
        if values[index] == answer[index]:
            point += 1
        else:
            wrong[index] = {
                "correct": answer[index],
                "incorrect": values[index]
            }

    return on_success({
        "sbd": sbd,
        "ma_de": ma_de,
        "point": round(point / len_answer * 10, 1),
        "wrong": wrong,
    })
# except Exception as err:
#     print(err)
#     return on_fail("Ảnh không hợp lệ")
