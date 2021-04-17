from typing import Optional

from fastapi import FastAPI, Header, Form, UploadFile, File
from fastapi.responses import FileResponse

from extra_partition import predict

app = FastAPI(docs_url="/group3", redoc_url=None)


@app.post("/predict")
def _predict(image: UploadFile = File(...)):
    return predict(image)
