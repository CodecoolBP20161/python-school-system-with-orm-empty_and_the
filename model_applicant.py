from model_city import *
from random import randint


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    city = ForeignKeyField(City, related_name="home")
    application_code = IntegerField(null=True)
    school = ForeignKeyField(School, null=True, related_name="school")
    status = CharField(default="new")

    # Return the applicant as an object by application_code
    @classmethod
    def get_applicant_object_by_application_code(cls, appl_code):
        return cls.select().where(cls.application_code == appl_code).get()

    # Return the list of the applicants, who haven't got application_code yet (list of objects)
    @classmethod
    def new_applicant(cls):
        object_list = list(cls.select().where(cls.application_code.is_null(True)))
        return object_list

    # Save the application_code to the new_applicant from the object_list
    @classmethod
    def application_code_generator(cls, object_list):
        for element in object_list:
                element.application_code = cls.get_free_application_code(object_list)
                element.save()

    # Get the closest school and save it to the new_applicant from the object_list
    @classmethod
    def get_closest_school(cls, object_list):
        for element in object_list:
            element.school = element.city.school
            element.status = "in progress"
            element.save()

    # Create a unique application_code
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
