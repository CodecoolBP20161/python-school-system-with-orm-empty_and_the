from model_school import *
from model_base import *


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name="workplace")
    mentor_password = IntegerField()

    @classmethod
    def get_mentor_object_by_password(cls, user_input):
        return cls.select().where(cls.mentor_password == user_input).get()
