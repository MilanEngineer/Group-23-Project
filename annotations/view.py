import json

# Let `data` be the file path
data = "output_183_annotations.json"  # Replace with your actual file path

# Read and load the data from the file
with open(data, "r", encoding="utf-8") as f:
    annotations = json.load(f)

# Process and display the annotated data
for annotation in annotations:
    text = annotation["text"]
    entities = annotation["entities"]
    
    # Print the text
    print("Text:")
    print(text)
    print("\nEntities:")
    
    # Print each entity with its character positions and label
    for start_char, end_char, label in entities:
        entity_text = text[start_char:end_char]
        print(f" - {entity_text} ({start_char}-{end_char}): {label}")
    
    print("\n" + "="*50 + "\n")
