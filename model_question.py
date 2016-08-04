from model_applicant import *
from model_mentor import *
from model_answer import *


class Question(BaseModel):
    question_text = CharField()
    question_status = CharField(default="new")
    applicant = ForeignKeyField(Applicant, related_name="appl_question")
    mentor = ForeignKeyField(Mentor, related_name="mentor_question", null=True)
    date_time = DateTimeField()

    # Answers a question based on the input of a mentor
    @classmethod
    def answer_question(cls, user_input, answer):
        question_object = cls.select().where(cls.id=user_input).get()
        Answer.create(answer_text=answer, question=question_object)
        question_object.status = "answered"
        question_object.save()
