import spacy
import random
from spacy.training.example import Example
import json  # Assuming training data is stored in a JSON file

# Function to load training data from an external JSON file
def load_training_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Transform data into the required format
    training_data = []
    for entry in data:
        text = entry["text"]
        entities = entry["entities"]
        training_data.append((text, {"entities": entities}))
    
    return training_data

def train_ner(data_path, output_dir, iterations=30, batch_size=8, dropout=0.5):
    # Load training data
    print("Loading training data...")
    TRAIN_DATA = load_training_data(data_path)
    
    # print sample
    print("Sample Training Data:")
    sample_text, sample_annotaiton = TRAIN_DATA[0]
    print(sample_text)
    for ent in sample_annotaiton.get("entities"):
        print(f'Entity-Type: {ent[2]}, Entity text: {sample_text[ent[0]:ent[1]]}')
    
    # Load a blank model or pre-trained model
    print("Loading SpaCy model...")
    nlp = spacy.blank("en")  # For a blank model, or replace with spacy.load("en_core_web_sm")
    
    # Add the NER pipeline component if not already present
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")
    
    # Add labels to the NER
    print("Adding entity labels...")
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])
    
    # Convert training data to SpaCy Example format
    examples = [
        Example.from_dict(nlp.make_doc(text), annotations) for text, annotations in TRAIN_DATA
    ]
    
    # Disable other pipes during training for efficiency
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        
        # Training loop
        print("Starting training...")
        for epoch in range(iterations):
            random.shuffle(examples)
            losses = {}
            for batch in spacy.util.minibatch(examples, size=batch_size):
                nlp.update(batch, drop=dropout, losses=losses)
            print(f"Epoch {epoch + 1}/{iterations}, Loss: {losses['ner']:.4f}")
    
    # Save the trained model
    print(f"Saving model to {output_dir}...")
    nlp.to_disk(output_dir)
    print("Training complete!")

if __name__ == "__main__":
    # Define paths and parameters
    DATA_PATH = "./pocs/spacy-ner/training/training_data.json"  # Path to your training data file
    OUTPUT_DIR = "./pocs/spacy-ner/trained_ner_model"  # Path to save the trained model
    ITERATIONS = 30  # Number of training iterations
    BATCH_SIZE = 8  # Batch size for training
    DROPOUT = 0.5  # Dropout rate
    
    # Train the NER model
    train_ner(DATA_PATH, OUTPUT_DIR, iterations=ITERATIONS, batch_size=BATCH_SIZE, dropout=DROPOUT)
