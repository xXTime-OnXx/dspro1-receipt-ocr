from typing import List

from receipt.receipt_item import ReceiptItem

class ReceiptService():

    def __init__(self):
        # TODO: initialize tesseract
        # TODO: initialize NER model (spacy)
        pass

    def stringify(self, image) -> str:
        # TODO: image to text with tesseract
        pass

    def extract_items(self, text: str) -> List[ReceiptItem]:
        # TODO: extract items from string with NER model (spacy)
        return {
            "items": [
                {
                    "quantity": 1,
                    "name": "Accessoires",
                    "price": 34.90
                },
                {
                    "quantity": 1,
                    "name": "Oberteile (Sammelgruppe)",
                    "price": 129.00
                }
            ]
        }

