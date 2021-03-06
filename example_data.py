# This script drops all tables and generates news with some data for testing

# import build for drop and create tables
from build import *

# import needed libraries
from datetime import datetime
from random import choice

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

# generating e_mail list
e = ["emptyandthe+{}@gmail.com".format(i) for i in range(1, 19)]

# generating mentors
danimentor = Mentor.create(first_name="Dániel", last_name="Salamon", school=class_budapest,
                           mentor_password=111111, email=e[10])
mikimentor = Mentor.create(first_name="Miklós", last_name="Beöthy", school=class_budapest,
                           mentor_password=222222, email=e[11])
tomimentor = Mentor.create(first_name="Tamás", last_name="Tompa", school=class_budapest,
                           mentor_password=333333, email=e[12])
miskolcmentor_1 = Mentor.create(first_name="Mihály", last_name="Miskolc", school=class_miskolc,
                                mentor_password=444444, email=e[13])
miskolcmentor_2 = Mentor.create(first_name="Manfréd", last_name="Miskolc", school=class_miskolc,
                                mentor_password=888888, email=e[14])
krakowmentor = Mentor.create(first_name="Károly", last_name="Krakow", school=class_krakow,
                             mentor_password=555555, email=e[15])
polandmentor = Mentor.create(first_name="Lewandowski", last_name="Robert", school=class_krakow,
                             mentor_password=666666, email=e[16])
polishmentor = Mentor.create(first_name="Jackson", last_name="Polish", school=class_krakow,
                             mentor_password=77777, email=e[17])


# generate applicants with given parameters for testing
antal = Applicant.create(first_name="Antal", last_name="Szűcs", city=city_gyor, application_code=11111, email=e[5])
maria = Applicant.create(first_name="Mária", last_name="Kocsis", city=city_hatvan, application_code=22222, email=e[6])
python = Applicant.create(first_name="Monthy", last_name="Python", city=city_hatvan, application_code=33333, email=e[7])
ilona = Applicant.create(first_name="Ilona", last_name="Szabó", city=city_sopron, application_code=44444, email=e[8])
lajos = Applicant.create(first_name="Lajos", last_name="Tóth", city=city_sopron, application_code=55555, email=e[9])

# generate questions
question1 = Question.create(question_text="2 + 2 = ?", question_status="waiting for answer", applicant=antal,
                            mentor=danimentor, date_time=datetime(2016, 10, 7, 15, 10))
question2 = Question.create(question_text="5 * 6 = ?", question_status="waiting for answer", applicant=maria,
                            date_time=datetime(2016, 9, 6, 13, 10))
question3 = Question.create(question_text="3 - 7 = ?", question_status="waiting for answer", applicant=maria,
                            mentor=mikimentor, date_time=datetime(2016, 9, 12, 14, 10))
question4 = Question.create(question_text="15 * 3 = ?", question_status="new", applicant=maria,
                            date_time=datetime(2016, 9, 17, 16, 10))
question5 = Question.create(question_text="16 / 4 = ?", question_status="waiting for answer",
                            applicant=ilona, mentor=tomimentor, date_time=datetime(2016, 10, 10, 13, 10))
question6 = Question.create(question_text="10 * 10 = ?", question_status="waiting for answer",
                            applicant=lajos, mentor=tomimentor, date_time=datetime(2016, 9, 2, 13, 10))


# generate interview slots
InterviewSlot.create(
    start=datetime(
        2016, 9, 6, 13, 10), end=datetime(
            2016, 9, 6, 14, 10), reserved=False, mentor=mikimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 6, 13, 10), end=datetime(
            2016, 9, 6, 14, 10), reserved=False, mentor=tomimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 6, 13, 10), end=datetime(
            2016, 9, 6, 14, 10), reserved=False, mentor=danimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 8, 13, 10), end=datetime(
            2016, 9, 8, 14, 10), reserved=False, mentor=mikimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 8, 13, 10), end=datetime(
            2016, 9, 8, 14, 10), reserved=False, mentor=tomimentor)
InterviewSlot.create(
    start=datetime(
        2016, 10, 8, 13, 10), end=datetime(
            2016, 9, 10, 14, 10), reserved=False, mentor=mikimentor)
InterviewSlot.create(
    start=datetime(
        2016, 10, 8, 13, 10), end=datetime(
            2016, 9, 10, 14, 10), reserved=False, mentor=tomimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 12, 9, 30), end=datetime(
            2016, 9, 12, 10, 30), reserved=False, mentor=mikimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 15, 11, 00), end=datetime(
            2016, 9, 15, 12, 00), reserved=False, mentor=danimentor)
InterviewSlot.create(
    start=datetime(
        2016, 9, 6, 13, 10), end=datetime(
            2016, 9, 6, 14, 10), reserved=False, mentor=miskolcmentor_1)
InterviewSlot.create(
    start=datetime(
        2016, 9, 6, 13, 10), end=datetime(
            2016, 9, 6, 14, 10), reserved=False, mentor=miskolcmentor_2)
InterviewSlot.create(
    start=datetime(
        2016, 5, 6, 13, 10), end=datetime(
            2016, 9, 5, 14, 10), reserved=False, mentor=mikimentor)
InterviewSlot.create(
    start=datetime(
        2016, 5, 6, 13, 10), end=datetime(
            2016, 9, 5, 14, 10), reserved=False, mentor=tomimentor)
