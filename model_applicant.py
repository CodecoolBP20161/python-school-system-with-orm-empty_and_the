from model_base import *
from peewee import *
from random import randint


class Applicant(BaseModel):
    name = CharField()
    city = CharField()
    application_code = IntegerField(null=True)
    school = CharField(null=True)
    status = CharField(default="new")

    @classmethod
    def new_applicant(cls):
        object_list = list(cls.select().where(cls.application_code.is_null(True)))
        return object_list

    @classmethod
    def application_code_generator(cls):
        object_list = cls.new_applicant()
        for element in object_list:
            element.application_code = randint(10000, 99999)
            element.save()
