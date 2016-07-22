from model_mentor import *
from model_school import *
from example_data import *


danimentor = Mentor.create(first_name="Dániel", last_name="Salamon", school=class_budapest, mentor_password=11111)
mikimentor = Mentor.create(first_name="Miklós", last_name="Beöthy", school=class_budapest, mentor_password=22222)
tomimentor = Mentor.create(first_name="Tamás", last_name="Tompa", school=class_budapest, mentor_password=33333)
miskolcmentor = Mentor.create(first_name="Mihály", last_name="Miskolc", school=class_miskolc, mentor_password=44444)
krakowmentor = Mentor.create(first_name="Károly", last_name="Krakow", school=class_krakow, mentor_password=55555)
