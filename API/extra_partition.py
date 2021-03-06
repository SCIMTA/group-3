import cv2
import numpy as np

from Point import Point
from orc import extra_question, extra_info
from utils import on_fail, on_success


def extra_partition(img):
    width = 720
    height = 1018
    # height = 800

    h, w = img.shape
    img = img[int(h * 0.12):int(h * 0.88), int(w * 0.15):int(w * 0.85)]
    # cv2.imshow('', img[int(h * 0.12):int(h * 0.88), int(w * 0.15):int(w * 0.85)])
    # cv2.waitKey()
    min_area = width / 10
    image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, 35)

    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    blank_image = np.zeros((height, width, 3), np.uint8)
    contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    box_rect = []

    for idx, con in enumerate(contours):
        area = cv2.contourArea(con)
        x, y, w, h = cv2.boundingRect(con)
        if min_area < area < width and int(w / h) < 3 and w * h - area > w * h * 0.05:
            box_rect.append((x, y, w, h))

    mean = int(np.mean(list(map(lambda x: x[2], box_rect))))
    for box in box_rect.copy():
        if box[2] < mean - 2:
            box_rect.remove(box)
    for idx, box in enumerate(box_rect):
        x, y, w, h = box
        cv2.rectangle(blank_image, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

    # cv2.waitKey()
    # sắp xếp theo diện tích
    area_box = sorted(box_rect, key=lambda e: -e[2] * e[3])

    # lấy ra 4 ô ở góc
    max_box = area_box[:4]
    # sắp xếp từ trên xuống dưới
    max_box = sorted(max_box, key=lambda e: e[1])

    # sắp xếp từ ngang
    max_box[:2] = sorted(max_box[:2], key=lambda e: e[0])
    max_box[2:] = sorted(max_box[2:], key=lambda e: e[0])
    p1, p2, p3, p4 = max_box
    list_max_box = [[p1[0], p1[1]],
                    [p2[0] + p2[2], p2[1]],
                    [p3[0], p3[1] + p3[3]],
                    [p4[0] + p4[2], p4[1] + p4[3]], ]
    pst1 = np.float32(list_max_box)
    w_b = width
    h_b = height
    pst2 = np.float32([[0, 0], [w_b, 0], [0, h_b], [w_b, h_b]])
    matrix = cv2.getPerspectiveTransform(pst1, pst2)
    img_out = cv2.warpPerspective(image, matrix, (w_b, h_b))

    #####    crop_img handle
    blank_image = np.zeros((img_out.shape[0], img_out.shape[1], 3), np.uint8)
    contours, _ = cv2.findContours(img_out, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    box_rect = []

    for idx, con in enumerate(contours):
        area = cv2.contourArea(con)
        x, y, w, h = cv2.boundingRect(con)
        if min_area < area < width and int(w / h) < 2.5 and w * h - area > w * h * 0.05:
            box_rect.append((x, y, w, h))

    mean = int(np.mean(list(map(lambda x: x[2], box_rect))))
    for box in box_rect.copy():
        if box[2] < mean - 2:
            box_rect.remove(box)
    for idx, box in enumerate(box_rect):
        x, y, w, h = box
        cv2.rectangle(blank_image, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)
    #####
    # cv2.imshow('image', image)
    # cv2.imshow('blank_image', blank_image)
    # cv2.imshow('img_out', img_out)
    # cv2.waitKey()

    ##### short again
    box_rect = sorted(box_rect, key=lambda e: -e[2] * e[3])

    max_box = box_rect[:4]
    # sắp xếp từ trên xuống dưới
    max_box = sorted(max_box, key=lambda e: e[1])
    max_box[:2] = sorted(max_box[:2], key=lambda e: e[0])
    max_box[2:] = sorted(max_box[2:], key=lambda e: e[0])

    box_rect = box_rect[4:]
    #####

    # sắp xếp từ trên xuống dưới
    box_rect = sorted(box_rect, key=lambda e: e[1])

    # sắp xếp từ ngang
    box_rect[:2] = sorted(box_rect[:2], key=lambda e: e[0])
    box_rect[2:4] = sorted(box_rect[2:4], key=lambda e: e[0])
    box_rect[4:8] = sorted(box_rect[4:8], key=lambda e: e[0])
    box_rect[8:12] = sorted(box_rect[8:12], key=lambda e: e[0])
    box_rect[12:16] = sorted(box_rect[12:16], key=lambda e: e[0])
    box_rect[16:20] = sorted(box_rect[16:20], key=lambda e: e[0])

    list_box = list(map(lambda x: Point(x[0], x[1]), box_rect))
    list_max_box_area = list(map(lambda x: Point(x[0], x[1]), max_box))

    def gen_x_y(p1, p2):
        return list_box[p1].x, list_box[p1].y, list_box[p2].x, list_box[p2].y

    # lấy tọa độ điểm để, cắt ảnh
    sbd = gen_x_y(0, 3)
    ma_de = list_box[1].x, list_box[1].y, list_max_box_area[1].x, list_box[3].y
    cau_1_den_10 = gen_x_y(4, 9)
    cau_11_den_20 = gen_x_y(8, 13)
    cau_21_den_30 = gen_x_y(12, 17)
    cau_31_den_40 = gen_x_y(5, 10)
    cau_41_den_50 = gen_x_y(9, 14)
    cau_51_den_60 = gen_x_y(13, 18)
    cau_61_den_70 = gen_x_y(6, 11)
    cau_71_den_80 = gen_x_y(10, 15)
    cau_81_den_90 = gen_x_y(14, 19)
    cau_91_den_100 = list_box[7].x, list_box[7].y, list_max_box_area[3].x, list_box[11].y
    cau_101_den_110 = list_box[11].x, list_box[11].y, list_max_box_area[3].x, list_box[15].y
    cau_111_den_120 = list_box[15].x, list_box[15].y, list_max_box_area[3].x, list_box[19].y
    # cắt ảnh
    image = img_out
    x1, y1, x2, y2 = sbd
    img_sbd = image[y1 + 19:y2 + 3, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = ma_de
    img_ma_de = image[y1 + 19:y2 - 5, x1 + 21:x2 - 32]

    x1, y1, x2, y2 = cau_1_den_10
    img_cau_1_den_10 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_11_den_20
    img_cau_11_den_20 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_21_den_30
    img_cau_21_den_30 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_31_den_40
    img_cau_31_den_40 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_41_den_50
    img_cau_41_den_50 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_51_den_60
    img_cau_51_den_60 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_61_den_70
    img_cau_61_den_70 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_71_den_80
    img_cau_71_den_80 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_81_den_90
    img_cau_81_den_90 = image[y1 + 19:y2 - 5, x1 + 20:x2 - 20]

    x1, y1, x2, y2 = cau_91_den_100
    img_cau_91_den_100 = image[y1 + 19:y2, x1 + 20:x2 - 35]

    x1, y1, x2, y2 = cau_101_den_110
    img_cau_101_den_110 = image[y1 + 19:y2, x1 + 20:x2 - 35]

    x1, y1, x2, y2 = cau_111_den_120
    img_cau_111_den_120 = image[y1 + 19:y2, x1 + 20:x2 - 35]

    # cv2.imshow('', img_ma_de)
    # cv2.waitKey()

    return img_sbd, img_ma_de, img_cau_1_den_10, img_cau_11_den_20, img_cau_21_den_30, img_cau_31_den_40, img_cau_41_den_50, img_cau_51_den_60, img_cau_61_den_70, img_cau_71_den_80, img_cau_81_den_90, img_cau_91_den_100, img_cau_101_den_110, img_cau_111_den_120


def predict(img, answer):
    try:
        len_answer = len(answer)

        if len_answer == 0:
            return on_fail("Câu trả lời không hợp lệ")

        img_sbd, img_made, img_cau_1_den_10, img_cau_11_den_20, img_cau_21_den_30, img_cau_31_den_40, img_cau_41_den_50, img_cau_51_den_60, img_cau_61_den_70, img_cau_71_den_80, img_cau_81_den_90, img_cau_91_den_100, img_cau_101_den_110, img_cau_111_den_120 = extra_partition(
            img)

        #### debug

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
                wrong[index + 1] = {
                    "correct": answer[index],
                    "incorrect": values[index]
                }

        return on_success({
            "sbd": sbd,
            "ma_de": ma_de,
            "point": round(point / len_answer * 10, 1),
            "wrong": wrong,
        })

    except Exception as err:
        print(err)
        return on_fail("Ảnh không hợp lệ")
