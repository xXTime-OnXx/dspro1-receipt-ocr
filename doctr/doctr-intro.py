from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Model
model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
# Image
img = DocumentFile.from_images("receipts/receipt1.jpg")
# Analyze
result = model(img)

result.show()