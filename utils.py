import re
import spacy
from sklearn.externals import joblib  # or import your model directly

nlp = spacy.load("en_core_web_sm")  # Load Spacy model
model = joblib.load('your_model.pkl')  # Load your trained model

def mask_pii(email_body):
    # Define PII patterns
    patterns = {
        "full_name": r"[A-Z][a-z]+ [A-Z][a-z]+",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone_number": r"\+?\d{1,4}?\s?\d{1,4}?\s?\d{4}",
        "dob": r"\d{2}/\d{2}/\d{4}",
        "aadhar_num": r"\d{4}\s\d{4}\s\d{4}",
        "credit_debit_no": r"\d{16}",
        "cvv_no": r"\d{3}",
        "expiry_no": r"\d{2}/\d{2}"
    }
    
    masked_email = email_body
    masked_entities = []

    for entity, pattern in patterns.items():
        matches = re.finditer(pattern, email_body)
        for match in matches:
            masked_email = masked_email.replace(match.group(), f"[{entity}]")
            masked_entities.append({
                "position": [match.start(), match.end()],
                "classification": entity,
                "entity": match.group()
            })

    return masked_email, masked_entities

def classify_email_model(masked_email):
    # Preprocess and classify using your model
    return model.predict([masked_email])[0] 