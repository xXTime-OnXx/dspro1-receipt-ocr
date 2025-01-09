import json

import spacy
from spacy.tokens import Span
from spacy.tokens import DocBin

# Load a blank SpaCy model
nlp = spacy.blank("de")

# Load Dataset
with open("./data/datasets/ner-swiss-receipts.json", "r") as f:
    dataset = json.load(f)

# Initialize DocBin
doc_bin = DocBin()

for entry in dataset:
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

# Save DocBin to disk
doc_bin.to_disk("./training_data.spacy")