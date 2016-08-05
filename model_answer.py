from model_question import *
from model_applicant import *
from model_mentor import *


class Answer(BaseModel):
    answer_text = CharField()
    question = ForeignKeyField(Question, related_name="appl_answer")

    # Return the question, question_status and answer (if it exists) related to the applicant
    @classmethod
    def get_answers_by_application_code(cls, user_input):
        answers = cls.select(
            Applicant,
            Question,
            cls).join(
            Question,
            JOIN.RIGHT_OUTER).join(Applicant).where(
            Applicant.application_code == user_input)
        for element in answers:
            yield (element.question.question_text,
                   element.question.question_status, element.answer_text)

    # Answers a question based on the input of a mentor
    @classmethod
    def answer_question(cls, user_input, answer, mentor_id):
        question_object = Question.select().join(Mentor).where(Question.id == user_input,
                                                               Question.question_status == "waiting for answer",
                                                               Mentor.id == mentor_id).get()
        cls.create(answer_text=answer, question=question_object)
        question_object.question_status = "answered"
        question_object.save()
