from model_base import *


class Applicant(BaseModel):
    name = CharField()
    city = CharField()
    application_code = IntegerField(default=None)
    school = CharField(default=None)
    status = CharField(default="new")
