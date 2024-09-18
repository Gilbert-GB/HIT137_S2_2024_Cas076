import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Function to extract entities using SciSpaCy
def extract_entities_scispacy(file_path, model_name):
    # Load SciSpaCy model
    nlp = spacy.load(model_name)
    
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Process the text and extract entities
    doc = nlp(text)
    diseases = []
    drugs = []

    for ent in doc.ents:
        if ent.label_ == "DISEASE":
            diseases.append(ent.text)
        elif ent.label_ == "CHEMICAL":
            drugs.append(ent.text)

    return diseases, drugs

# Function to extract entities using BioBERT
def extract_entities_biobert(file_path):
    # Load the BioBERT model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
    model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
    
    # Initialize pipeline for NER
    nlp = pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)
    
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract entities using BioBERT
    ner_results = nlp(text)
    diseases = []
    drugs = []

    # Filter entities by disease and drugs
    for entity in ner_results:
        if 'disease' in entity['entity'].lower():
            diseases.append(entity['word'])
        elif 'drug' in entity['entity'].lower():
            drugs.append(entity['word'])

    return diseases, drugs

# Function to compare results between SciSpaCy and BioBERT
def compare_ner_results(scispacy_diseases, scispacy_drugs, biobert_diseases, biobert_drugs):
    print("\n--- Comparison ---")
    
    # Compare diseases
    print("\nDiseases detected by SciSpaCy:", len(scispacy_diseases))
    print(scispacy_diseases)
    print("\nDiseases detected by BioBERT:", len(biobert_diseases))
    print(biobert_diseases)

    # Compare drugs
    print("\nDrugs detected by SciSpaCy:", len(scispacy_drugs))
    print(scispacy_drugs)
    print("\nDrugs detected by BioBERT:", len(biobert_drugs))
    print(biobert_drugs)

# Main function to run the NER and comparison
def main():
    file_path = "CSV1.txt"  # Your input text file
    
    # Extract entities using SciSpaCy models
    print("\nExtracting entities using SciSpaCy (en_core_sci_sm)...")
    sci_diseases_sm, sci_drugs_sm = extract_entities_scispacy(file_path, "en_core_sci_sm")
    
    print("\nExtracting entities using SciSpaCy (en_ner_bc5cdr_md)...")
    sci_diseases_bc5cdr, sci_drugs_bc5cdr = extract_entities_scispacy(file_path, "en_ner_bc5cdr_md")
    
    # Extract entities using BioBERT
    print("\nExtracting entities using BioBERT...")
    bio_diseases, bio_drugs = extract_entities_biobert(file_path)
    
    # Compare SciSpaCy and BioBERT results
    compare_ner_results(sci_diseases_bc5cdr, sci_drugs_bc5cdr, bio_diseases, bio_drugs)

# Run the main function
if __name__ == "__main__":
    main()