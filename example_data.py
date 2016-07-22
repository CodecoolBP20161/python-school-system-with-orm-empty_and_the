# This script can generate example data for "City" and "InterviewSlot" models.
from model_city import *


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
