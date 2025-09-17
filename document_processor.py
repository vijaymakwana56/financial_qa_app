import pandas as pd
import pdfplumber
import tempfile

def process_document(file):
    if file.name.endswith(".pdf"):
        return extract_from_pdf(file)
    elif file.name.endswith(".xlsx"):
        return extract_from_excel(file)
    else:
        return {}

def extract_from_pdf(file):
    text_data = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text_data.append(page.extract_text())
    return {"text": "\n".join(text_data)}

def extract_from_excel(file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    df = pd.read_excel(tmp_path)
    return {"dataframe": df.to_dict(orient="records")}
