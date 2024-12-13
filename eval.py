from collections import namedtuple

Entity = namedtuple("Entity", ["text", "label"])

'''
reads a file and returns a list of entity 
tuples which include the text and its label
'''
def read_entities(file_path):
    entities = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Ignore empty lines
                word = line.split('\t')
                text = word[0]
                label = word[1]
                entities.append(Entity(text, label))
    return entities

'''
calculates precision, recall, and F1 score based on exact matches
of text and labels in the answer key and output files
'''
def calculate_metrics(key_entities, response_entities):
  
    correct = 0
    for response in response_entities:
        if response in key_entities:
            correct += 1
    
    total_predicted = len(response_entities)
    total_actual = len(key_entities)

    #Precision, Recall, and F1 score calculations
    precision = (correct / total_predicted) * 100 if total_predicted > 0 else 0.0
    recall = (correct / total_actual) * 100 if total_actual > 0 else 0.0
    f1_score = (2/ (1/precision + 1/recall)) if (precision + recall) > 0 else 0.0

    print(f"Correct matches: {correct}")
    print(f"System output total: {total_predicted}")
    print(f"Answer key total: {total_actual}")
    print(f"Precision: {precision:.2f}%")
    print(f"Recall: {recall:.2f}%")
    print(f"F1: {f1_score:.2f}%")

def main():
    #read key and response entities
    key_entities = read_entities('key_output.txt') #key_output is generated from testData.json
    response_entities = read_entities('OtherFormatData/test_output.txt')#test_output is geneerated from sample_medical_text_data

    #calculate and print metrics
    calculate_metrics(key_entities, response_entities)

if __name__ == "__main__":
    main()
        
