from model_base import *
from model_applicant import *
from model_answers import Answers


class Questions(BaseModel):
    question = CharField()
    status = CharField(default="new")
    related_applicant = ForeignKeyField(Applicant, null=True)
    # related_answer = ForeignKeyField(Answers, null=True)
    related_answer = IntegerField(null=True)
