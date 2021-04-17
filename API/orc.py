import cv2
import numpy as np

path = 'extra/'

# for file in os.listdir(path):
#     image = cv2.imread(path + file)
#     cv2.imshow('', image)
#     cv2.waitKey()

img = cv2.imread('extra/cau_1_den_10.png', 0)


# cv2.imshow('', image)
# cv2.waitKey()

def split_image(s_image, i_h, i_w, i, j):
    return s_image[i * i_h:i * i_h + i_h + 5, j * i_w:j * i_w + i_w]


def extra_info(image, column, row):
    h, w = image.shape
    item_h = h // column
    item_w = w // row
    text = []
    for i in range(column):
        for j in range(row):
            item = split_image(image, item_h, item_w, i, j)
            ret, thresh = cv2.threshold(item, 127, 255, cv2.THRESH_BINARY)
            arr = np.array(thresh)
            unique, count = np.unique(arr, return_counts=True)

            if len(count) == 2 and count[0] > 50:
                text.append(str(i))

    return ''.join(text)


def num_to_text(n):
    switcher = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
    }
    return switcher.get(n, "Invalid num")


def extra_question(image, column=10, row=4):
    h, w = image.shape
    item_h = h // column
    item_w = w // row
    value = {}
    for i in range(column):
        for j in range(row):
            item = split_image(image, item_h, item_w, i, j)
            ret, thresh = cv2.threshold(item, 127, 255, cv2.THRESH_BINARY)
            arr = np.array(thresh)
            unique, count = np.unique(arr, return_counts=True)
            if len(count) == 2 and count[0] > 50:
                value[i] = num_to_text(j)
    return value


print(extra_question(img))
