import json
import spacy
from spacy.tokens import Span
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split

# Load a blank SpaCy model
nlp = spacy.blank("de")

# Load Dataset
with open("./data/datasets/ner-swiss-receipts-train.json", "r") as f:
    train_dataset = json.load(f)

with open("./data/datasets/ner-swiss-receipts-test.json", "r") as f:
    test_dataset = json.load(f)

# Split the train_dataset (90% of data) into training, validation -> full datasplit of (80 / 10 / 10)
train_data, dev_data = train_test_split(train_dataset, test_size=1/9, random_state=42)
test_data = test_dataset

# Function to convert data to DocBin
def create_doc_bin(data, nlp):
    doc_bin = DocBin()
    for entry in data:
        text = entry["text"]
        entities = entry["entities"]
        doc = nlp.make_doc(text)

        spans = []

        # Convert character indices to token indices
        for start_char, end_char, label in entities:
            # Use char_span to map character indices to token indices
            span = doc.char_span(start_char, end_char, label=label)
            if span is None:
                print(f"Warning: Span could not be aligned for '{text[start_char:end_char]}'")
                continue

            spans.append(span)

        # Add spans to the Doc
        doc.spans["sc"] = spans

        # Add Doc to DocBin
        doc_bin.add(doc)

    return doc_bin

# Create DocBins for train, dev, and test sets
train_doc_bin = create_doc_bin(train_data, nlp)
dev_doc_bin = create_doc_bin(dev_data, nlp)
test_doc_bin = create_doc_bin(test_data, nlp)

# Save DocBins to disk
train_doc_bin.to_disk("./train.spacy")
dev_doc_bin.to_disk("./dev.spacy")
test_doc_bin.to_disk("./test.spacy")