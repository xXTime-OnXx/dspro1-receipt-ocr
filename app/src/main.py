import numpy as np
import cv2

from fastapi import FastAPI, UploadFile, HTTPException

from receipt.receipt_service import ReceiptService


receipt_service = ReceiptService()

app = FastAPI()


@app.get("/ping")
async def ping() -> str:
    return "pong"


@app.post("/receipt/image/items")
async def receipt_items(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

    file_bytes = await file.read()
    file_array = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(file_array, cv2.IMREAD_COLOR)
    
    if image is None:
        raise HTTPException(status_code=400, detail="Failed to decode image.")

    receipt_text = receipt_service.stringify(image)
    return receipt_service.extract_items(receipt_text)