#Project Title: Entity and Relation Extraction using Python#

Description:
This project extracts named entities and relations from a financial order document using Python. It focuses on identifying organisations, names, and their corresponding PAN numbers, then builds the relationship “PAN_Of” between them. The extraction is automated using text parsing and regular expressions, and the results are stored in a structured CSV format.

Key Features:

PDF text extraction using pdfplumber

Pattern-based entity recognition with regex

Automatic relation mapping (e.g., PAN_Of)

Clean and validated CSV output

Tech Stack:
Python, pdfplumber, Regular Expressions (Regex), CSV

Files Included:

Assignment1_extraction.py — main extraction script

PDF for Python LLM (1).pdf — input dataset

extracted_entities_relations.csv — output file

Usage:

Install dependency:

pip install pdfplumber


Run the script:

python Assignment1_extraction.py


View results in extracted_entities_relations.csv.

Outcome:
Efficient extraction of PAN-based entity relationships from complex regulatory text using open-source tools.
