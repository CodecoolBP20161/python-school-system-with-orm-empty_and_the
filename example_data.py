# This script drops all tables and generates news with some data for testing

# import build for drop and create tables
from build import *

# import needed libraries
from datetime import datetime

# generating schools
class_budapest = School.create(name="CodecoolBudapest")
class_miskolc = School.create(name="CodecoolMiskolc")
class_krakow = School.create(name="CodecoolKrakow")

# generating cities
city_kaposvar = City.create(name="Kaposvár", school=class_budapest)
city_erd = City.create(name="Érd", school=class_budapest)
city_visegrad = City.create(name="Visegrád", school=class_budapest)
city_veszprem = City.create(name="Veszprém", school=class_budapest)
city_sopron = City.create(name="Sopron", school=class_budapest)
city_kecskemet = City.create(name="Kecskemét", school=class_budapest)
city_gyor = City.create(name="Győr", school=class_budapest)
city_godollo = City.create(name="Gödöllő", school=class_budapest)
city_hatvan = City.create(name="Hatvan", school=class_budapest)
city_vac = City.create(name="Vác", school=class_budapest)
city_eger = City.create(name="Eger", school=class_miskolc)
city_nyiregyhaza = City.create(name="Nyíregyháza", school=class_miskolc)
city_debrecen = City.create(name="Debrecen", school=class_miskolc)
city_kiskoros = City.create(name="Kiskőrös", school=class_miskolc)
city_gyula = City.create(name="Gyula", school=class_miskolc)
city_hajduszoboszlo = City.create(name="Hajdúszoboszló", school=class_miskolc)
city_kassa = City.create(name="Kassa", school=class_miskolc)
city_wieliczka = City.create(name="Wieliczka", school=class_krakow)
city_liszki = City.create(name="Liszki", school=class_krakow)
city_katowice = City.create(name="Katowice", school=class_krakow)
city_varso = City.create(name="Varsó", school=class_krakow)
city_berlin = City.create(name="Berlin", school=class_krakow)

# generating mentors
danimentor = Mentor.create(first_name="Dániel", last_name="Salamon", school=class_budapest, mentor_password=111111)
mikimentor = Mentor.create(first_name="Miklós", last_name="Beöthy", school=class_budapest, mentor_password=222222)
tomimentor = Mentor.create(first_name="Tamás", last_name="Tompa", school=class_budapest, mentor_password=333333)
miskolcmentor = Mentor.create(first_name="Mihály", last_name="Miskolc", school=class_miskolc, mentor_password=444444)
krakowmentor = Mentor.create(first_name="Károly", last_name="Krakow", school=class_krakow, mentor_password=555555)

# generate new applicants without application_code
Applicant.create(first_name="Smith", last_name="John", city=city_varso)
Applicant.create(first_name="Smith", last_name="Jane", city=city_liszki)
Applicant.create(first_name="Smith", last_name="Johnny", city=city_berlin)
Applicant.create(first_name="Kovács", last_name="János", city=city_debrecen)
Applicant.create(first_name="Molnár", last_name="László", city=city_debrecen)

# generate applicants with given parameters for testing
antal = Applicant.create(
    first_name="Szűcs",
    last_name="Antal",
    city=city_gyor,
    application_code=11111,
    school=class_budapest,
    status="in progress")
maria = Applicant.create(
    first_name="Kocsis",
    last_name="Mária",
    city=city_hatvan,
    application_code=22222,
    school=class_budapest,
    status="in progress")
python = Applicant.create(
    first_name="Monthy",
    last_name="Python",
    city=city_hatvan,
    application_code=33333,
    school=class_miskolc,
    status="in progress")
ilona = Applicant.create(
    first_name="Szabó",
    last_name="Ilona",
    city=city_sopron,
    application_code=44444,
    school=class_krakow,
    status="in progress")
lajos = Applicant.create(
    first_name="Tóth",
    last_name="Lajos",
    city=city_sopron,
    application_code=55555,
    school=class_krakow,
    status="in progress")

# generate questions
question1 = Question.create(question_text="2 + 2 = ?", question_status="answered", applicant=antal)
question2 = Question.create(question_text="5 * 6 = ?", question_status="new", applicant=maria)
question3 = Question.create(question_text="3 - 7 = ?", question_status="waiting for answer", applicant=maria)
question4 = Question.create(question_text="15 * 3 = ?", question_status="new", applicant=maria)
question5 = Question.create(question_text="16 / 4 = ?", question_status="answered", applicant=ilona)
question6 = Question.create(question_text="10 * 10 = ?", question_status="answered", applicant=lajos)

# generate answers
answer1 = Answer.create(answer_text="4", question=question1)
answer1 = Answer.create(answer_text="4", question=question5)
answer1 = Answer.create(answer_text="100", question=question6)

# generate interviews
Interview.create(date_time=datetime(2016, 12, 6, 15, 10), mentor=mikimentor, applicant=antal)
Interview.create(date_time=datetime(2016, 8, 7, 13, 20), mentor=danimentor, applicant=maria)
Interview.create(date_time=datetime(2016, 10, 5, 16, 40), mentor=danimentor, applicant=ilona)
Interview.create(date_time=datetime(2016, 9, 4, 18, 50), mentor=krakowmentor, applicant=lajos)
