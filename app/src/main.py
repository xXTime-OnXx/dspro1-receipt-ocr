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

    receipt_text = receipt_service.stringify(file)
    return receipt_service.extract_items(receipt_text)