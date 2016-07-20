from model_base import *
from peewee import *


class Applicant(BaseModel):
    name = CharField()
    city = CharField()
    application_code = IntegerField(null=True)
    school = CharField(null=True)
    status = CharField(default="new")

    @classmethod
    def new_applicant(cls):
        object_list = list(cls.select().where(cls.application_code.is_null(True)))
        return(object_list)
