from model_base import *
from model_mentor import *
from model_interview import *


class MentorInterview(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name="mentorinterview")
    interview = ForeignKeyField(Interview, related_name="interviews")

    @classmethod
    def get_all_interviews(cls):
        for element in cls.select():
            yield (element.mentor.first_name + ' ' + element.mentor.last_name, element.interview.date_time,
                   element.interview.applicant.first_name + ' ' + element.interview.applicant.last_name,
                   element.interview.applicant.school.name)
