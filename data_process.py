import json

# Load data from 'kaggle corpus.json'
with open("kaggle corpus.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Process data and write to 'processed_data.txt'
with open("processed_data.txt", "w", encoding="utf-8") as output_file:
    for example in data.get("examples", []):
        example_id = example.get("id", "N/A")
        content = example.get("content", "N/A").replace('\n', ' ')

        output_file.write(f"Example ID: {example_id}\n")
        output_file.write(f"Content: {content}\n")
        
        # Process annotations
        annotations = example.get("annotations", [])
        if annotations:
            output_file.write("Annotations:\n")
            for annotation in annotations:
                annotation_id = annotation.get("id", "N/A")
                tag_name = annotation.get("tag_name", "N/A")
                value = annotation.get("value", "N/A")
                start = annotation.get("start", "N/A")
                end = annotation.get("end", "N/A")
                
                output_file.write(f"  - Annotation ID: {annotation_id}\n")
                output_file.write(f"    Tag Name: {tag_name}\n")
                output_file.write(f"    Value: {value}\n")
                output_file.write(f"    Start: {start}\n")
                output_file.write(f"    End: {end}\n")
        
        output_file.write("\n")  


