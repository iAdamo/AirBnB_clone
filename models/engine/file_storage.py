#!/usr/bin/python3
"""file_storage Module: contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances

You can also test file by file by using this command:
python3 -m unittest tests/test_models/test_file_storage.py
"""

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances

    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
        by <class name>.id

    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        key = class_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            if exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding='utf-8') as\
                                                                        file:
                    attr_dict = json.load(file)
                    for key, value in attr_dict.items():
                        match key[:-37]:
                            case "BaseModel":
                                FileStorage.__objects[key] = BaseModel(**value)
                            case "User":
                                FileStorage.__objects[key] = User(**value)
                            case "State":
                                FileStorage.__objects[key] = State(**value)
                            case "City":
                                FileStorage.__objects[key] = City(**value)
                            case "Amenity":
                                FileStorage.__objects[key] = Amenity(**value)
                            case "Place":
                                FileStorage.__objects[key] = Place(**value)
                            case "Review":
                                FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
