Entity and Relation Extraction using Python
📄 Description

This project demonstrates how to extract named entities and relations from a financial order document using Python.
It focuses on identifying organisations, names, and their corresponding PAN numbers, then maps their relationship as “PAN_Of”.
The extraction process is automated using text parsing and regular expressions, and the final results are saved in a structured CSV file.

🚀 Key Features

Extracts text directly from PDFs using pdfplumber

Identifies entities and PAN numbers with pattern-based regex

Builds automatic relation mappings (e.g., PAN_Of)

Outputs clean, validated data in CSV format

🧠 Tech Stack

Languages & Libraries:
Python • pdfplumber • Regular Expressions (Regex) • CSV

📁 Files Included

Assignment1_extraction.py — Main extraction script

PDF for Python LLM (1).pdf — Input dataset (source document)

extracted_entities_relations.csv — Output file with extracted entities and relations

⚙️ Usage
1. Install dependency
pip install pdfplumber

2. Run the script
python Assignment1_extraction.py

3. View output

Open the generated file:

extracted_entities_relations.csv

🎯 Outcome

This project automates the extraction of PAN-based entity relationships from complex financial or regulatory documents.
It provides a scalable template for entity-relation extraction tasks using open-source tools and standard Python libraries.
