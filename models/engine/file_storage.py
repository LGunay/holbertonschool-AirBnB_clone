#!usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        name = obj.__class__.__name__ 
        self.__objects[f"{name}.{obj.id}"] = obj
    
    def save(self):
        file = self.__file_path
        objd = self.__objects
        newD = {}
        for k, v in objd.items():
            newD[k] = v.to_dict()

        with open(file, "w") as f:
            json.dump(newD, f)

    def reload(self):
        file = self.__file_path

        try:
            with open(file, "r") as f:
                data = json.load(f)
            for k in data:
                self.__objects[k] = BaseModel(**data[k])
        except FileNotFoundError:
            pass
