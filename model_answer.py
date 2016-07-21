from model_base import *
from model_question import *


class Answer(BaseModel):
    answer = CharField()
    question = ForeignKeyField(Question, related_name="answer")
