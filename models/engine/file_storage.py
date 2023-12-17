#!usr/bin/python3
"""Class FileStorage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

class FileStorage:
    """class responsible of storing data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets new object to dictionary __objects"""

        cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        """serializes __objects to json file path"""

        dictio_obj = {}

        for keys, value in FileStorage.__objects.items():
            dictio_obj[keys] = value.to_dict()

        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(json.dumps(dictio_obj))

    def reload(self):
        """deserializes the JSON file to __objects"""

        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as json_file:
                file_str = json_file.read()
                dictio_obj = json.loads(file_str)
                for value in dictio_obj.values():
                    self.new(dct[value['__class__']](**value))
