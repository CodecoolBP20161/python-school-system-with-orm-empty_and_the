from model_base import *
from model_school import School


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, related_name="location")
