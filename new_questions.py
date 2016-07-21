# New Question (from random applicants) created into your project database by this script.
# You can run it anytime to generate new Question!

from model_base import *
from model_question import *
from model_applicant import *
from model_answer import *
from new_applicants import *

question1 = Question.create(question_text="2 + 2 = ?", question_status="answered", applicant=antal)
question2 = Question.create(question_text="5 * 6 = ?", question_status="new", applicant=maria)
question3 = Question.create(question_text="3 - 7 = ?", question_status="waiting for answer", applicant=maria)
question4 = Question.create(question_text="15 * 3 = ?", question_status="new", applicant=maria)
question5 = Question.create(question_text="16 / 4 = ?", question_status="answered", applicant=ilona)
question6 = Question.create(question_text="10 * 10 = ?", question_status="answered", applicant=lajos)

answer1 = Answer.create(answer_text="4", question=question1)
answer1 = Answer.create(answer_text="4", question=question5)
answer1 = Answer.create(answer_text="100", question=question6)
