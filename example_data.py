# This script can generate example data for "City" and "InterviewSlot" models.
from model_city import *
from model_school import *


# generating schools
ccbudapest = School.create(name="CodecoolBudapest")
ccmiskolc = School.create(name="CodecoolMiskolc")
cckrakow = School.create(name="CodecoolKrakow")

# generating cities
City.create(name="Kaposvár", school=ccbudapest)
City.create(name="Érd", school=ccbudapest)
City.create(name="Visegrád", school=ccbudapest)
City.create(name="Veszprém", school=ccbudapest)
City.create(name="Sopron", school=ccbudapest)
City.create(name="Kecskemét", school=ccbudapest)
City.create(name="Győr", school=ccbudapest)
City.create(name="Gödöllő", school=ccbudapest)
City.create(name="Hatvan", school=ccbudapest)
City.create(name="Vác", school=ccbudapest)
City.create(name="Eger", school=ccmiskolc)
City.create(name="Nyíregyháza", school=ccmiskolc)
City.create(name="Debrecen", school=ccmiskolc)
City.create(name="Kiskőrös", school=ccmiskolc)
City.create(name="Gyula", school=ccmiskolc)
City.create(name="Hajdúszoboszló", school=ccmiskolc)
City.create(name="Kassa", school=ccmiskolc)
City.create(name="Wieliczka", school=cckrakow)
City.create(name="Liszki", school=cckrakow)
City.create(name="Katowice", school=cckrakow)
City.create(name="Varsó", school=cckrakow)
City.create(name="Berlin", school=cckrakow)
