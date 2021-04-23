import cv2
import numpy as np
from fastapi import FastAPI, Form, UploadFile, File

from extra_partition import predict

app = FastAPI(docs_url="/group3", redoc_url=None)


@app.post("/predict")
async def _predict(image: UploadFile = File(...), answer: str = Form('')):
    img, img_color = await get_mat_image(image)
    # img_color = cv2.resize(img_color, (320, 320), interpolation=cv2.INTER_LINEAR)
    # u2net_img = using_u2net(img_color)
    # cv2.imshow('', u2net_img)
    # cv2.waitKey()
    # return {}
    return predict(img, answer)


async def get_mat_image(image_file):
    contents = await image_file.read()
    np_arr = np.fromstring(contents, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE), cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
