# Interview_slot table contains the mentor's free time for the interviews

from model_mentor import *


class Interview_slot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor)
