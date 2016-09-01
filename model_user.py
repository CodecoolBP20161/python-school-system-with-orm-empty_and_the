from model_base import *


class User(BaseModel):
    username = CharField()
    password = CharField()
