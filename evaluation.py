import spacy

nlp_trained_model = spacy.load("output/model-best")
doc = nlp_trained_model('''
The patient was prescribed Aspirin for their heart condition.
The doctor recommended Ibuprofen to alleviate the patient's headache.
The patient is suffering from diabetes, and they need to take Metformin regularly.
After the surgery, the patient experienced some post-operative complications, including infection.
The patient is currently on a regimen of Lisinopril to manage their high blood pressure.
The antibiotic course for treating the bacterial infection should be completed as prescribed.
The patient's insulin dosage needs to be adjusted to better control their blood sugar levels.
The physician suspects that the patient may have pneumonia and has ordered a chest X-ray.
The patient's cholesterol levels are high, and they have been advised to take Atorvastatin.
The allergy to penicillin was noted in the patient's medical history.
''')
print(doc.ents)
spacy.displacy.render(doc, style="ent", jupyter=True)