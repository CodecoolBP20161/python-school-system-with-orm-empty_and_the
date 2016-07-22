# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from model_base import *
from model_applicant import *
from example_data import *
from datetime import datetime
from model_interview import *
from new_mentors import *

Applicant.create(first_name="Smith", last_name="John", city=city_varso)
Applicant.create(first_name="Smith", last_name="Jane", city=city_liszki)
Applicant.create(first_name="Smith", last_name="Johnny", city=city_berlin)
Applicant.create(first_name="Kovács", last_name="János", city=city_debrecen)
Applicant.create(first_name="Molnár", last_name="László", city=city_debrecen)


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
