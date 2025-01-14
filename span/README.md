## Training a Span Classifier with Spacy

### Training Data
First we need to prepare the training data in a spacy readble format. This is done in the `./training/preprocess.py` python script.

### Training
In order to train a classifier we can use the spacy cli:
```bash
python -m spacy train config.cfg --output ./output --paths.train ./training/train.spacy --paths.dev ./training/dev.spacy
```

### Evaluation
```bash
python -m spacy evaluate ./output/model-best ./test.spacy --output ./metrics.json
```