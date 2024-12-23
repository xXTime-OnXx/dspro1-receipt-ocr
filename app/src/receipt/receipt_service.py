import os
import cv2
import spacy
import pytesseract

from typing import List

from receipt.receipt_item import ReceiptItem

class ReceiptService():

    def __init__(self):
        path = os.path.abspath("../named-entity-recognition/models/receipts-ner-v01")
        self.nlp = spacy.load(path)
        
        pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'


    def stringify(self, image) -> str:
        resized_image = self._resize(image)
        gray_image = self._get_grayscale(resized_image)
        return pytesseract.image_to_string(gray_image, lang='eng', config='--oem 3 -c tessedit_char_blacklist="!@%^&*_+=<>?/{}|\\~`£"')


    def extract_items(self, text: str) -> List[ReceiptItem]:
        doc = self.nlp(text)
        return [ReceiptItem(ent.text) for ent in doc.ents if ent.label_ == 'RECEIPT_ITEM']
    
    # ------------------------------------------------------------------------------------------------------------------------

    def _resize(self, image, scale=1.5):
        height, width = image.shape[:2]
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        return resized_image
    
    def _get_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)