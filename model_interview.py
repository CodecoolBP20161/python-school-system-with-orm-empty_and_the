from model_applicant import *
from model_mentor import *


class Interview(BaseModel):
    date_time = DateTimeField()
    mentor_1 = ForeignKeyField(Mentor, related_name="mentor_1")
    mentor_2 = ForeignKeyField(Mentor, related_name="mentor_2")
    applicant = ForeignKeyField(Applicant, related_name="interview")

    @classmethod
    def get_interview_details_by_application_code(cls, user_input):
        interview_object = cls.select(
            Applicant, cls).join(Applicant).where(
            Applicant.application_code == user_input).get()
        return (
            interview_object.date_time,
            interview_object.applicant.school.name,
            interview_object.mentor_1.first_name,
            interview_object.mentor_1.last_name,
            interview_object.mentor_2.first_name,
            interview_object.mentor_2.last_name)

    @classmethod
    def get_interviews_by_password(cls, user_input):
        interviews = cls.select(
            Mentor,
            cls).join(Mentor).where(
            cls.mentor_1.mentor_password == user_input or cls.mentor_2.mentor_password == user_input)
        for element in interviews:
            yield (element.date_time,
                   element.applicant.application_code, element.applicant.first_name, element.applicant.last_name)
