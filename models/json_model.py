import json
from pathlib import Path
from dataclasses import dataclass, asdict

class JsonModel:
    def __init__(self, file_name = "file.json"):
        self.folder = Path("data")
        self.file = self.folder / file_name
        if not self.folder.exists():
            self.folder.mkdir(parents = True)
        if not self.file.exists():
            self.file.touch()
            with open(self.file, "w") as file:
                json.dump([], file, indent=4)

    def write_json(self, data_list):
        with open(self.file, "w") as file:
            data_dicts = []  
            for data in data_list:  
                data_dicts.append(asdict(data))
            json.dump(data_dicts, file, indent=4)

    def read_json(self, class_type):
        with open(self.file, "r") as file:
            data_list = json.load(file)
            if isinstance(data_list, list):
                objects_list = []
                for data in data_list:
                    objects_list.append(class_type(**data))
                return objects_list
            else:
                return [class_type(**data_list)]
