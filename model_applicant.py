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
                element.application_code = cls.get_free_application_code(object_list)
                element.save()

    @classmethod
    def closest_school(cls):
        object_list = cls.new_applicant()
        for element in object_list:
            element.school = element.city.school
            element.status = "in progress"
            element.save()

    @staticmethod
    def get_free_application_code(object_list):
        while True:
            continue_boolean = False
            random_code = randint(10000, 99999)
            for element in object_list:
                if element.application_code == random_code:
                    continue_boolean = True
            if continue_boolean is True:
                continue
            return random_code
