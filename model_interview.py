from model_base import *
from model_mentor import *
from model_applicant import *


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
