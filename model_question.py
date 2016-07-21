from model_base import *
from model_applicant import *


class Question(BaseModel):
    question = CharField()
    status = CharField(default="new")
    applicant = ForeignKeyField(Applicant, related_name="question")
