# Interview_slot table contains the mentor's free time for the interviews

from model_mentor import *


class Interview_slot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name="mentor")

    # Return the list of the slots not reserved
    @classmethod
    def get_mentor_object_list_not_reserved(cls):
        interview_slot_object_list = list(cls.select().where(cls.reserved == False))
        return interview_slot_object_list

    # Find two not reserved mentor in the applicant's school and return interview start, mentor_1, mentor_2
    @classmethod
    def get_free_mentor_pair(cls, object_list):
        interview_slot_object_list = cls.get_mentor_object_list_not_reserved
        for element in interview_slot_object_list:
            if element.mentor.school.name == school:
                for element2 in interview_slot_object_list:
                    if (element2.mentor.id != element.mentor.id) and (element2.start == element.start):
                        return element.start, element.mentor.first_name, element2.mentor.first_name
