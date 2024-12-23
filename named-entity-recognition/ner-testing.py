import spacy

# Path to the directory where the model was saved
OUTPUT_DIR = "./models/receipts-ner-v01"

# Load the trained model
nlp = spacy.load(OUTPUT_DIR)

# Example text
text = '(fv) Die Gastronomiegruppe\n\nHochschule Luzern\nInformatik 8 Wirtschaft\nC‘o ZFV-Unternehmungen\nFluelastrasse 51\n8047 Zurich\n\nCHF\nPizza Neapolitana 10.50\nRamseier Apfelschor] 3.00\n\nTotal CHF 1,00\n\né MASTERCARD 13,50\n\nMwSt\n\nMwSt Prozent Netto Brutto\n(1) 8.18 12,49 Iaio0 1.0]\n\nProfit Center: TnHouse\n29.11.2024 11:36:49 #:2450 0p:568071 0:56\n8002 $:568\n\nEs bediente Sie - 91 f Check\n\nKopie # ]\n\nCHE-105 827. 102 MWST\nVielen Dank und auf Wiedersehen\n\n'

# Process the text
doc = nlp(text)

# Print recognized entities
print("Entities:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
