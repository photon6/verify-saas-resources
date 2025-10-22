from odoo import models
import spacy

class QuasyAnonymizer(models.AbstractModel):
    _name = 'quasy.anonymizer'
    _description = 'QuASy Query Anonymizer'

    def anonymize_text(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        anonymized = text
        for ent in doc.ents:
            anonymized = anonymized.replace(ent.text, f"[{ent.label_}]")
        return anonymized