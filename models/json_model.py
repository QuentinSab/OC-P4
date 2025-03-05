import json
from pathlib import Path
from dataclasses import asdict


class JsonModel:
    def __init__(self, file_name="file.json"):
        self.folder = Path("data")
        self.file = self.folder / file_name

        # Create the data folder if it doesn't exist
        if not self.folder.exists():
            self.folder.mkdir(parents=True)

        # Create an empty JSON file if it doesn't exist
        if not self.file.exists():
            self.file.touch()
            with open(self.file, "w") as file:
                json.dump([], file, indent=4)

    def write_json(self, data_list):
        """Write a list of objects to the JSON file"""
        with open(self.file, "w") as file:
            data_dicts = []

            # Convert each object to a dictionary
            for data in data_list:
                data_dicts.append(asdict(data))

            json.dump(data_dicts, file, indent=4)

    def write_dict_json(self, data_dicts):
        """Write a list of dictionaries to the JSON file"""
        with open(self.file, "w") as file:
            json.dump(data_dicts, file, indent=4)

    def read_json(self, class_type):
        """Read JSON data and convert it to a list of objects of the given class type"""
        with open(self.file, "r") as file:
            data_list = json.load(file)

            if isinstance(data_list, list):
                objects_list = []

                for data in data_list:
                    # Add objects from dictionaries to the list
                    objects_list.append(class_type(**data))

                return objects_list
            else:
                # Handle the case of a single dictionary
                return [class_type(**data_list)]
