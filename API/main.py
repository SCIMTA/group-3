import cv2
import numpy as np
from fastapi import FastAPI, Form, UploadFile, File

from extra_partition import predict
from using_u2net import using_u2net

app = FastAPI(docs_url="/group3", redoc_url=None)


@app.post("/predict")
async def _predict(image: UploadFile = File(...), answer: str = Form('')):
    img, img_color = await get_mat_image(image)
    cv2.imwrite('cache.png', img_color)
    img_color = cv2.resize(img_color, (320, 320))
    u2net_img, path_u2net = using_u2net(img_color)
    return predict(cv2.cvtColor(u2net_img, cv2.COLOR_BGR2GRAY), answer)


async def get_mat_image(image_file):
    contents = await image_file.read()
    np_arr = np.fromstring(contents, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE), cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
