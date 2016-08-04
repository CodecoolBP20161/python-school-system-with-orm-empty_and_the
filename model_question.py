from model_applicant import *
from model_mentor import *


class Question(BaseModel):
    question_text = CharField()
    question_status = CharField(default="new")
    applicant = ForeignKeyField(Applicant, related_name="appl_question")
    mentor = ForeignKeyField(Mentor, related_name="mentor_question", null=True)
