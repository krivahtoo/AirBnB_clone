#!/usr/bin/python3
"""defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    val = datetime.fromisoformat(val)
                self.__dict__[key] = val
        else:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """return string represention"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        obj = {}

        for key, val in self.__dict__.items():
            if type(val) == datetime:
                obj[key] = val.isoformat()
            else:
                obj[key] = val
        obj['__class__'] = self.__class__.__name__

        return obj
