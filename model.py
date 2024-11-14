import spacy # importing spacy library
from spacy.tokens import DocBin # importing DocBin from spacy.tokens
import json # importing json library
from spacy.util import filter_spans

def create_model(fileName, type):
    with open(fileName) as f:
        data = json.load(f) # loading the data from the json file

    nlp = spacy.load('en_core_web_sm') # loading the model
    doc_bin = DocBin() # creating a DocBin object


    for example in data:
        text = example['text']
        annotations = example['entities']

        doc = nlp.make_doc(text)
        ents = []

        for i in annotations:
            snippet = doc.char_span(i[0], i[1], label=i[2], alignment_mode="contract")
            if snippet:
                ents.append(snippet)
        filtered_ents = filter_spans(ents)
        doc.set_ents(filtered_ents)
        doc_bin.add(doc)

    #doc_bin.to_disk((type+".spacy"))

    """
    nlp_trained_model = spacy.load("output/model-best")
    doc = nlp_trained_model(''' medical text ''')
    if doc.ents:
        spacy.displacy.serve(doc, style="ent", auto_select_port=True)
    else:
        print("No entities found")
    """

create_model('trainingData.json', 'train')

# python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy