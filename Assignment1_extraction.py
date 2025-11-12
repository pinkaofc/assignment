
# Assignment 1: Entity and Relation Extraction using Python



import pdfplumber
import re
import csv
from pathlib import Path

pdf_path = Path("PDF for Python LLM (1).pdf")
output_csv = Path("extracted_entities_relations.csv")

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_entities_and_relations(text):
    pattern = r"(\d+\.\s+)([A-Z\s\(\)\.&\-]+?)\s+([A-Z]{5}[A-Z0-9]{4}[A-Z])"
    matches = re.findall(pattern, text)
    
    extracted_data = []
    for _, name, pan in matches:
        clean_name = name.strip().replace("\n", " ").replace("  ", " ")
        clean_pan = pan.strip()
        extracted_data.append((clean_pan, "PAN_Of", clean_name))
    return extracted_data

def save_to_csv(data, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Entity (PAN)", "Relation", "Entity (Person/Org)"])
        writer.writerows(data)

def main():
    if not pdf_path.exists():
        print("PDF file not found. Please check the path.")
        return

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    print("Extracting entities and relations...")
    data = extract_entities_and_relations(text)

    if not data:
        print("No entities or relations found. Please verify the input PDF.")
        return

    save_to_csv(data, output_csv)
    print(f"Extraction complete. Results saved in '{output_csv.name}'")
    print(f"Total records extracted: {len(data)}")

if __name__ == "__main__":
    main()
