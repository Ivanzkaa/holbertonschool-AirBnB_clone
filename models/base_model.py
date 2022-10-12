#!/usr/bin/python3
"""Before the creation of the class"""


from datetime import datetime
import uuid


t_data = "2017-06-14T22:31:03.285259"
format_dt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Creating the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.strptime(t_data, format_dt)
        self.updated_at = datetime.strptime(t_data, format_dt)
        """datetime.datetime.now().isoformat(format_date_time)"""

    def save(self):
        """updating the public instance with the current\
            datetime"""
        self.updated_at = datetime.now()

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
        return "[{}] ({}) {}".format(self.__class__.__name__,
        self.id, self.__dict__)

