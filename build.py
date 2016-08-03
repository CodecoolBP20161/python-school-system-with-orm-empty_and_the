# This script can create the database tables based on your models
from model_base import *
from model_applicant import *
from model_school import *
from model_city import *
from model_interview import *
from model_question import *
from model_answer import *
from model_mentor import *
from model_interview_slot import *

db.connect()
# List the tables here what you want to create...
db.drop_tables([Applicant, City, School, Interview, Question, Answer, Mentor, InterviewSlot], safe=True, cascade=True)
db.create_tables([Applicant, City, School, Interview, Question, Answer, Mentor, InterviewSlot], safe=True)
