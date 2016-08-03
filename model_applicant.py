from model_city import *
from random import randint

class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    city = ForeignKeyField(City, related_name="home")
    application_code = IntegerField(null=True)
    school = ForeignKeyField(School, null=True, related_name="school")
    status = CharField(default="new")
    has_interview = BooleanField(default=False)

    # Return the applicant as an object by application_code
    @classmethod
    def get_applicant_object_by_application_code(cls, appl_code):
        return cls.select().where(cls.application_code == appl_code).get()

    # Return the list of the applicants, who haven't got application_code yet (list of objects)
    @classmethod
    def get_new_applicants_by_city(cls):
        object_list = list(cls.select().where(cls.city.is_null(True)))
        return object_list

    @classmethod
    def get_new_applicants_by_application_code(cls):
        object_list = list(cls.select().where(cls.application_code.is_null(True)))
        return object_list

    @classmethod
    def get_applicants_without_interview(cls):
        # used subpress warning(# noqa) because issue: https://github.com/coleifer/peewee/issues/612
        object_list = list(cls.select().where(cls.has_interview == False))  # noqa
        return object_list

    # Save the application_code to the new_applicant from the object_list
    @classmethod
    def application_code_generator(cls):
        for element in cls.get_new_applicants_by_application_code():
                element.application_code = cls.get_free_application_code()
                element.save()

    # Get the closest school and save it to the new_applicant from the object_list
    @classmethod
    def get_closest_school(cls):
        for element in cls.get_new_applicants_by_city():
            element.school = element.city.school
            element.status = "in progress"
            element.save()

    # Create a unique application_code
    @classmethod
    def get_free_application_code(cls):
        while True:
            continue_boolean = False
            random_code = randint(10000, 99999)
            for element in cls.get_new_applicants_by_application_code():
                if element.application_code == random_code:
                    continue_boolean = True
            if continue_boolean is True:
                continue
            return random_code
