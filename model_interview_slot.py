# Interview_slot table contains the mentor's free time for the interviews

from model_mentor import *
from model_applicant import *
from model_interview import *


class Interview_slot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name="mentor")

    # Return the list of the slots not reserved
    @classmethod
    def get_mentor_object_list_not_reserved(cls):
        interview_slot_object_list = list(cls.select().where(cls.reserves == False))
        print(len(interview_slot_object_list))
        return interview_slot_object_list

    # Find two not reserved mentor in the applicant's school and return interview start, mentor_1, mentor_2
    @classmethod
    def get_interview_for_applicants(cls, object_list):
        object_list = Applicant.new_applicant()
        for i in object_list:
            break_boolean = False
            interview_slot_object_list = cls.get_mentor_object_list_not_reserved()
            for j in interview_slot_object_list:
                if break_boolean:
                    break
                elif j.mentor.school_id == i.school_id:
                    for k in interview_slot_object_list:
                        if k.mentor.id != j.mentor.id and k.start == j.start and k.mentor.school_id == i.school_id:
                            j.reserved = True
                            j.save()
                            k.reserved = True
                            k.save()
                            Interview.create(
                                date_time=j.start,
                                mentor_1=j.mentor,
                                mentor_2=k.mentor,
                                applicant=i)
                            break_boolean = True
                            break
