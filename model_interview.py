from model_applicant import *
from model_mentor import *


class Interview(BaseModel):
    date_time = DateTimeField()
    mentor = ForeignKeyField(Mentor)
    applicant = ForeignKeyField(Applicant, related_name="interview")

    @classmethod
    def get_interview_details_by_application_code(cls, user_input):
        interview_object = cls.select(Applicant, cls).join(Applicant).where(Applicant.application_code == user_input).get()
        return (interview_object.applicant.application_code, interview_object.applicant.school.name, interview_object.mentor.first_name, interview_object.mentor.last_name)
