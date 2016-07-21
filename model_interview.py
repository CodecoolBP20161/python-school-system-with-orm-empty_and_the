from model_applicant import *


class Interview(BaseModel):
    date_time = DateTimeField()
    mentor = CharField()
    applicant = ForeignKeyField(Applicant, related_name="interview")
