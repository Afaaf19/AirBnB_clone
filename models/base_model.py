#!usr/bin/python3
"""the base classe"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """this classe is the main class that all the subclasses inherits from"""
    def __init__(self, *args, **kwargs):
        """constructor"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    f = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, f))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """class string returning the string format"""

        return ("[{}] ({}) {}"
                "".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ updates the last updated time to now"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary"""

        dictio = self.__dict__.copy()
        dictio["__class__"] = self.__class__.__name__
        dictio["created_at"] = str(datetime.isoformat(self.created_at))
        dictio["updated_at"] = str(datetime.isoformat(self.updated_at))
        return dictio
