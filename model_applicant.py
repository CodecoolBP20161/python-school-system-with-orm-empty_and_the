from model_base import *
from model_school import *
from model_city import *
from peewee import *
from random import randint


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    city = ForeignKeyField(City, related_name="home")
    application_code = IntegerField(null=True)
    school = ForeignKeyField(School, null=True, related_name="school")
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

    @classmethod
    def closest_school(cls):
        object_list = cls.new_applicant()
        for element in object_list:
            print(element.school, element.city.school)
            element.school = element.city.school
            element.save()
