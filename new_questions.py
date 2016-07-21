# New Question (from random applicants) created into your project database by this script.
# You can run it anytime to generate new Question!

from model_base import *
from model_question import *
from model_applicant import *
from model_answer import *
from new_applicants import *

question1 = Question.create(question="2 + 2 = ?", status="answered", applicant=antal)
question2 = Question.create(question="5 * 6 = ?", status="new", applicant=maria)
question3 = Question.create(question="3 - 7 = ?", status="waiting for answer", applicant=maria)
question4 = Question.create(question="15 * 3 = ?", status="new", applicant=maria)
question5 = Question.create(question="16 / 4 = ?", status="answered", applicant=ilona)
question6 = Question.create(question="10 * 10 = ?", status="answered", applicant=lajos)

answer1 = Answer.create(answer="4", question=question1)
answer1 = Answer.create(answer="4", question=question5)
answer1 = Answer.create(answer="100", question=question6)
