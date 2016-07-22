from model_applicant import *


class Question(BaseModel):
    question_text = CharField()
    question_status = CharField(default="new")
    applicant = ForeignKeyField(Applicant, related_name="appl_question")
