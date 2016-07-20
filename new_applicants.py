# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from model_base import *
from model_applicant import *

Applicant.create(name="Smith, John", city="Varsó")
Applicant.create(name="Smith, Jane", city="Liszki")
Applicant.create(name="Smith, Johnny", city="Berlin")
Applicant.create(name="Kovács, János", city="Nyíregyháza")
Applicant.create(name="Molnár, László", city="Debrecen")
Applicant.create(name="Szűcs, Antal", city="Győr")
Applicant.create(name="Kocsis, Mária", city="Hatvan")
Applicant.create(name="Monthy, Python", city="Kassa")
Applicant.create(name="Szabó, Ilona", city="Gödöllő")
Applicant.create(name="Tóth, Lajos", city="Veszprém")
