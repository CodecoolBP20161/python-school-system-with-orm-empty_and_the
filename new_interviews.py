from model_base import *
from new_applicants import *
from new_mentors import *


Interview.create(date_time=datetime(2016, 12, 6, 15, 10), mentor=mikimentor, applicant=antal)
Interview.create(date_time=datetime(2016, 8, 7, 13, 20), mentor=danimentor, applicant=maria)
Interview.create(date_time=datetime(2016, 10, 5, 16, 40), mentor=tomimentor, applicant=ilona)
Interview.create(date_time=datetime(2016, 9, 4, 18, 50), mentor=krakowmentor, applicant=lajos)
