from model_school import *
from model_base import *


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name="workplace")
    mentor_password = IntegerField()
    email = CharField()

    # Return the details of the interviews related to the mentor
    def get_interviews_by_mentor_object(self):
        interviews1 = self.mentor_1
        interviews2 = self.mentor_2
        for element in interviews1:
            yield (element.date_time,
                   element.applicant.application_code, element.applicant.first_name, element.applicant.last_name)
        for element in interviews2:
            yield (element.date_time,
                   element.applicant.application_code, element.applicant.first_name, element.applicant.last_name)

    # Return the mentor as an object by password
    @classmethod
    def get_mentor_object_by_password(cls, user_input):
        return cls.select().where(cls.mentor_password == user_input).get()
