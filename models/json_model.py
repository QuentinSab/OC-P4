import json
from pathlib import Path

class JsonModel:
    def __init__(self, file_name = "file.json"):
        self.folder = Path("data")
        self.file = self.folder / file_name    
        if not self.folder.exists():
            self.folder.mkdir(parents = True)

    def write_json(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def read_json(self):
        with open(self.file, "r") as file:
            return json.load(file)

    def append_json(self, data):
        existing_data = self.read_json()
        if isinstance(existing_data, list):
            existing_data.append(data.__dict__)
        else:
            existing_data = [existing_data, data.__dict__]
        self.write_json(existing_data)


