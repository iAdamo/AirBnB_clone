#!/usr/bin/env python3
"""
base_model module: contains a class `BaseModel` that defines all common
attributes/methods for other classes

You can also test file by file by using this command:
python3 -m unittest tests/test_models/test_base_model.py
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    BaseModel class: defines all common attributes/methods for other classes
    """
    def _init_(self):
        """
        Initialize a BaseModel instance

        Args:
            id: (string) - assign with an uuid when an instance is created

            created_at: (datetime) - assign with the current datetime
            when an instance is created

            updated_at: (datetime) - assign with the current datetime when an
            instance is created and it will be updated every time you change
            your object
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def _str_(self):
        """
        return an informal string representation of an instance

        Return:
            str: string representation of BaseModel atttributes
        """
        return f"[{_class.__name}] ({self.id}) {self.__dict_}"

    def save(self):
        """
        updates the public instance attribute `updated_at` with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        _dict_ of the instance

        Return:
            dict: dictionary containing the attributes of BaseModel
        """
        self._dict["__class"] = __class.__name_
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self._dict_
