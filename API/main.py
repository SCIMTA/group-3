import cv2
import numpy as np
from fastapi import FastAPI, Form, UploadFile, File

from extra_partition import predict

app = FastAPI(docs_url="/group3", redoc_url=None)


@app.post("/predict")
async def _predict(image: UploadFile = File(...), answer: str = Form('')):
    img = await get_mat_image(image)
    cv2.imwrite("cache.png", img)
    return predict(img, answer)


async def get_mat_image(image_file):
    contents = await image_file.read()
    np_arr = np.fromstring(contents, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
