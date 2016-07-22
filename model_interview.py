from model_applicant import *
from model_mentor import *


class Interview(BaseModel):
    date_time = DateTimeField()
    mentor = ForeignKeyField(Mentor)
    applicant = ForeignKeyField(Applicant, related_name="interview")

    @classmethod
    def get_interview_details_by_application_code(cls, user_input):
        interview_object = cls.select(
            Applicant, cls).join(Applicant).where(
            Applicant.application_code == user_input).get()
        return (
            interview_object.date_time,
            interview_object.applicant.school.name,
            interview_object.mentor.first_name,
            interview_object.mentor.last_name)

    @classmethod
    def get_interviews_by_password(cls, user_input):
        interviews = cls.select(
            Mentor,
            cls).join(Mentor).where(
            Mentor.mentor_password == user_input)
        for element in interviews:
            yield (element.date_time,
                   element.applicant.application_code, element.applicant.first_name, element.applicant.last_name)
