import json
from pathlib import Path

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
                data_dicts.append(data.__dict__)
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

    def append_json(self, data):
        existing_data = self.read_json(type(data))
        existing_data.append(data)
        self.write_json(existing_data)
        
    def generate_id(self, json_data):
        used_ids = set()
        for object in json_data:
            used_ids.add(object.id)
        id = 1
        while id in used_ids:
            id += 1
        return id

    def get_object_by_id(self, id, json_data):
        for object in json_data:
            if object.id == id:
                return object
        return None