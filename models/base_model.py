#!/usr/bin/python3
"""Before the creation of the class"""


from datetime import datetime
import models
import uuid


t_data = "2017-06-14T22:31:03.285259"
format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Creating the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class"""
        if len(kwargs) > 0:
            for key, t_data in kwargs.items():
                """initializing the loop to itirate through\
                    the items of the kwargs"""
                if key == "created_at":
                    """if the key if == to created_at\
                        it will create an instance for the \
                        datetime of the created_at"""
                    self.created_at = datetime.strptime(t_data, format_dt)
                elif key == "updated_at":
                    """if the key == update it will\
                        create an instance of the time_data\
                        for the update"""
                    self.updated_at = datetime.strptime(t_data, format_dt)
                elif key != "__class__":
                    """if the key does not == class\
                    it will set the attributes for the id,\
                    the key and the time data"""
                    setattr(self, key, t_data)
        else:
            """the random instances created"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """updating the public instance with the current\
            datetime"""
        self.updated_at = datetime.now()
        """calling the method save(self) of storage"""
        models.storage.save()

    def to_dict(self):
        """the dict method and its key value and pairs"""
        dic = {
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.strftime(format_dt),
            'id': self.id,
            'created_at': self.created_at.strftime(format_dt)
        }
        return dic

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
