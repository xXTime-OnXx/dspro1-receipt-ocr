import json
import spacy
from spacy.tokens import Span
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split

# Load a blank SpaCy model
nlp = spacy.blank("de")

# Load Dataset
with open("./data/datasets/ner-swiss-receipts.json", "r") as f:
    dataset = json.load(f)

# Split the dataset into training, validation, and test sets (80/10/10 split)
train_data, temp_data = train_test_split(dataset, test_size=0.2, random_state=42)
dev_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

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