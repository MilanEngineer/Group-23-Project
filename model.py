import spacy # importing spacy library
import spacy.displacy
from spacy.tokens import DocBin # importing DocBin from spacy.tokens
import json # importing json library
from spacy.util import filter_spans

def create_training_data(inputFile, outputFile):
    with open('JsonData/trainingData.json') as f:
        data = json.load(f) # loading the data from the json file

    nlp = spacy.load('en_core_web_lg') # loading the model
    doc_bin = DocBin() # creating a DocBin object


    for example in data:
        text = example['text']
        annotations = example['entities']

        doc = nlp.make_doc(text)
        ents = []

        for i in annotations:
            snippet = doc.char_span(i[0], i[1], label=i[2])
            if snippet is not None:
                ents.append(snippet)
        filtered_snippets = filter_spans(ents)
        doc.set_ents(filtered_snippets)
        doc_bin.add(doc)

    doc_bin.to_disk(outputFile) # saving the data to a file


def test_model(path, medicalText):
    trained_model = spacy.load(path) # loading the trained model
    doc = trained_model(medicalText) # passing the medical text to the model


    with open('OtherFormatData/test_output.txt', 'w') as f:
        if doc.ents:
            for ent in doc.ents:
                f.write(f'{ent.text}\t{ent.label_}\t{ent.start_char}\t{ent.end_char}\n')
        else:
            f.write("No entities found.\n")



#create_training_data('JsonData/trainingData.json', 'train.spacy')

with open('OtherFormatData/sample_medical_text.txt', 'r') as file:
    medicalText = file.read()

test_model('output/model-best', medicalText)

# python -m spacy download en_core_web_lg
# python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy
# python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy