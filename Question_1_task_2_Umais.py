import os

# Install SpaCy and SciSpaCy
os.system('pip install spacy scispacy')
os.system('pip install en-core-sci-sm')
os.system('pip install https://huggingface.co/allenai/scispacy-models/resolve/main/en_ner_bc5cdr_md-0.4.0.tar.gz')

# Install Transformers and BioBERT
os.system('pip install transformers')

# Now import the libraries and use them
import spacy
from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load SpaCy model
nlp = spacy.load('en_core_sci_sm')

# Define example text
text = "The patient was diagnosed with diabetes and hypertension."

# Process text with SpaCy
doc = nlp(text)
print("SpaCy Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Load BioBERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('dmis-lab/biobert-base-cased-v1.1')
model = BertForTokenClassification.from_pretrained('dmis-lab/biobert-base-cased-v1.1')

# Tokenize input text
inputs = tokenizer(text, return_tensors="pt")

# Perform inference with BioBERT
with torch.no_grad():
    outputs = model(**inputs)

print("\nBioBERT Outputs:")
print(outputs)
