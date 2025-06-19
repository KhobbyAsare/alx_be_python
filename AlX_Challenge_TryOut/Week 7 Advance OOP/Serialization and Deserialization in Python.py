import json

"""
Task
Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

Takes a dictionary (data) and a filename (filename) as input.
Serializes the dictionary to a JSON file with the given filename.
Deserializes the JSON file back into a dictionary.
Returns the deserialized dictionary.

"""

def process_json(data: dict, filename: str) -> dict:
    if not data and not filename:
        raise Exception("Provide the data and the filename")

    with open(filename, 'w') as file:
        json.dump(data, file)

    with open(filename, 'r') as file:
        print(file) # serialized data
        data = json.load(file)

    return data

content = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

print(process_json(content, 'contentjson.txt'))

