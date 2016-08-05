from model_school import *
from model_base import *


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name="workplace")
    mentor_password = IntegerField()
    email = CharField()

    # Yield question details for a mentor object
    def get_question_data_for_mentor(self):
        for element in self.mentor_question:
            if element.question_status == "waiting for answer":
                yield (element.id, element.date_time, element.applicant.application_code, element.question_text)

    # Yield the details of the interviews related to the mentor
    def get_interviews_by_mentor_object(self):
        for element in self.mentorinterview:
            yield (element.interview.date_time, element.interview.applicant.application_code,
                   element.interview.applicant.first_name, element.interview.applicant.last_name)

    # Return the mentor as an object by password
    @classmethod
    def get_mentor_object_by_password(cls, user_input):
        return cls.select().where(cls.mentor_password == user_input).get()
