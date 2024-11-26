import spacy
from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")

data1 = '''
GREEN FIELD
5305 E PACIFIC COAST HWY
Long Beach, CA 90804
(562) 597-0906

Server: Francis         Station: 3
----------------------------------
Order #: 69923          Dine In
Table: B11              Guests: 2
----------------------------------
1 Coffee                3.00
2 Lunch                 45.90
1 Coke                  3.00

SUB TOTAL:              51.90
Tax 1:                  4.60

TOTAL:                  $56.58

    5/26/2016 12:53:10 PM

        THANK YOU!
'''

training_data = [
    (
        data1,
        [
            (246, 273, "RECEIPT_ITEM"),
            (275, 303, "RECEIPT_ITEM"),
            (305, 332, "RECEIPT_ITEM"),
        ]
    ),
]

# the DocBin will store the example documents
db = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    
    for ent in doc.ents:
        print(f'entity={ent.label_:<15s} {ent.text}, {ent.start}, {ent.end}')
    
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")