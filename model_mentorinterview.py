from model_base import *
from model_mentor import *
from model_interview import *


class MentorInterview(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name="mentorinterview")
    interview = ForeignKeyField(Interview, related_name="interviews")
