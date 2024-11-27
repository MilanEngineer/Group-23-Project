import json

def preprocess(data):
    length = len(data['examples'])
    training_length = int(length * 0.7)
    dev_length = int(length * 0.2)
    test_length = int(length * 0.1)

    processed_training = parse_data(data, training_length)
    processed_dev = parse_data(data, dev_length)
    processed_test = parse_data(data, test_length)

    with open('JsonData/trainingData.json', 'w') as f:
        json.dump(processed_training, f)
    with open('JsonData/devData.json', 'w') as f:
        json.dump(processed_dev, f)
    with open('JsonData/testData.json', 'w') as f:
        json.dump(processed_test, f)

def parse_data(data, length):
    processed_data = []

    training_data = data['examples'][:length]

    for curr_content in training_data:
        new_content = {}
        new_content['text'] = curr_content['content']
        new_entities = []
        for j in curr_content['annotations']:
            new_entities.append([j['start'], j['end'], j['tag_name']])


        processed_data.append({
            'text': new_content['text'],
            'entities': new_entities
        })

    return processed_data
    

def main():
    with open('JsonData/rawData.json') as f:
        data = json.load(f)
    preprocess(data)


if __name__ == '__main__':
    main()