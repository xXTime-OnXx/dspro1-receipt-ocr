from typing import List

from fastapi import FastAPI, File, UploadFile

from receipt.receipt_service import ReceiptService
from receipt.receipt_item import ReceiptItem

receipt_service = ReceiptService()

app = FastAPI()


@app.get("/ping")
async def ping() -> str:
    return "pong"


@app.post("/receipt/image/items")
async def receipt_items(image: UploadFile):
    # TODO: check if input file is an image
    receipt_text = receipt_service.stringify(image)
    return receipt_service.extract_items(receipt_text)