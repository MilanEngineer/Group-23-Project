# Group-23-Project: Medical Named Entity Recognition (NER) Model

This project trains and tests a Named Entity Recognition (NER) model for medical texts using spaCy.

## Prerequisites

- Python 3.6+
- spaCy library
- en_core_web_lg model for spaCy

## Installation

1. Clone or download this repository
2. Install the required packages:
```pip install spacy```
3. Download the en_core_web_lg model:
```python -m spacy download en_core_web_lg```

## File Structure

- `main.py`: The main script containing the code for training and testing the model
- `trainingData.json`: JSON file containing the training data
- `sample_medical_text.txt`: Text file containing sample medical text for testing
- `config.cfg`: Configuration file for spaCy training (will be created during setup)

## Usage

1. Initialize the spaCy configuration:
```python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy```

2. Train the model:
```python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy```

4. Run the script:
```python model.py```

## Output

The script generates a `test_output.txt` file containing the recognized entities in the following format:

entity_text label start_character end_character
