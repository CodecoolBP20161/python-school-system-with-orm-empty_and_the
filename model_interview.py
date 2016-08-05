from model_base import *
from model_mentor import *
from model_applicant import *


class Interview(BaseModel):
    date_time = DateTimeField()
    applicant = ForeignKeyField(Applicant, related_name="applicantinterview")

    # Return the details of the interview for the applicant
    @classmethod
    def get_interview_details_by_application_code(cls, user_input):
        interview_object = cls.select(
            Applicant, cls).join(Applicant).where(
            Applicant.application_code == user_input).get()
        yield interview_object.date_time
        yield interview_object.applicant.school.name
        for element in interview_object.interviews:
            yield element.mentor.first_name
            yield element.mentor.last_name
